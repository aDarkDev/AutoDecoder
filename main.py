# Auto Decoder RoBot
# By Confused Character
# github https://github.com/ConfusedCharacter/
#
# pip3 install telethon

import base64
from telethon import TelegramClient,events
import os

api_hash = "123"
api_id = 123
bot_token = ""

client = TelegramClient("Auto Decoder",api_id,api_hash).start(bot_token=bot_token)

print("runned")

class decode_it:
    def __init__(self) -> None:
        pass

    def hex(self,text):
        try:
            a_string = bytes.fromhex(text)
            a_string = a_string.decode("ascii")
            return a_string
        except:
            return False
    
    def base64(self,text):
        try:
            a = base64.b64decode(text.encode('utf-8')).decode('utf-8')
            print(a,'adsasd')
            return a
        except:
            return False

    def binary(self,string):
        try:
            string = string.replace(" ","").replace(",","").replace("\n","")
            lists = []
            for x in range(round(len(string)/8)):
                lists.append(string[:8])
                string = string[8:]
            
            lists = list(map( lambda x : chr(int(x,2)) , lists ))
            a = "".join(lists)
            return a
        except:
            return False

    def base32(self,text):
        try:
            a = base64.b32decode(text.encode('utf-8')).decode('utf-8')
            return a
        except:
            return False
    
    def base16(self,text):
        try:
            a = base64.b16decode(text.encode('utf-8')).decode('utf-8')
            return a
        except:
            return False
        
    def base85(self,text):
        try:
            a = base64.b85decode(text.encode('utf-8')).decode('utf-8')
            return a
        except:
            return False
    
    def utf(self,text):
        last = ""
        data = ['ASMO-708', 'big5', 'cp1025', 'cp866', 'cp875', 'csISO2022JP', 'DOS-720', 'DOS-862', 'EUC-CN', 'EUC-JP', 'euc-jp', 'euc-kr', 'GB18030', 'gb2312', 'hz-gb-2312', 'IBM00858', 'IBM00924', 'IBM01047', 'IBM01140', 'IBM01141', 'IBM01142', 'IBM01143', 'IBM01144', 'IBM01145', 'IBM01146', 'IBM01147', 'IBM01148', 'IBM01149', 'IBM037', 'IBM1026', 'IBM273', 'IBM277', 'IBM278', 'IBM280', 'IBM284', 'IBM285', 'IBM290', 'IBM297', 'IBM420', 'IBM423', 'IBM424', 'IBM437', 'IBM500', 'ibm737', 'ibm775', 'ibm850', 'ibm852', 'IBM855', 'ibm857', 'IBM860', 'ibm861', 'IBM863', 'IBM864', 'IBM865', 'ibm869', 'IBM870', 'IBM871', 'IBM880', 'IBM905', 'IBM-Thai', 'iso-2022-jp', 'iso-2022-jp', 'iso-2022-kr', 'iso-8859-1', 'iso-8859-13', 'iso-8859-15', 'iso-8859-2', 'iso-8859-3', 'iso-8859-4', 'iso-8859-5', 'iso-8859-6', 'iso-8859-7', 'iso-8859-8', 'iso-8859-8-i', 'iso-8859-9', 'Johab', 'koi8-r', 'koi8-u', 'ks_c_5601-1987', 'macintosh', 'shift_jis', 'us-ascii', 'utf-16', 'utf-16BE', 'utf-32', 'utf-32BE', 'utf-7', 'utf-8', 'windows-1250', 'windows-1251', 'Windows-1252', 'windows-1253', 'windows-1254', 'windows-1255', 'windows-1256', 'windows-1257', 'windows-1258', 'windows-874', 'x-Chinese-CNS', 'x-Chinese-Eten', 'x-cp20001', 'x-cp20003', 'x-cp20004', 'x-cp20005', 'x-cp20261', 'x-cp20269', 'x-cp20936', 'x-cp20949', 'x-cp50227', 'x-EBCDIC-KoreanExtended', 'x-Europa', 'x-IA5', 'x-IA5-German', 'x-IA5-Norwegian', 'x-IA5-Swedish', 'x-iscii-as', 'x-iscii-be', 'x-iscii-de', 'x-iscii-gu', 'x-iscii-ka', 'x-iscii-ma', 'x-iscii-or', 'x-iscii-pa', 'x-iscii-ta', 'x-iscii-te', 'x-mac-arabic', 'x-mac-ce', 'x-mac-chinesesimp', 'x-mac-chinesetrad', 'x-mac-croatian', 'x-mac-cyrillic', 'x-mac-greek', 'x-mac-hebrew', 'x-mac-icelandic', 'x-mac-japanese', 'x-mac-korean', 'x-mac-romanian', 'x-mac-thai', 'x-mac-turkish', 'x-mac-ukrainian']
        for i in data:
            try:
                decoded = text.encode(i.replace("windows-","cp")).decode("utf-8")
                last += "-"*10+"\nType: "+i+"\nResult: "+decoded+"\n"+"-"*10
            except:
                pass
        
        return last

async def event_new(event,data):
    try:
        await event.reply(data)
    except:
        open("decode-result.txt",'w',encoding="utf-8").write(data)
        await event.reply(file="decode-result.txt")
        os.remove("decode-result.txt")

@client.on(events.NewMessage(pattern=("/start")))
async def dss(event):
    await event.respond("Welcome To Auto Decoder Bot.\nSend Your Text.")

@client.on(events.NewMessage())
async def dss(event):
    text = event.text
    decode = decode_it()

    if event.text == "/start":
        pass
    elif "/utf" in event.text:
        await event_new(event,decode.utf(text.split("/utf ")[1]))
    else:
        if data_d := decode.base32(text):
            await event_new(event,f"Type: Base32\nResult: {data_d}")
        elif data_d := decode.base64(text):
            await event_new(event,f"Type: Base64\nResult: {data_d}")
        elif data_d := decode.base85(text):
            await event_new(event,f"Type: Base85\nResult: {data_d}")
        elif data_d := decode.binary(text):
            await event_new(event,f"Type: Binary\nResult: {data_d}")
        elif data_d := decode.hex(text):
            await event_new(event,f"Type: Hex\nResult: {data_d}")
        else:
            await event.respond("Sorry Not found.\nBy @ConfusedCharacter , [github](https://github.com/ConfusedCharacter) , [WebSite](https://ConfusedCharacter.com)",link_preview = False)

client.run_until_disconnected()



#█▀▀ █▀█ █▄░█ █▀▀ █░█ █▀ █▀▀ █▀▄   █▀▀ █░█ ▄▀█ █▀█ ▄▀█ █▀▀ ▀█▀ █▀▀ █▀█
#█▄▄ █▄█ █░▀█ █▀░ █▄█ ▄█ ██▄ █▄▀   █▄▄ █▀█ █▀█ █▀▄ █▀█ █▄▄ ░█░ ██▄ █▀▄
