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
 
smile= emojize(":smile:", use_aliases=True) 
 
target = [] 
 
 
def remind(bot): 
    global target 
    for chat in target: 
        print(chat, target) 
        bot.sendMessage(chat_id=chat, text=emojize(":bell:", use_aliases=True)+'Time to Drink More Water ! !\n    WATERRRRRRRRR is so good'+emojize(":poop:", use_aliases=True)+emojize(":+1:", use_aliases=True)) 
 

 
 
def start(bot, update): 
    global target 
    bot.send_message(chat_id=update.message.chat_id, text="I'm WaterLuLaLa"+ smile +",\n which is a bot that will remind you four time a day to drink more water\n /help - get some help \n /daily_demand - knowing your daily demand in water \n /weather - knowing weather \n") 
    bot.sendPhoto(chat_id=update.message.chat_id, photo='https://i.pinimg.com/originals/27/91/32/2791328773f5d889befdf67595f2c5e3.png') 
    chat_id = update.message.chat_id
    if chat_id not in target
        print(chat_id)
        target.append(chat_id)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()



def help(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="There's some commands : \n /start - to begin with a cool picture\n /help - get some help\n /daily_demand - know how much water you need\n /weather - Puli's weather")
    

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
                                                     
