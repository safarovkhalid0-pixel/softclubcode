# # 1
# import asyncio
# from aiogram import Bot, Dispatcher, types
# from aiogram.filters import Command

# TOCEN = "8941231136:AAHWFGWT6REBkCRH4hyWbb75fp0uilDbyfw"
# bot = Bot(token=TOCEN)
# dp = Dispatcher()

# @dp.message()
# async def first_handler(message: types.Message):
#     await message.answer("salom")

# # @dp.message(Command("start"))
# # async def start_handler(message: types.Message):
# #     await message.answer("")

# @dp.message()
# async def main():
#     await dp.start_polling(bot)

# if __name__ == "__main__":
#     asyncio.run(main())



# # 2
# import asyncio
# from aiogram import Bot, Dispatcher, types
# from aiogram.filters import Command
# from aiogram import F  
# import translators as ts

# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  #

# TOKEN = "8742853542:AAHpP41_UrCr3pnK9qjdmEdZlq05hYsX7Ww"

# bot = Bot(token=TOKEN)
# dp = Dispatcher()


# btn_en = KeyboardButton(text="🇺🇸 Английский")
# btn_ru = KeyboardButton(text="🇷🇺 Русский")


# lang_keyboard = ReplyKeyboardMarkup(
#     keyboard=[[btn_en, btn_ru]],  
#     resize_keyboard=True,         
#     one_time_keyboard=False       
# )


# @dp.message(Command("start"))
# async def cmd_start(message: types.Message):
    
#     await message.answer(
#         "Привет! 🌍 Я твой робот-переводчик.\n"
#         "Выбери на кнопках ниже, какой язык ты хочешь протестировать:",
#         reply_markup=lang_keyboard  
#     )



# @dp.message(F.text == "🇺🇸 Английский")  
# async def press_en(message: types.Message):
#     await message.answer("Отлично! Напиши мне фразу на английском (например: 'Hello, how are you?'), и я переведу её.")

# @dp.message(F.text == "🇷🇺 Русский")  
# async def press_ru(message: types.Message):
#     await message.answer("Супер! Напиши мне что-то на русском, но помни: мой главный режим пока настроен на перевод с английского! 😉")


# @dp.message()
# async def translate_handler(message: types.Message):
#     waiting_message = await message.answer("Перевожу... 🔄")
#     try:
#         translated_text = ts.translate_text(
#             query_text=message.text, 
#             from_language='en', 
#             to_language='ru'
#         )
#         await waiting_message.edit_text(f"Перевод: 👇\n\n{translated_text}")
#     except Exception:
#         await waiting_message.edit_text("Ой, что-то пошло не так. Попробуй еще раз!")


# async def main():
#     print("Бот с кнопками успешно запущен!")
#     await dp.start_polling(bot)

# if __name__ == "__main__":
#     asyncio.run(main())


# # 3
# import asyncio
# from aiogram import Bot, Dispatcher, types
# from aiogram.filters import Command

# TOKEN = "8742853542:AAHpP41_UrCr3pnK9qjdmEdZlq05hYsX7Ww"

# bot = Bot(token=TOKEN)
# dp = Dispatcher()


# @dp.message(Command("start"))
# async def cmd_start(message: types.Message):
#     await message.answer("Привет! Я твой первый робот-бот! Отправь мне любое сообщение, и я повторю его.")


# @dp.message()
# async def echo_message(message: types.Message):
#     await message.answer(f"Ты сказал: {message.text}")





# async def main():
#     print("Робот запущен и слушает команды...")
#     await dp.start_polling(bot)

# if __name__ == "__main__":
#     asyncio.run(main())
