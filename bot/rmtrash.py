# Copyright (C) 2021 By WoofMusic

import os
from pyrogram import Client, filters
from pyrogram.types import Message
from helpers.filters import command
from helpers.decorators import sudo_users_only, errors

downloads = os.path.realpath("bot/downloads")
raw = os.path.realpath(".")

@Client.on_message(command(["rmd", "cleardl"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_downloads(_, message: Message):
    ls_dir = os.listdir(downloads)
    if ls_dir:
        for file in os.listdir(downloads):
            os.remove(os.path.join(downloads, file))
        await message.reply_text("✅ **deleted all downloaded files**")
    else:
        await message.reply_text("❌ **no files downloaded**")
        
@Client.on_message(command(["clean", "wipe", "rmw"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_raw(_, message: Message):
    ls_dir = os.listdir(raw)
    if ls_dir:
        for file in os.listdir(raw):
            if file.endswith('.raw'):
                os.remove(os.path.join(raw, file))
        await message.reply_text("✅ **deleted all raw files**")
    else:
        await message.reply_text("❌ **no raw files**")

@Client.on_message(command(["ya"]) & ~filters.edited)
# edit if u want
async def haduhh(_, message: Message):
    pth = os.path.realpath(".")
    ls_dir = os.listdir(pth)
    if ls_dir:
        for dta in os.listdir(pth):
            os.system("rm -rf *.raw *.jpg")
        await message.reply_text("Oke")
    else:
        await message.reply_text("sip")