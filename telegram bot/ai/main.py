import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from openai import OpenAI


# =========================
# TOKEN
# =========================

TELEGRAM_TOKEN = "8955215038:AAFoCymEeDXjO0lR0byzuVhtVHDQxJj5hBY"

OPENAI_KEY = "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"


bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

client = OpenAI(
    api_key=OPENAI_KEY
)


# =========================
# START
# =========================

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Салом 🤖\n"
        "Ман AI бот ҳастам.\n"
        "Саволи худро нависед."
    )


# =========================
# HELP
# =========================

@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        "Ба ман ҳар савол фиристед.\n"
        "Ман ҷавоб медиҳам."
    )


# =========================
# AI ANSWER
# =========================

@dp.message()
async def chat_ai(message: Message):

    try:
        await message.answer("⏳ Ҷавоб тайёр шуда истодааст...")

        result = client.responses.create(
            model="gpt-4.1-mini",
            input=message.text
        )

        answer = result.output_text

        await message.answer(answer)

    except Exception as error:
        await message.answer(
            f"Хато шуд ❌\n{error}"
        )


# =========================
# RUN BOT
# =========================

async def main():
    print("AI Bot ишора шуд ✅")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())