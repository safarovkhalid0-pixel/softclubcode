# import asyncio
# from datetime import datetime

# from aiogram import Bot, Dispatcher
# from aiogram.filters import Command
# from aiogram.types import Message

# # ==========================
# # TOKEN
# # ==========================
# TOKEN = "8941231136:AAHWFGWT6REBkCRH4hyWbb75fp0uilDbyfw"

# bot = Bot(token=TOKEN)
# dp = Dispatcher()

# # ==========================
# # START
# # ==========================
# @dp.message(Command("start"))
# async def start(message: Message):
#     text = f"""
# 👋 Салом, {message.from_user.first_name}!

# Ман Telegram Bot ҳастам.

# Фармонҳои ман:

# /start - Оғози бот
# /help - Ёрдам
# /about - Дар бораи бот
# /id - ID-и шумо
# /time - Вақти ҳозира

# Ба ман паём фиристед, ман ҷавоб медиҳам.
# """
#     await message.answer(text)

# # ==========================
# # HELP
# # ==========================
# @dp.message(Command("help"))
# async def help_command(message: Message):
#     await message.answer(
#         """
# 📖 Ёрдам

# Фармонҳо:

# /start
# /help
# /about
# /id
# /time

# Ин бот метавонад паёмҳои шуморо такрор кунад.
# """
#     )

# # ==========================
# # ABOUT
# # ==========================
# @dp.message(Command("about"))
# async def about(message: Message):
#     await message.answer(
#         """
# ℹ️ Дар бораи бот

# Ном: My Telegram Bot
# Забон: Python
# Китобхона: aiogram 3.x

# Ин бот ҳамчун мисол сохта шудааст.
# """
#     )

# # ==========================
# # USER ID
# # ==========================
# @dp.message(Command("id"))
# async def my_id(message: Message):
#     await message.answer(
#         f"🆔 ID-и шумо:\n{message.from_user.id}"
#     )

# # ==========================
# # TIME
# # ==========================
# @dp.message(Command("time"))
# async def time(message: Message):
#     now = datetime.now()
#     await message.answer(
#         f"🕒 Вақт:\n{now.strftime('%H:%M:%S')}"
#     )

# # ==========================
# # PHOTO
# # ==========================
# @dp.message(lambda message: message.photo)
# async def photo(message: Message):
#     await message.answer("📷 Акси шумо қабул шуд.")

# # ==========================
# # STICKER
# # ==========================
# @dp.message(lambda message: message.sticker)
# async def sticker(message: Message):
#     await message.answer("😀 Стикер қабул шуд.")

# # ==========================
# # VOICE
# # ==========================
# @dp.message(lambda message: message.voice)
# async def voice(message: Message):
#     await message.answer("🎤 Паёми овозӣ қабул шуд.")

# # ==========================
# # DOCUMENT
# # ==========================
# @dp.message(lambda message: message.document)
# async def document(message: Message):
#     await message.answer("📄 Ҳуҷҷат қабул шуд.")

# # ==========================
# # TEXT
# # ==========================
# @dp.message()
# async def echo(message: Message):
#     text = message.text.lower()

#     if text == "салом":
#         await message.answer("👋 Салом! Хуш омадед.")
#     elif text == "ном":
#         await message.answer("🤖 Ман Telegram Bot ҳастам.")
#     elif text == "рахмат":
#         await message.answer("😊 Марҳамат!")
#     elif text == "bye":
#         await message.answer("👋 Хайр!")
#     else:
#         await message.answer(
#             f"Шумо навиштед:\n\n{message.text}"
#         )

# # ==========================
# # MAIN
# # ==========================
# async def main():
#     print("=" * 40)
#     print("Bot Started...")
#     print("=" * 40)

#     await dp.start_polling(bot)

# if __name__ == "__main__":
#     asyncio.run(main())