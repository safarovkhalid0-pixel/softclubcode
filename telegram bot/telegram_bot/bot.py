import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import (
    Message,
    CallbackQuery,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


TOKEN = "8661194292:AAF1fJeM93u3Uds0qSPemfTyWq7bN8YWAsc"


bot = Bot(TOKEN)
dp = Dispatcher()


# ======================
# FOOD DATABASE
# ======================

foods = {
    "burger": {
        "name": "🍔 Burger",
        "price": "$8",
        "description": "Juicy beef burger with cheese and vegetables."
    },

    "pizza": {
        "name": "🍕 Pizza",
        "price": "$12",
        "description": "Hot pepperoni pizza with mozzarella."
    },

    "hotdog": {
        "name": "🌭 Hot Dog",
        "price": "$6",
        "description": "Classic hot dog with sauce."
    },

    "cola": {
        "name": "🥤 Cola",
        "price": "$2",
        "description": "Cold refreshing drink."
    }
}


# ======================
# FSM
# ======================

class OrderState(StatesGroup):
    name = State()
    address = State()
    phone = State()


# ======================
# KEYBOARDS
# ======================

def main_keyboard():

    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🍔 View Menu"),
                KeyboardButton(text="🛒 My Orders")
            ],
            [
                KeyboardButton(text="ℹ️ Help")
            ]
        ],
        resize_keyboard=True
    )


def menu_keyboard():

    buttons = []

    for key, item in foods.items():
        buttons.append(
            [
                InlineKeyboardButton(
                    text=item["name"],
                    callback_data=f"food_{key}"
                )
            ]
        )

    return InlineKeyboardMarkup(
        inline_keyboard=buttons
    )


def food_keyboard(food):

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🛒 Order",
                    callback_data=f"order_{food}"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔙 Back",
                    callback_data="back_menu"
                )
            ]
        ]
    )


def cancel_keyboard():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="❌ Cancel",
                    callback_data="cancel"
                )
            ]
        ]
    )


# ======================
# START
# ======================

@dp.message(Command("start"))
async def start(message: Message):

    await message.answer(
        "👋 Welcome to FastBite Restaurant Bot!\n\n"
        "Hungry? Please choose an option below:",
        reply_markup=main_keyboard()
    )


# ======================
# REPLY BUTTONS
# ======================

@dp.message(F.text == "🍔 View Menu")
async def view_menu(message: Message):

    await message.answer(
        "Choose your food:",
        reply_markup=menu_keyboard()
    )


@dp.message(F.text == "ℹ️ Help")
async def help_button(message: Message):

    await message.answer(
        "ℹ️ FastBite Restaurant Bot can:\n\n"
        "🍔 Show food menu\n"
        "🛒 Take food orders\n"
        "👤 Collect customer name\n"
        "📍 Collect delivery address\n"
        "📞 Collect phone number\n"
        "🛒 Show your orders"
    )


@dp.message(F.text == "🛒 My Orders")
async def my_orders(message: Message):

    try:

        with open(
            "orders.txt",
            "r",
            encoding="utf-8"
        ) as file:

            orders = file.read()


        if message.from_user.id.str() in orders:

            await message.answer(
                "🛒 Your orders:\n\n" + orders
            )

        else:

            await message.answer(
                "You don't have any orders yet."
            )

    except FileNotFoundError:
        await message.answer(
            "You don't have any orders yet."
        )


# ======================
# FOOD DETAILS
# ======================

@dp.callback_query(F.data.startswith("food_"))
async def food_info(callback: CallbackQuery):

    food_id = callback.data.replace(
        "food_",
        ""
    )

    food = foods[food_id]


    await callback.message.edit_text(
        f"<b>{food['name']}</b>\n\n"
        f"Price: {food['price']}\n\n"
        f"{food['description']}",
        reply_markup=food_keyboard(food_id),
        parse_mode="HTML"
    )


@dp.callback_query(F.data == "back_menu")
async def back_menu(callback: CallbackQuery):

    await callback.message.edit_text(
        "Choose your food:",
        reply_markup=menu_keyboard()
    )


# ======================
# ORDER PROCESS
# ======================

@dp.callback_query(F.data.startswith("order_"))
async def order_start(
        callback: CallbackQuery,
        state: FSMContext
):

    food = callback.data.replace(
        "order_",
        ""
    )


    await state.update_data(
        food=food
    )


    await callback.message.answer(
        "Enter your name:",
        reply_markup=cancel_keyboard()
    )


    await state.set_state(
        OrderState.name
    )


@dp.message(OrderState.name)
async def get_name(
        message: Message,
        state: FSMContext
):

    await state.update_data(
        name=message.text
    )


    await message.answer(
        "Enter your address:",
        reply_markup=cancel_keyboard()
    )


    await state.set_state(
        OrderState.address
    )



@dp.message(OrderState.address)
async def get_address(
        message: Message,
        state: FSMContext
):

    await state.update_data(
        address=message.text
    )


    await message.answer(
        "Enter your phone number:",
        reply_markup=cancel_keyboard()
    )


    await state.set_state(
        OrderState.phone
    )



@dp.message(OrderState.phone)
async def get_phone(
        message: Message,
        state: FSMContext
):

    data = await state.get_data()


    order_text = (
        f"User ID: {message.from_user.id}\n"
        f"Food: {foods[data['food']]['name']}\n"
        f"Name: {data['name']}\n"
        f"Address: {data['address']}\n"
        f"Phone: {message.text}\n"
        f"--------------------\n"
    )


    with open(
        "orders.txt",
        "a",
        encoding="utf-8"
    ) as file:

        file.write(order_text)



    await message.answer(
        "✅ Your order has been placed!\n\n"
        f"{order_text}",
        reply_markup=main_keyboard()
    )


    await state.clear()



# ======================
# CANCEL
# ======================

@dp.callback_query(F.data == "cancel")
async def cancel(
        callback: CallbackQuery,
        state: FSMContext
):

    await state.clear()


    await callback.message.answer(
        "❌ Order cancelled.",
        reply_markup=main_keyboard()
    )



# ======================
# RUN
# ======================

async def main():

    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())