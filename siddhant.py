import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
from Config import STRING, ALIVE_NAME, USERNAME, SUDO, BIO_MESSAGE, API_ID, API_HASH, STRING2, STRING3, STRING4 ,STRING5, STRING6, STRING7, STRING8 ,STRING9, STRING10, STRING11, STRING12 , STRING13 , STRING14 , STRING15 ,STRING16 , STRING17 , STRING18 , STRING19 , STRING20 , STRING21 , STRING22 , STRING23 , STRING24 , STRING25, STRING26, STRING27, STRING28 ,STRING29, STRING30, STRING31, STRING32 ,STRING33, STRING34, STRING35, STRING36 , STRING37 , STRING38 , STRING39 , STRING40
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Utils import RAID, RRAID


a = API_ID
b = API_HASH
smex = STRING
smexx = STRING2
smexxx = STRING3
smexxxx = STRING4
smexxxxx = STRING5
sixth = STRING6
seven = STRING7
eight = STRING8
ninth = STRING9
tenth = STRING10
eleve = STRING11
twelv = STRING12
thirt = STRING13
forte = STRING14
fifth = STRING15
sieee = STRING16
seeee = STRING17
eieee = STRING18
nieee = STRING19
gandu = STRING20
ekish = STRING21
baish = STRING22
teish = STRING23
tfour = STRING24
tfive = STRING25
steeee = STRING26
sheeee = STRING27
eleeee = STRING28
npeeee = STRING29
pizza = STRING30
bimsish = STRING31
kimish = STRING32
kaju = STRING33
katli = STRING34
papadi = STRING35
sieeee = STRING36
seeeee = STRING37
eieeee = STRING38
nieeee = STRING39
nunni = STRING40


idk = ""
ydk = ""
wdk = ""
sdk = ""
hdk = ""
adk = ""
bdk = ""
cdk = ""
edk = ""
ddk = ""
vkk = ""
kkk = ""
lkk = ""
mkk = ""
sid = ""
shy = ""
aan = ""
ake = ""
eel = ""
khu = ""
shi = ""
yaa = ""
dav = ""
raj = ""
put = ""
idg = ""
ydg = ""
wdg = ""
sdg = ""
hdg = ""
adg = ""
bdg = ""
cdg = ""
edg = ""
ddg = ""
vgg = ""
ggg = ""
lgg = ""
mgg = ""
kit = ""


que = {}

SMEX_USERS = []
for x in SUDO: 
    SMEX_USERS.append(x)
    
