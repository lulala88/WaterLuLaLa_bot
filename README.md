# 提醒每天喝水的Telegram_bot

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
- pipenv
- flask
- con
- beautifulsoup4
- requests
- json

## 參考資料
1. 將Telegram_bot設置在RaspberryPi
https://www.instructables.com/id/Set-up-Telegram-Bot-on-Raspberry-Pi/

2. 計算一天喝水量
https://www.morewater.com.tw/QA.aspx

3. python 參考
https://github.com/dbader/schedule

4. python crontab
https://github.com/dbader/schedule

5. 天氣資訊
https://works.ioa.tw/weather/api/doc/index.html
