#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import os
import asyncio
from robote import(EDIT_SLEEP_TIME_OUT,DESTINATION_FOLDER,UPLOADER_CONFIG)
from pyrogram import(InlineKeyboardButton,InlineKeyboardMarkup,Message)
async def check_size_g(client,message):
 del_it=await message.reply_text("🔊 Checking size...wait!!!")
 if not os.path.exists('memek.conf'):
  with open('memek.conf','a',newline="\n",encoding='utf-8')as fole:
   fole.write("[DRIVE]\n")
   fole.write(f"{UPLOADER_CONFIG}")
 destination=f'{DESTINATION_FOLDER}'
 gau_tam=subprocess.Popen(['memek','size','--config=./memek.conf','DRIVE:'f'{destination}'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 gau,tam=gau_tam.communicate()
 print(gau)
 print(tam)
 print(tam.decode("utf-8"))
 gautam=gau.decode("utf-8")
 print(gautam)
 await asyncio.sleep(5)
 await message.reply_text(f"🔊CloudInfo:\n\n{gautam}")
 await del_it.delete()
async def g_clearme(client,message):
 inline_keyboard=[]
 ikeyboard=[]
 ikeyboard.append(InlineKeyboardButton("Yes 🚫",callback_data=("fuckingdo").encode("UTF-8")))
 ikeyboard.append(InlineKeyboardButton("No 🤗",callback_data=("fuckoff").encode("UTF-8")))
 inline_keyboard.append(ikeyboard)
 reply_markup=InlineKeyboardMarkup(inline_keyboard)
 await message.reply_text("Are you sure? 🚫 This will delete all your downloads locally 🚫",reply_markup=reply_markup,quote=True)