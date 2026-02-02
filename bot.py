import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
from openai import OpenAI

TOKEN = os.getenv("TG_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_KEY")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

client = OpenAI(api_key=OPENAI_KEY)

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("🤖 Привет! Я ИИ-бот. Напиши мне любой вопрос.")

@dp.message()
async def chat(message: Message):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Ты дружелюбный ИИ-ассистент."},
                {"role": "user", "content": message.text}
            ]
        )
        await message.answer(response.choices[0].message.content)
    except Exception:
        await message.answer("Ошибка 😔 Попробуй позже.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