async def start_yukki():
    global idk
    global ydk
    global wdk
    global sdk
    global hdk
    global adk
    global bdk
    global cdk
    global ddk
    global edk
    global vkk
    global kkk
    global lkk
    global mkk
    global sid
    global shy
    global aan
    global ake
    global eel
    global khu
    global shi
    global yaa
    global dav
    global raj
    global put
    global idg
    global ydg
    global wdg
    global sdg
    global hdg
    global adg
    global bdg
    global cdg
    global ddg
    global edg
    global vgg
    global ggg
    global lgg
    global mgg
    global kit
    
    if smex:
        session_name = str(smex)
        print("String 1 Found")
        idk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 1")
            await idk.start()
            botme = await idk.get_me()
            await idk(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await idk(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await idk(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await idk(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            idk = "smex"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "startup"
        idk = TelegramClient(session_name, a, b)
        try:
            await idk.start()
        except Exception as e:
            pass
   
    if smexx:
        session_name = str(smexx)
        print("String 2 Found")
        ydk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 2")
            await ydk.start()
            await ydk(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await ydk(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await ydk(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await ydk(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botme = await ydk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "startup"
        ydk = TelegramClient(session_name, a, b)
        try:
            await ydk.start()
        except Exception as e:
            pass

    if smexxx:
        session_name = str(smexxx)
        print("String 3 Found")
        wdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 3")
            await  wdk.start()
            await wdk(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await wdk(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await wdk(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await wdk(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botme = await wdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "startup"
        wdk = TelegramClient(session_name, a, b)
        try:
            await wdk.start()
        except Exception as e:
            pass

    if smexxxx:
        session_name = str(smexxxx)
        print("String 4 Found")
        hdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 4")
            await hdk.start()
            await hdk(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await hdk(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await hdk(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await hdk(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botme = await hdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "startup"
        hdk = TelegramClient(session_name, a, b)
        try:
            await hdk.start()
        except Exception as e:
            pass

    if smexxxxx:
        session_name = str(smexxxxx)
        print("String 5 Found")
        sdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 5")
            await sdk.start()
            await sdk(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await sdk(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await sdk(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await sdk(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botme = await sdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "startup"
        sdk = TelegramClient(session_name, a, b)
        try:
            await sdk.start()
        except Exception as e:
            pass
                  
    if sixth:
        session_name = str(sixth)
        print("String 6 Found")
        adk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 6")
            await adk.start()
            await adk(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await adk(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await adk(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await adk(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botme = await adk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = "startup"
        adk = TelegramClient(session_name, a, b)
        try:
            await adk.start()
        except Exception as e:
            pass

    if seven:
        session_name = str(seven)
        print("String 7 Found")
        bdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 7")
            await bdk.start()
            await bdk(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await bdk(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await bdk(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await bdk(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botme = await bdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = "startup"
        bdk = TelegramClient(session_name, a, b)
        try:
            await bdk.start()
        except Exception as e:
            pass    
        
    
    if eight:
        session_name = str(eight)
        print("String 8 Found")
        cdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 8")
            await cdk.start()
            await cdk(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await cdk(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await cdk(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await cdk(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botme = await cdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = "startup"
        cdk = TelegramClient(session_name, a, b)
        try:
            await cdk.start()
        except Exception as e:
            pass   
        
    if ninth:
        session_name = str(ninth)
        print("String 9 Found")
        ddk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 9")
            await ddk.start()
            await ddk(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await ddk(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await ddk(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await ddk(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botme = await ddk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = "startup"
        ddk = TelegramClient(session_name, a, b)
        try:
            await ddk.start()
        except Exception as e:
            pass   
    
  
    if tenth:
        session_name = str(tenth)
        print("String 10 Found")
        edk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 10")
            await edk.start()
            await edk(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await edk(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await edk(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await edk(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botme = await edk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = "startup"
        edk = TelegramClient(session_name, a, b)
        try:
            await edk.start()
        except Exception as e:
            pass 
        
    
    if eleve:
        session_name = str(eleve)
        print("String 11 Found")
        vkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 11")
            await vkk.start()
            await vkk(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await vkk(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await vkk(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await vkk(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botme = await vkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 11 not Found")
        pass
        session_name = "startup"
        vkk = TelegramClient(session_name, a, b)
        try:
            await vkk.start()
        except Exception as e:
            pass
        
    
    if twelv:
        session_name = str(twelv)
        print("String 12 Found")
        kkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 12")
            await kkk.start()
            await kkk(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await kkk(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await kkk(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await kkk(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botme = await kkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 12 not Found")
        pass
        session_name = "startup"
        kkk = TelegramClient(session_name, a, b)
        try:
            await kkk.start()
        except Exception as e:
            pass   
    
  
    if thirt:
        session_name = str(thirt)
        print("String 13  Found")
        lkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 13")
            await lkk.start()
            await lkk(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await lkk(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await lkk(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await lkk(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botme = await lkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 13 not Found")
        pass
        session_name = "startup"
        lkk = TelegramClient(session_name, a, b)
        try:
            await lkk.start()
        except Exception as e:
            pass 
        
    
    if forte:
        session_name = str(forte)
        print("String 14 Found")
        mkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 14")
            await mkk.start()
            await mkk(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await mkk(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await mkk(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await mkk(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botme = await mkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 14 not Found")
        pass
        session_name = "startup"
        mkk = TelegramClient(session_name, a, b)
        try:
            await mkk.start()
        except Exception as e:
            pass
        
    
    if fifth:
        session_name = str(fifth)
        print("String 15 Found")
        sid = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 15")
            await sid.start()
            await sid(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await sid(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await sid(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await sid(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botme = await sid.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 15 not Found")
        pass
        session_name = "startup"
        sid = TelegramClient(session_name, a, b)
        try:
            await sid.start()
        except Exception as e:
            pass


    if sieee:
        session_name = str(sieee)
        print("String 16 Found")
        shy = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 16")
            await shy.start()
            botme = await shy.get_me()
            await shy(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await shy(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await shy(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await shy(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 16 not Found")
        session_name = "startup"
        shy = TelegramClient(session_name, a, b)
        try:
            await shy.start()
        except Exception as e:
            pass
   
    if seeee:
        session_name = str(seeee)
        print("String 17 Found")
        aan = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 17")
            await aan.start()
            botme = await aan.get_me()
            await aan(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await aan(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await aan(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await aan(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 17 not Found")
        session_name = "startup"
        aan = TelegramClient(session_name, a, b)
        try:
            await aan.start()
        except Exception as e:
            pass
   
    if eieee:
        session_name = str(eieee)
        print("String 18 Found")
        ake = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 18")
            await ake.start()
            botme = await ake.get_me()
            await ake(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await ake(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await ake(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await ake(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 18 not Found")
        session_name = "startup"
        ake = TelegramClient(session_name, a, b)
        try:
            await ake.start()
        except Exception as e:
            pass
   
    if nieee:
        session_name = str(nieee)
        print("String 19 Found")
        eel = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 19")
            await eel.start()
            botme = await eel.get_me()
            await eel(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await eel(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await eel(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await eel(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 19 not Found")
        session_name = "startup"
        eel = TelegramClient(session_name, a, b)
        try:
            await idk.start()
        except Exception as e:
            pass
   
    if gandu:
        session_name = str(gandu)
        print("String 20 Found")
        khu = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 20")
            await khu.start()
            botme = await khu.get_me()
            await khu(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await khu(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await khu(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await khu(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 20 not Found")
        session_name = "startup"
        khu = TelegramClient(session_name, a, b)
        try:
            await khu.start()
        except Exception as e:
            pass
   
    if ekish:
        session_name = str(ekish)
        print("String 21 Found")
        shi = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 21")
            await shi.start()
            botme = await shi.get_me()
            await shi(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await shi(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await shi(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await shi(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 21 not Found")
        session_name = "startup"
        shi = TelegramClient(session_name, a, b)
        try:
            await shi.start()
        except Exception as e:
            pass
   
    if baish:
        session_name = str(baish)
        print("String 22 Found")
        yaa = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 22")
            await yaa.start()
            botme = await yaa.get_me()
            await yaa(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await yaa(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await yaa(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await yaa(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 22 not Found")
        session_name = "startup"
        yaa = TelegramClient(session_name, a, b)
        try:
            await yaa.start()
        except Exception as e:
            pass
   
    if teish:
        session_name = str(teish)
        print("String 23 Found")
        dav = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 23")
            await dav.start()
            botme = await dav.get_me()
            await dav(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await dav(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await dav(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await dav(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 23 not Found")
        session_name = "startup"
        dav = TelegramClient(session_name, a, b)
        try:
            await dav.start()
        except Exception as e:
            pass
   
    if tfour:
        session_name = str(tfour)
        print("String 24 Found")
        raj = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 24")
            await raj.start()
            botme = await raj.get_me()
            await raj(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await raj(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await raj(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await raj(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 24 not Found")
        session_name = "startup"
        raj = TelegramClient(session_name, a, b)
        try:
            await raj.start()
        except Exception as e:
            pass
   
    if tfive:
        session_name = str(tfive)
        print("String 25 Found")
        put = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 1")
            await put.start()
            botme = await put.get_me()
            await put(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await put(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await put(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await put(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 25 not Found")
        session_name = "startup"
        put = TelegramClient(session_name, a, b)
        try:
            await put.start()
        except Exception as e:
            pass
    if steeee:
        session_name = str(steeee)
        print("String 26 Found")
        idg = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 26")
            await idg.start()
            botme = await idg.get_me()
            await idg(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await idg(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await idg(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await idg(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botid = telethon.utils.get_peer_id(botme)
            steeee_USERS.append(botid)
        except Exception as e:
            idg = "steeee"
            print(e)
            pass
    else:
        print("Session 26 not Found")
        session_name = "startup"
        idg = TelegramClient(session_name, a, b)
        try:
            await idg.start()
        except Exception as e:
            pass
   
    if sheeee:
        session_name = str(sheeee)
        print("String 27 Found")
        ydg = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 27")
            await ydg.start()
            await ydg(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await ydg(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await ydg(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await ydg(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botme = await ydg.get_me()
            botid = telethon.utils.get_peer_id(botme)
            steeee_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 27 not Found")
        pass
        session_name = "startup"
        ydg = TelegramClient(session_name, a, b)
        try:
            await ydg.start()
        except Exception as e:
            pass

    if eleeee:
        session_name = str(eleeee)
        print("String 28 Found")
        wdg = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 28")
            await  wdg.start()
            await wdg(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await wdg(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await wdg(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await wdg(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botme = await wdg.get_me()
            botid = telethon.utils.get_peer_id(botme)
            steeee_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 28 not Found")
        pass
        session_name = "startup"
        wdg = TelegramClient(session_name, a, b)
        try:
            await wdg.start()
        except Exception as e:
            pass

    if npeeee:
        session_name = str(npeeee)
        print("String 29 Found")
        hdg = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 29")
            await hdg.start()
            await hdg(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await hdg(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await hdg(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await hdg(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botme = await hdg.get_me()
            botid = telethon.utils.get_peer_id(botme)
            steeee_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 29 not Found")
        pass
        session_name = "startup"
        hdg = TelegramClient(session_name, a, b)
        try:
            await hdg.start()
        except Exception as e:
            pass

    if pizza:
        session_name = str(pizza)
        print("String 30 Found")
        sdg = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 30")
            await sdg.start()
            await sdg(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await sdg(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await sdg(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await sdg(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botme = await sdg.get_me()
            botid = telethon.utils.get_peer_id(botme)
            steeee_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 30 not Found")
        pass
        session_name = "startup"
        sdg = TelegramClient(session_name, a, b)
        try:
            await sdg.start()
        except Exception as e:
            pass
                  
    if bimsish:
        session_name = str(bimsish)
        print("String 31 Found")
        adg = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 31")
            await adg.start()
            await adg(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await adg(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await adg(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await adg(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botme = await adg.get_me()
            botid = telethon.utils.get_peer_id(botme)
            steeee_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 31 not Found")
        pass
        session_name = "startup"
        adg = TelegramClient(session_name, a, b)
        try:
            await adg.start()
        except Exception as e:
            pass

    if kimish:
        session_name = str(kimish)
        print("String 32 Found")
        bdg = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 32")
            await bdg.start()
            await bdg(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await bdg(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await bdg(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await bdg(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botme = await bdg.get_me()
            botid = telethon.utils.get_peer_id(botme)
            steeee_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 32 not Found")
        pass
        session_name = "startup"
        bdg = TelegramClient(session_name, a, b)
        try:
            await bdg.start()
        except Exception as e:
            pass    
        
    
    if kaju:
        session_name = str(kaju)
        print("String 33 Found")
        cdg = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 33")
            await cdg.start()
            await cdg(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await cdg(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await cdg(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await cdg(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botme = await cdg.get_me()
            botid = telethon.utils.get_peer_id(botme)
            steeee_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 33 not Found")
        pass
        session_name = "startup"
        cdg = TelegramClient(session_name, a, b)
        try:
            await cdg.start()
        except Exception as e:
            pass   
        
    if katli:
        session_name = str(katli)
        print("String 34 Found")
        ddg = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 34")
            await ddg.start()
            await ddg(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await ddg(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await ddg(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await ddg(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botme = await ddg.get_me()
            botid = telethon.utils.get_peer_id(botme)
            steeee_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 34 not Found")
        pass
        session_name = "startup"
        ddg = TelegramClient(session_name, a, b)
        try:
            await ddg.start()
        except Exception as e:
            pass   
    
  
    if papadi:
        session_name = str(papadi)
        print("String 35 Found")
        edg = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 35")
            await edg.start()
            await edg(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await edg(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await edg(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await edg(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botme = await edg.get_me()
            botid = telethon.utils.get_peer_id(botme)
            steeee_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 35 not Found")
        pass
        session_name = "startup"
        edg = TelegramClient(session_name, a, b)
        try:
            await edg.start()
        except Exception as e:
            pass 
        
    
    if sieeee:
        session_name = str(sieeee)
        print("String 36 Found")
        vgg = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 36")
            await vgg.start()
            await vgg(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await vgg(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await vgg(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await vgg(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botme = await vgg.get_me()
            botid = telethon.utils.get_peer_id(botme)
            steeee_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 36 not Found")
        pass
        session_name = "startup"
        vgg = TelegramClient(session_name, a, b)
        try:
            await vgg.start()
        except Exception as e:
            pass
        
    
    if seeeee:
        session_name = str(seeeee)
        print("String 37 Found")
        ggg = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 37")
            await ggg.start()
            await ggg(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await ggg(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await ggg(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await ggg(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botme = await ggg.get_me()
            botid = telethon.utils.get_peer_id(botme)
            steeee_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 37 not Found")
        pass
        session_name = "startup"
        ggg = TelegramClient(session_name, a, b)
        try:
            await ggg.start()
        except Exception as e:
            pass   
    
  
    if eieeee:
        session_name = str(eieeee)
        print("String 38  Found")
        lgg = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 38")
            await lgg.start()
            await lgg(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await lgg(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await lgg(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await lgg(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botme = await lgg.get_me()
            botid = telethon.utils.get_peer_id(botme)
            steeee_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 38 not Found")
        pass
        session_name = "startup"
        lgg = TelegramClient(session_name, a, b)
        try:
            await lgg.start()
        except Exception as e:
            pass 
        
    
    if nieeee:
        session_name = str(nieeee)
        print("String 39 Found")
        mgg = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 39")
            await mgg.start()
            await mgg(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await mgg(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await mgg(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await mgg(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botme = await mgg.get_me()
            botid = telethon.utils.get_peer_id(botme)
            steeee_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 39 not Found")
        pass
        session_name = "startup"
        mgg = TelegramClient(session_name, a, b)
        try:
            await mgg.start()
        except Exception as e:
            pass
    if nunni:
        session_name = str(nunni)
        print("String 40 Found")
        kit = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 40")
            await kit.start()
            await kit(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await kit(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await kit(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await kit(functions.channels.JoinChannelRequest(channel="@RDX_ON_FIRE"))
            botme = await kit.get_me()
            botid = telethon.utils.get_peer_id(botme)
            steeee_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 40 not Found")
        pass
        session_name = "startup"
        kit = TelegramClient(session_name, a, b)
        try:
            await kit.start()
        except Exception as e:
            pass
   
   
loop = asyncio.get_event_loop()
loop.run_until_complete(start_yukki())       

async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception as e:
        pass


@idk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@idg.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ydg.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@wdg.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@hdg.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@sdg.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@adg.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bdg.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@cdg.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@edg.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@hdg.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ddg.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@vgg.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ggg.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@lgg.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@mgg.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@kit.on(events.NewMessage(incoming=True, pattern=r"\.bio"))

async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗼\n\nCommand:\n\n.bio <Message to set Bio of Userbot accounts>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)     
        if len(e.text) > 5:
            bio = str(yukki[0])
            text = "KRR RHAA HU 😉"
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.account.UpdateProfileRequest(about=bio))
                await event.edit("HO GYA BHAI YARR🤑")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@sid.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@idg.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ydg.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@wdg.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@hdg.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@sdg.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@adg.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bdg.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@cdg.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@edg.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@hdg.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ddg.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@vgg.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ggg.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@lgg.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@mgg.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@kit.on(events.NewMessage(incoming=True, pattern=r"\.join"))

async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.join <Public Channel or Group Link/Username>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = yukki[0]
            text = "GHUSANE ME TIME LAGEGA SORRY GHUSNE ME..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("OH SED GHUSH GYA MAI TO 😬")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.pjoin")) 
@ake.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@idg.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ydg.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@wdg.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@hdg.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@sdg.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@adg.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bdg.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@cdg.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@edg.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@hdg.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ddg.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@vgg.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ggg.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@lgg.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@mgg.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@kit.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))



async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.pjoin <Private Channel or Group's access hash>\n\nExample :\nLink = https://t.me/joinchat/HGYs1wvsPUplMmM1\n\n.pjoin HGYs1wvsPUplMmM1"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = yukki[0]
            text = "GHUSH RHA WAIT"
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(ImportChatInviteRequest(bc))
                await event.edit("GHUSA DIYE YARR TUM ")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
        
@idk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@idg.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ydg.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@wdg.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@hdg.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@sdg.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@adg.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bdg.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@cdg.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@edg.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@hdg.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ddg.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@vgg.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ggg.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@lgg.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@mgg.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@kit.on(events.NewMessage(incoming=True, pattern=r"\.leave"))

async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗟𝗲𝗮𝘃𝗲\n\nCommand:\n\n.leave <Channel or Chat ID>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".leave(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) == 7:
            bc = yukki[0]
            bc = int(bc)
            text = "RDX BOT Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Succesfully Left")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
                
        
        
@idk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@idg.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ydg.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@wdg.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@hdg.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@sdg.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@adg.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@bdg.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@cdg.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@edg.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@hdg.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ddg.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@vgg.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ggg.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@lgg.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@mgg.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@kit.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗽𝗮𝗺\n\nCommand:\n\n.spam <count> <message to spam>\n\n.spam <count> <reply to a message>\n\nCount must be a integer."
    error = "Spam Module can only be used till 10000 count. For bigger spams use BigSpam."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            counter = int(yukki[0])
            if counter > 10000:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:  
            counter = int(yukki[0])
            if counter > 10000:
                return await e.reply(error, parse_mode=None, link_preview=None )
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukki[0])
            if counter > 10000:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            

@idk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@idg.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ydg.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@wdg.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@hdg.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@sdg.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@adg.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bdg.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@cdg.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@edg.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@hdg.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ddg.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@vgg.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ggg.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@lgg.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@mgg.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@kit.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))


async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺\n\nCommand:\n\n.delayspam <sleep time> <count> <message to spam>\n\n.delayspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        smex = await e.get_reply_message()
        yukki = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        yukkisexy = yukki[1:]
        if len(yukkisexy) == 2:
            message = str(yukkisexy[1])
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@idk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@idg.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ydg.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@wdg.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@hdg.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@sdg.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@adg.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bdg.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@cdg.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@edg.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@hdg.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ddg.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@vgg.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ggg.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@lgg.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@mgg.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@kit.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))

async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗴𝗦𝗽𝗮𝗺\n\nCommand:\n\n.bigspam <count> <message to spam>\n\n.bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            counter = int(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.1)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(0.1)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@idk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@idg.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ydg.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@wdg.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@hdg.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@sdg.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@adg.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bdg.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@cdg.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@edg.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@hdg.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ddg.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@vgg.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ggg.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@lgg.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@mgg.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@kit.on(events.NewMessage(incoming=True, pattern=r"\.raid"))

async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(yukki[0])
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(yukki[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )





@idk.on(events.NewMessage(incoming=True))
@ydk.on(events.NewMessage(incoming=True))
@wdk.on(events.NewMessage(incoming=True))
@hdk.on(events.NewMessage(incoming=True))
@sdk.on(events.NewMessage(incoming=True))
@adk.on(events.NewMessage(incoming=True))
@bdk.on(events.NewMessage(incoming=True))
@cdk.on(events.NewMessage(incoming=True))
@edk.on(events.NewMessage(incoming=True))
@ddk.on(events.NewMessage(incoming=True))
@vkk.on(events.NewMessage(incoming=True))
@kkk.on(events.NewMessage(incoming=True))
@lkk.on(events.NewMessage(incoming=True))
@mkk.on(events.NewMessage(incoming=True))
@sid.on(events.NewMessage(incoming=True))
@shy.on(events.NewMessage(incoming=True))
@aan.on(events.NewMessage(incoming=True))
@ake.on(events.NewMessage(incoming=True))
@eel.on(events.NewMessage(incoming=True))
@khu.on(events.NewMessage(incoming=True))
@shi.on(events.NewMessage(incoming=True))
@yaa.on(events.NewMessage(incoming=True))
@dav.on(events.NewMessage(incoming=True))
@raj.on(events.NewMessage(incoming=True))
@put.on(events.NewMessage(incoming=True))
@idg.on(events.NewMessage(incoming=True))
@ydg.on(events.NewMessage(incoming=True))
@wdg.on(events.NewMessage(incoming=True))
@hdg.on(events.NewMessage(incoming=True))
@sdg.on(events.NewMessage(incoming=True))
@adg.on(events.NewMessage(incoming=True))
@bdg.on(events.NewMessage(incoming=True))
@cdg.on(events.NewMessage(incoming=True))
@edg.on(events.NewMessage(incoming=True))
@ddg.on(events.NewMessage(incoming=True))
@vgg.on(events.NewMessage(incoming=True))
@ggg.on(events.NewMessage(incoming=True))
@lgg.on(events.NewMessage(incoming=True))
@mgg.on(events.NewMessage(incoming=True))
@kit.on(events.NewMessage(incoming=True))

async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.2)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(RRAID)),
            reply_to=event.message.id,
        )           
            
            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@idg.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ydg.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@wdg.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@hdg.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@sdg.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@adg.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bdg.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@cdg.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@edg.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@hdg.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ddg.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@vgg.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ggg.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@lgg.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@mgg.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@kit.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))


async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.replyraid <Username of User>\n\n.replyraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(yukki[0])
            a = await e.client.get_entity(message)
            g = a.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@idg.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ydg.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@wdg.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@hdg.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@sdg.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@adg.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bdg.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@cdg.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@edg.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@hdg.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ddg.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@vgg.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ggg.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@lgg.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@mgg.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@kit.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))

async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.dreplyraid <Username of User>\n\n.dreplyraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(yukki[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
    
       

@idk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@idg.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ydg.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@wdg.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@hdg.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@sdg.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@adg.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bdg.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@cdg.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@edg.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@hdg.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ddg.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@vgg.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ggg.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@lgg.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@mgg.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@kit.on(events.NewMessage(incoming=True, pattern=r"\.ping"))

async def ping(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "ruko ruko rdx hu phatunga to chodunga !"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"😬𝗟𝗜𝗡𝗚!\n`{ms}` 𝗺𝘀 [{ALIVE_NAME}](https://t.me/{USERNAME})")





@idk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@idg.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@ydg.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@wdg.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@hdg.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@sdg.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@adg.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@bdg.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@cdg.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@edg.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@hdg.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@ddg.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@vgg.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@ggg.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@lgg.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@mgg.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@kit.on(events.NewMessage(incoming=True, pattern=r"\.alive"))

       


async def alive(e):
    if e.sender_id in SMEX_USERS:
        text = "THODA RUKO YARR🤧"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        await event.edit(f"👑𝐌𝐀𝐒𝐓𝐄𝐑👑😈[{ALIVE_NAME}](https://t.me/{USERNAME})😈 ┣━━•➳➠  𝐉𝐎𝐈𝐍 𝐅𝐎𝐑 ➪ [𝐑𝐄𝐏𝐎](https://t.me/rdx_official_bot) ")


        
        

@idk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@idg.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ydg.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@wdg.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@hdg.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@sdg.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@adg.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bdg.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@cdg.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@edg.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@hdg.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ddg.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@vgg.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ggg.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@lgg.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@mgg.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@kit.on(events.NewMessage(incoming=True, pattern=r"\.restart"))

async def restart(e):
    if e.sender_id in SMEX_USERS:
        text = "𝙍𝙚𝙨𝙩𝙖𝙧𝙩𝙚𝙙\n\nPlease wait till it reboots..."
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await idk.disconnect()
        except Exception as e:
            pass
        try:
            await ydk.disconnect()
        except Exception as e:
            pass
        try:
            await wdk.disconnect()
        except Exception as e:
            pass
        try:
            await hdk.disconnect()
        except Exception as e:
            pass
        try:
            await sdk.disconnect()
        except Exception as e:
            pass
        try:
            await adk.disconnect()
        except Exception as e:
            pass
        try:
            await bdk.disconnect()
        except Exception as e:
            pass
        try:
            await cdk.disconnect()
        except Exception as e:
            pass
        try:
            await ddk.disconnect()
        except Exception as e:
            pass
        try:
            await edk.disconnect()
        except Exception as e:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

        
        
        
        
        
@idk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@idg.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ydg.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@wdg.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@hdg.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@sdg.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@adg.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bdg.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@cdg.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@edg.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@hdg.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ddg.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@vgg.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ggg.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@lgg.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@mgg.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@kit.on(events.NewMessage(incoming=True, pattern=r"\.help"))

async def help(e):
    if e.sender_id in SMEX_USERS:
       text = "𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀\n\n𝙐𝙩𝙞𝙡𝙨 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.ping\n.restart\n\n𝙐𝙨𝙚𝙧𝙗𝙤𝙩 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.bio\n.join\n.pjoin\n.leave\n\n𝙎𝙥𝙖𝙢 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.spam\n.delayspam\n.bigspam\n.raid\n.replyraid\n.dreplyraid\n\n\nFor more help regarding usage of plugins type plugins name"
       await e.reply(text, parse_mode=None, link_preview=None )

        

    
        
text = """

💥💥RDX SPAM BOT IS MODIFIED OF YUKKI 💥💥💥
💥💥💥💥💥💥 BY  SIDDHANT   OP 💥💥💥💥💥💥"""

print(text)
print("")
print("SMEX! RDX MULTI SPAM BOT STARTED SUCCESFULLY.")
if len(sys.argv) not in (1, 3, 4):
    try:
        idk.disconnect()
    except Exception as e:
        pass
    try:
        ydk.disconnect()
    except Exception as e:
        pass
    try:
        wdk.disconnect()
    except Exception as e:
        pass
    try:
        hdk.disconnect()
    except Exception as e:
        pass
    try:
        sdk.disconnect()
    except Exception as e:
        pass
    try:
        adk.disconnect()
    except Exception as e:
        pass
    try:
        bdk.disconnect()
    except Exception as e:
        pass
    try:
        cdk.disconnect()
    except Exception as e:
        pass
    try:
        edk.disconnect()
    except Exception as e:
        pass
    try:
        ddk.disconnect()
    except Exception as e:
        pass
    try:
        vkk.disconnect()
    except Exception as e:
        pass 
    try:
        kkk.disconnect()
    except Exception as e:
        pass
    try:
        lkk.disconnect()
    except Exception as e:
        pass 
    try:
        mkk.disconnect()
    except Exception as e:
        pass
    try:
        sid.disconnect()
    except Exception as e:
        pass
    try:
        shy.disconnect()
    except Exception as e:
        pass
    try:
        aan.disconnect()
    except Exception as e:
        pass
    try:
        ake.disconnect()
    except Exception as e:
        pass
    try:
        eel.disconnect()
    except Exception as e:
        pass
    try:
        khu.disconnect()
    except Exception as e:
        pass
    try:
        shi.disconnect()
    except Exception as e:
        pass
    try:
        yaa.disconnect()
    except Exception as e:
        pass
    try:
        dav.disconnect()
    except Exception as e:
        pass
    try:
        raj.disconnect()
    except Exception as e:
        pass
    try:
        put.disconnect()
    except Exception as e:
        pass
else:
    try:
        idk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ydk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        wdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        hdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        adk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        cdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        edk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ddk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        vkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        kkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        lkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        mkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sid.run_until_disconnected()
    except Exception as e:
        pass
    try:
        shy.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aan.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ake.run_until_disconnected()
    except Exception as e:
        pass
    try:
        eel.run_until_disconnected()
    except Exception as e:
        pass
    try:
        khu.run_until_disconnected()
    except Exception as e:
        pass
    try:
        shi.run_until_disconnected()
    except Exception as e:
        pass
    try:
        yaa.run_until_disconnected()
    except Exception as e:
        pass
    try:
        dav.run_until_disconnected()
    except Exception as e:
        pass
    try:
        raj.run_until_disconnected()
    except Exception as e:
        pass
    try:
        put.run_until_disconnected()
    except Exception as e:
        pass
    try:
        idg.disconnect()
    except Exception as e:
        pass
    try:
        ydg.disconnect()
    except Exception as e:
        pass
    try:
        wdg.disconnect()
    except Exception as e:
        pass
    try:
        hdg.disconnect()
    except Exception as e:
        pass
    try:
        sdg.disconnect()
    except Exception as e:
        pass
    try:
        adg.disconnect()
    except Exception as e:
        pass
    try:
        bdg.disconnect()
    except Exception as e:
        pass
    try:
        cdg.disconnect()
    except Exception as e:
        pass
    try:
        edg.disconnect()
    except Exception as e:
        pass
    try:
        ddg.disconnect()
    except Exception as e:
        pass
    try:
        vgg.disconnect()
    except Exception as e:
        pass 
    try:
        ggg.disconnect()
    except Exception as e:
        pass
    try:
        lgg.disconnect()
    except Exception as e:
        pass 
    try:
        mgg.disconnect()
    except Exception as e:
        pass
    try:
        kit.disconnect()
    except Exception as e:
        pass
