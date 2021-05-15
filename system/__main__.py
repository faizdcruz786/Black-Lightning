# Copyright (C) 2021 KeinShin@Github.
from subprocess import *
import os.path
import sys

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pickle as yum
import logging 

import schedule

from system.decorators import easters
import pyrogram


from pyrogram.raw.types import BotCommand
from setup.importer import *
logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.ERROR)
import holidays
from datetime import date, datetime

hol  = holidays.CountryHoliday('IN', prov="AS")
a = date.today()
p  =hol.get(a)



plugin =  logging.getLogger("PLUG-ERROR")
bot_lod =  logging.getLogger("BOT-ERROR")


from system import app, bot, ASSISTANT_LIST

from system.user_bot_assistant import ASSISTANT_HELP
from Config import *

chet = Variable.LOGS_CHAT_ID


USER = str(Variable.OWNER_NAME)

async def easter():
    # if Variable./
    est=yum.load("easters.dat", "rb") # for easters!
    if len(est)==7:
        await bot.send_message(chet, "**Congo**, **You have unlocked all the easters of this userbot gib party sir** 🎉🎆")

async def holydays():
    if p:
        await bot.send_message(chet, f"Happy {p} Master ✨🎉☺")
    else:
        return None


schedule.every().day.at("12:00").do(holydays)



async def add_bot_to_logg_grup():
    try: 

        await bot.join_chat(chet)
        text = f"BLACK USERBOT is deployed."
        async with bot.send_chat_action(chet, action="Typing"):
           await bot.send_message(chet, text)
    except BaseException:

        logging.error("CANNOT ADD ASSISTANT TO LOGS CHAT")
        


import glob
import importlib

async def start():

        await app.start()

        os.system("sh_files/load.sh")
        os.system("sh_files/assist.sh")
        info = f"Everything is loaded, Black Lightning is Online check your saved message and bot is added to LOG CHANNEL "
        
        logging.info(info)
        
        await pyrogram.idle()
        await  app.send_message("me", f"**BLACK-LIGHTNING USERBOT's MESSAGE\n\n{USER} Kindly Enable Inline from @BotFather to Access All The Features Including `.help` and Many More (if it's already done Ignore this message)")



app.loop.run_until_complete(start()) 
bot.loop.run_until_complete(add_bot_to_logg_grup())