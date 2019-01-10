Lulala a LSA專題 :baby: 
===
## 時間

### 1/3前

- 確立目標
- 建立 new bot
- 確定 raspberrypi 的 telepot 連接完成
- 簡單的命令指令成功


### 1/4
- 完成對話互動

### 1/5
- 成功抓取user回傳資料 完成 /daily_demand
- 嘗試爬蟲 (失敗)

### 1/9
- 成功定時提醒
- 嘗試自動登入 （失敗）
- 完成 /ewather
---
## 動機發想
因為現代人太常喝飲料，以至於時常忘了喝水，然而喝水又很重要，因此我們決定做一個telegram bot 來提醒大家喝水

## 所需設備
- Raspberry pi 3 
- USB 轉 TTL 傳輸線 
- 電腦

## 接線方式
![](https://i.imgur.com/6adE2Ek.png)
---
## 建立Telegram_bot
### Step 1: Install Telegram on Phone
### Step 2: Text /newbot to BotFather
![](https://i.imgur.com/WY5dtmq.png)
![](https://i.imgur.com/yuculUx.png)
### Step 3: Use Telegram's Web Version
### Step 4: Install Telepot on Raspberry Pi
sudo apt-get install python-pip
sudo pip install telepot
![](https://i.imgur.com/yWMn5MG.png)

---

## 系統架構

- python3
- telegram
 
---

## 安裝套件
- Telegram_with_Pi
  - python-telegram-bot
  - telegram.ext
  - telepot
  - logging
- 時間 
  - schedule
  - time
- 天氣 
  - requests
  - json
- 表情
  - Emoji


## 指令介紹
### 1. start - to begin with a cool picture

![](https://i.imgur.com/qh5PocY.png)
### 2. help - get some help 

![](https://i.imgur.com/t9IvtWM.png)
### 3. daily_demand - know how much water you need

![](https://i.imgur.com/V8xOPai.png)

### 4. weather - Puli's weather

![](https://i.imgur.com/0jjMyFx.png)


## 未來藍圖

- 更改/etc/rc.local 讓程式一開機就執行
- 配合今天的溫濕度及氣溫 去增加或減少所需補充水量
- 利用telegram bot 記錄大家的上線時間  依照上線時間，去做對應規劃
- 可以自己建立 reminder 提醒每天計畫


## 參考資料
1. 將Telegram_bot設置在pi
https://www.instructables.com/id/Set-up-Telegram-Bot-on-Raspberry-Pi/

2. Telegram_bot 用法
https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-–-Your-first-Bot

3. 計算一天喝水量
https://www.morewater.com.tw/QA.aspx

4. python 用法參考  
https://github.com/dbader/schedule#h3

5. python crontab
https://github.com/dbader/schedule

6. 天氣資訊 
https://works.ioa.tw/weather/api/doc/index.html
https://github.com/comdan66/weather/blob/master/README.md

7. 表情 
https://github.com/python-telegram-bot/python-telegram-bot/wiki/Emoji
https://www.webfx.com/tools/emoji-cheat-sheet/

8. requests
https://blog.gtwang.org/programming/python-requests-module-tutorial/

## 工作分配

- 106213014 資管二  歐芷欣 

    - `/daily_demand` `/start` `/help`
    -  表情文字敘述
    -  定時提醒 
    -  製作ppt 

- 106213019 資管二  蘇美婷 

    -  建立 telegram bot
    - `/weather` 
    -  寫github
