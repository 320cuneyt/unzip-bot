# Copyright (c) 2022 EDM115

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Inline buttons
class Buttons:
    START_BUTTON = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("Help 📜", callback_data="helpcallback"),
                InlineKeyboardButton("About 👀", callback_data="aboutcallback")
            ]
        ])

    CHOOSE_E_F__BTNS = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("🗂️ Archive extract", callback_data="extract_file|tg_file|no_pass"),
            ],
            [
                InlineKeyboardButton("🗂️ Extract a password protected archive 🔐", callback_data="extract_file|tg_file|with_pass")
            ],
            [
                InlineKeyboardButton("❌ Cancel", callback_data="cancel_dis")
            ]
        ])

    CHOOSE_E_U__BTNS = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("🔗 URL extract", callback_data="extract_file|url|no_pass"),
            ],
            [
                InlineKeyboardButton("🔗 URL extract (but password protected) 🔐", callback_data="extract_file|url|with_pass")
            ],
            [
                InlineKeyboardButton("❌ Cancel", callback_data="cancel_dis")
            ]
        ])

    CLN_BTNS = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("Clean my files 🚮", callback_data="cancel_dis")
            ],
            [
                InlineKeyboardButton("❌ Cancel", callback_data="nobully")
            ]
        ])

    ME_GOIN_HOME = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("Back 🏡", callback_data="megoinhome")
            ]
        ])

    SET_UPLOAD_MODE_BUTTONS = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("As document 📁", callback_data="set_mode|doc")
            ],
            [
                InlineKeyboardButton("As video 📹", callback_data="set_mode|video")
            ]
        ])

    I_PREFER_STOP = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("❌ Cancel", callback_data="canceldownload")
            ]
        ])

    MERGE_THEM_ALL = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("Merge 🛠️", callback_data=f"merge_this|{startid}|{stopid}")
            ],
            [
                InlineKeyboardButton("❌ Cancel", callback_data="nobully")
            ]
        ])


class Messages:
    START_TEXT = """
Hi **{}** 👋, I'm **Unarchiver bot** 🥰
**This is BETA version !** May be a lot buggy, but with new features. Better waiting for the stable version at daytime… 🙂

I can extract archives like `zip`, `rar`, `tar`, …

**Made with ❤️ by @EDM115bots**
    """

    HELP_TXT = """
**• How to extract 🤔**

    **1)** Send the file or link that you want to extract
    **2)** Click on extract button (If you sent a link use `🔗 URL extract` button. If it's a file just use `🗂️ Archive extract` button)


**• How to change upload mode 🤔**
    Send **/mode** command to the bot. You can change upload mode from there


**Note :**
    **1.** If your archive is password protected select `🗂️ Extract a password protected archive 🔐` mode. Bot isn’t a god to know your file’s password, so if this happens just send that password !
    **2.** Please don’t send corrupted files ! If you sent one by mistake just send **/clean** command
    **3.** If your archive have +95 files in it then bot can’t show all of extracted files to select from. So in that case if you can’t see your file in the buttons just click on `Upload all 📤` button. It will send all extracted files to you !


**• I wanna have help 🥺**

    PM me at **@EDM115**, I'm always here and open for anything 😘
    """

    ABOUT_TXT = """
**About Unarchiver bot [BETA | v4.4.0]**

• **Language :** [Python 3.9.1](https://www.python.org/)
• **Framework :** [Pyrogram 1.4.16](https://docs.pyrogram.org/)
• **Source code :** [EDM115/unzip-bot[beta]](https://github.com/EDM115/unzip-bot/tree/beta)
• **Developer :** [EDM115](https://github.com/EDM115)

**Made with ❤️ by @EDM115bots**
    """

    LOG_TXT = """
**Extract log 📝**

**User ID :** `{}`
**File Name :** `{}`
**File Size :** `{}`
    """

    PASS_TXT = """
**Password of above archive is 🔑**

`{}`
    """

    AFTER_OK_DL_TXT = """
**Successfully downloaded ✅**

**Download time :** `{}`
**Status :** Trying to extract the archive… Please wait
    """

    EXT_OK_TXT = """
**Extraction successful ✅**

**Extraction time :** `{}`
**Status :** Processing the extracted files… Please wait
    """

    EXT_CAPTION = """
`{}`

Successfully extracted by @unzip_edm115bot 🥰
    """

    URL_UPLOAD = """
`{}` is too huge to be uploaded to Telegram (`{}`)

Instead, I made it available here : {} 🥰
    """

    URL_ERROR = """
An error hapenned for `{}` 😕

**Error code :** `{}`
**Error type :** `{}`
**Error message :** `{}`

Please report this at @EDM115 if you think this is a serious error
    """

    LOG_CAPTION = """
**The file : ** `{}`

have been saved from

`{}` ** URL**
    """

    START_TXT = """
ℹ️ The bot have successfully started at `{}` 💪
    """

    STOP_TXT = """
ℹ️ The bot goes sleeping at `{}` 😴
    """

    EXT_FAILED_TXT = """
**Extraction failed 😕**

**What to do ?**

   • Please make sure archive isn’t corrupted
   • Please make sure that you selected the right mode !
   • Also check if you sent the right password (it's case sensitive)
   • Maybe your archive format isn’t supported yet 😔
   • If you sent splitted archives (.001, .part1, .00001, …), then I can’t extract them 🙂 (for the moment)


**IN ALL CASES**, please send **/clean**, else you couldn’t send any other task 🙂🔫 (may be fixed in the future)

Please report this at @EDM115 if you think this is a serious error
    """

    ERROR_TXT = """
**Error happened 😕**

**ERROR :** `{}`

Please report this at @EDM115 if you think this is a serious error
    """

    CANCELLED_TXT = """
**{} ✅**

Now all of your files have been deleted from my server 😌
    """

    DL_STOPPED = """
✅ The download of your file have successfully been cancelled 😌
    """

    HOW_MANY_UPLOADED = """
`{}` files were extracted from that archive
    """

    CLEAN_TXT = """
**Are sure want to delete your files from my server 🤔**

Note : This action cannot be undone !
    """

    SELECT_UPLOAD_MODE_TXT = """
Please select the upload mode by clicking on below buttons 👇

**Current upload mode is :** `{}`
    """

    CHANGED_UPLOAD_MODE_TXT = """
**Successfully changed upload mode to** `{}` ✅
    """

    SAVED_THUMBNAIL = """
**Successfully saved this thumbnail ✅**
    """

    DELETED_THUMB = """
**Successfully removed your thumbnail ✅**
    """
    
    PLS_REPLY = """
You need to reply to a picture for saving it as custom thumbnail 😃
    """

# List of error messages from p7zip
ERROR_MSGS = [
    "Error",
    "Can't open as archive"
    ]
