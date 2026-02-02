import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
from openai import OpenAI

TOKEN = "8598444224:AAHebFjrei0yWCuoQr7llsllV7YGCuBJeGA"
OPENAI_KEY = "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"
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
