# 提醒每天喝水的Telegram_bot

## 指令介紹
start - to begin with a cool picture
help - get some help 
daily_demand - know how much water you need 
weather - Puli's weather

## 動機發想
因為現代人太常喝飲料，以至於時常忘了喝水，然而喝水又很重要，因此我們決定做一個telegram bot 來提醒大家喝水

## 概念
1. User : 輸入身高體重  
   Telegrambot:回傳一天所需喝水量
   
2. 設置三個時間定時提醒喝水

3. User:輸入/weather指令
   Telegram bot:回傳溫度 並提醒是否增加/減少喝水量
   
## 安裝套件
- python-telegram-bot
- telegram.ext                                                              
- telepot
- flask
- con
- beautifulsoup4
- requests
- json
- Emoji   
- schedule    
- time                                                                             
-logging                                                                             

## 參考資料
1.將Telegram_bot設置在 
https://www.instructables.com/id/Set-up-Telegram-Bot-on-Raspberry-Pi/
2.Telegram_bot 
https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-–-Your-first-Bot
2.計算一天喝水量  
https://www.morewater.com.tw/QA.aspx
3.python 參考  
https://github.com/dbader/schedule#h3
4. python crontab 
https://github.com/dbader/schedule
5.天氣資訊 
https://works.ioa.tw/weather/api/doc/index.html
https://github.com/comdan66/weather/blob/master/README.md
6.表情 
https://github.com/python-telegram-bot/python-telegram-bot/wiki/Emoji
https://www.webfx.com/tools/emoji-cheat-sheet/
7.requests 
https://blog.gtwang.org/programming/python-requests-module-tutorial/

## 工作分配
106213014 資管二  歐芷欣 /daily_demand & 定時提醒  
106213019 資管二  蘇美婷 /weather
