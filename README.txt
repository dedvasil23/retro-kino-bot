🚀 Инструкция по запуску Ретро-КиноБота на Render.com

1. Зарегистрируйтесь или войдите на https://render.com
2. Нажмите "New +" → "Web Service"
3. Выберите "Deploy from Git" → подключите GitHub ИЛИ загрузите вручную архив и разархивируйте на GitHub
4. Укажите:

   - **Start Command:** python3 bot/main.py
   - **Environment:** Python 3
   - **Build Command:** pip install -r requirements.txt

5. В разделе Environment добавьте переменные:
   - BOT_TOKEN — ваш Telegram токен (пример: 8207345433:AA...)
   - KINOPOISK_API_KEY — ваш API-ключ (пример: ZYP13W3-RP...)

6. Нажмите Deploy — через 30–60 сек бот заработает!

💬 Чтобы протестировать — найдите своего бота в Telegram и напишите, например:
    фильм про побег из тюрьмы

🎬 Удачного проката!
