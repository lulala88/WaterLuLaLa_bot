import telepot 
from telegram.ext import Updater 
from telegram.ext import CommandHandler 
from telegram.ext import MessageHandler, Filters 
from emoji import emojize 
import schedule 
import time 
import logging 
import requests 
import json 
 
 
updater = Updater(token='793411044:AAGoUYvXBKapPWA8x6LWbqdY6FMu90PUswc') 
dispatcher = updater.dispatcher 


# 表情符號 
smile= emojize("😄", use_aliases=True) 

target = [] #用來放置訪問過這個bot的id 


 # 提醒多喝水
def remind(bot):
    ＃ 傳入陣列
    global target
    ＃ 定義陣列裡的參數
    for chat in target: 
        print(chat, target) ＃作為本機端確認是否有傳入
       ＃以下為每次提醒傳送的訊息
        bot.sendMessage(chat_id=chat, text=emojize("🔔", use_aliases=True)+'Time to Drink More Water ! !\n    WATERRRRRRRRR is so good'+emojize("💩", use_aliases=True)+emojize("👍", use_aliases=True)) 




＃ start指令 
def start(bot, update): 
    ＃傳入陣列放置拜訪過的user
    global target 
    ＃傳送有關bot的資訊與可愛圖片一張
    bot.send_message(chat_id=update.message.chat_id, text="I'm WaterLuLaLa"+ smile +",\n which is a bot that will remind you four time a day to drink more water\n /help - get some help \n /daily_demand - knowing your daily demand in water \n /weather - knowing weather \n") 
    bot.sendPhoto(chat_id=update.message.chat_id, photo='https://i.pinimg.com/originals/27/91/32/2791328773f5d889befdf67595f2c5e3.png') 
    ＃定義拜訪過的userid
    chat_id = update.message.chat_id
    ＃確認陣列中沒有重複存入這個 user後，將caht_id放入
    if chat_id not in targe
        print(chat_id)＃確認用
        target.append(chat_id)

＃新增這個指令
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

＃啟動指令
updater.start_polling()



＃help指令
def help(bot, update):
    ＃發送所有指令用以參考
    bot.send_message(chat_id=update.message.chat_id, text="There's some commands : \n /start - to begin with a cool picture\n /help - get some help\n /daily_demand - know how much water you need\n /weather - Puli's weather")


＃新增指令help
help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)
updater.start_polling()



text = 'Your water in need for a day is '

def echo(bot, update):
    a = int(update.message.text)
    b = a * 0.04
    bot.send_message(chat_id=update.message.chat_id, text=text+str(b)+"  liter")


def daily(bot,update):
    bot.send_message(chat_id=update.message.chat_id, text="Please input your weight ( just number ) ! \n Your are ??? kg ")
    echo_handler= MessageHandler(Filters.text, echo)
    dispatcher.add_handler(echo_handler)

daily_handler = CommandHandler('daily_demand',daily)
dispatcher.add_handler(daily_handler)

updater.start_polling()


def weather(bot,update):
    r = requests.get('https://works.ioa.tw/weather/api/weathers/171.json')
    data = json.loads(r.text)
    temperature = data['temperature']
    now = data['at']
    weather = data['desc']
    rainfall =data['rainfall']
    humidity = data['humidity']
    print(temperature,now,weather,rainfall,humidity)
    
    bot.send_message(chat_id=update.message.chat_id, text= "About Puli:\n"+emojize(':eyes:', use_aliases=True)+"    temperature  :  "+str(temperature) +"\n"+emojize(':flags:', use_aliases=True)+"    weather  :  "+ weather +"\n"+emojize(':droplet:', use_aliases=True)+"    rainfall  :  "+str(rainfall)+"\n"+emojize(':sweat_drops:', use_aliases=True)+"    humidity  :  "+ str(humidity)+"\n"+emojize(':alarm_clock:', use_aliases=True)+"    observation time  :  "+ now)

weather_handler = CommandHandler('weather',weather)
dispatcher.add_handler(weather_handler)

updater.start_polling()


bot1 = telepot.Bot('793411044:AAGoUYvXBKapPWA8x6LWbqdY6FMu90PUswc')
bot1.getMe()
schedule.every(1).minutes.do(remind,bot=bot1)


while True:
    schedule.run_pending()
    time.sleep(1)
                                                     
