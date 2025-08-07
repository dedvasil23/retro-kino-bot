import asyncio
import logging
import aiohttp
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, FSInputFile
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hbold
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

API_TOKEN = os.getenv("BOT_TOKEN")
KINOPOISK_API_KEY = os.getenv("KINOPOISK_API_KEY")

bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

SEARCH_URL = "https://api.kinopoisk.dev/v1.4/movie/search"

@dp.message(F.text == "/start")
async def cmd_start(message: Message):
    await message.answer(
        "🎞 <b>Добро пожаловать в Ретро-КиноБот!</b>

"
        "Напиши описание фильма, жанр или ключевые слова — и я найду для тебя подходящее кино 🎬"
    )

@dp.message()
async def search_movie(message: Message):
    query = message.text.strip()
    await message.answer("🔍 Ищу ленты по запросу: <b>{}</b>...".format(query))

    async with aiohttp.ClientSession() as session:
        headers = {"X-API-KEY": KINOPOISK_API_KEY}
        async with session.get(SEARCH_URL, params={"query": query}, headers=headers) as resp:
            data = await resp.json()

    films = data.get("docs", [])
    if not films:
        await message.answer("🥀 Увы, ничего не найдено. Попробуйте иначе сформулировать запрос.")
        return

    for film in films[:3]:
        name = film.get("name") or "Без названия"
        year = film.get("year", "—")
        genres = ", ".join([g["name"] for g in film.get("genres", [])]) or "Не указаны"
        description = film.get("description", "Нет описания")
        poster = film.get("poster", {}).get("previewUrl")
        kp_id = film.get("id")
        kp_link = f"https://www.kinopoisk.ru/film/{kp_id}/"

        text = f"<b>🎬 {name} ({year})</b>
"                f"<i>Жанр:</i> {genres}

"                f"{description}

"                f"<a href='{kp_link}'>🔗 Перейти на Кинопоиск</a>"

        if poster:
            await message.answer_photo(photo=poster, caption=text)
        else:
            await message.answer(text)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(dp.start_polling(bot))
