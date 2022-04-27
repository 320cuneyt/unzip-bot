# Copyright (c) 2022 EDM115

import subprocess
import os
import re
import shutil

from time import time
from aiohttp import ClientSession
from aiofiles import open as openfile
from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardButton
from pykeyboard import InlineKeyboard
from config import Config

## Run commands in shell
async def __run_cmds_unzipper(command):
    ext_cmd = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, check=True, universal_newlines=True)
    ext_out = ext_cmd.stdout.read()[:-1].decode("utf-8")
    return ext_out

## Extract with 7z
async def _extract_with_7z_helper(path, archive_path, password=None):
    if password:
        command = f"7z x -o{path} -p{password} {archive_path} -y"
    else:
        command = f"7z t {archive_path} -pIAmVeryProbablySureThatThisPasswordWillNeverBeUsedElseItsVeryStrangeAAAAAAAAAAAAAAAAAAA -y"
        ext_cmd = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, check=True, universal_newlines=True)
        ext_out = ext_cmd.stdout.read()[:-1].decode("utf-8")
        if "Everything is Ok" in ext_out:
            command = f"7z x -o{path} {archive_path} -y"
        else:
            await unzip_bot.send_message(chat_id=Config.LOGS_CHANNEL, text="That archive is password protected 😡")
            await unzip_bot.send_message(chat_id=query.message.chat.id, text="That archive is password protected 😡 Don't fool me !")
            command = f"exit"
    return await __run_cmds_unzipper(command)

##Extract with zstd (for .zst files)
async def _extract_with_zstd(path, archive_path):
    command = f"zstd -f --output-dir-flat {path} -d {archive_path}"
    return await __run_cmds_unzipper(command)

# Main function to extract files
async def extr_files(path, archive_path, password=None):
    file_path = os.path.splitext(archive_path)[1]
    if file_path == ".zst":
        os.mkdir(path)
        ex = await _extract_with_zstd(path, archive_path)
        return ex
    else:
        ex = await _extract_with_7z_helper(path, archive_path, password)
        return ex

# Get files in directory as a list
async def get_files(path):
    path_list = []
    for r, d, f in os.walk(path):
        for file in f:
            path_list.append(os.path.join(r, file))
    return path_list

# Make keyboard
async def make_keyboard(paths, user_id, chat_id):
    num = 0
    i_kbd = InlineKeyboard(row_width=1)
    data = []
    data.append(
        InlineKeyboardButton(f"Upload all 📤", f"ext_a|{user_id}|{chat_id}")
    )
    data.append(
        InlineKeyboardButton("❌ Cancel", "cancel_dis")
    )
    for file in paths:
        data.append(
            InlineKeyboardButton(f"{num} - {os.path.basename(file)}".encode("utf-8").decode("utf-8"), f"ext_f|{user_id}|{chat_id}|{num}")
        )
        num += 1
    i_kbd.add(*data)
    return i_kbd


### --- Saved for later --- ###
# async def make_keyboard(paths, user_id, chat_id):
#     num = 0
#     i_kbd = []
#     for file in paths:
#         i_kbd.append(
#             [InlineKeyboardButton(f"{num} - {os.path.basename(file)}", f"ext_f|{user_id}|{chat_id}|{num}")]
#         )
#         num += 1
#     i_kbd.append(
#         [InlineKeyboardButton(f"Upload all 📤", f"ext_a|{user_id}|{chat_id}")]
#     )
#     i_kbd.append(
#         [InlineKeyboardButton("❌ Cancel", callback_data="cancel_dis")]
#     )
#     return i_kbd
