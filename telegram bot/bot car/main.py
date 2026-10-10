import asyncio
import logging
from datetime import datetime

from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
)
from sqlalchemy import (
    BigInteger,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    create_engine,
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# 1. Танзимоти базаи маълумот (SQLite барои соддагӣ истифода шуд, метавонед ба PostgreSQL иваз кунед)
DATABASE_URL = "sqlite:///car_rental.db"
Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# 2. Моделҳои SQLAlchemy (Таблиcontentҳо)
class Cars(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    description = Column(Text)
    price_per_day = Column(Integer, nullable=False)
    emoji = Column(String)

    # Муносибат (Relationship) бо таблитсаи rentals
    rentals = relationship("Rentals", back_populates="car")


class Rentals(Base):
    __tablename__ = "rentals"

    id = Column(Integer, primary_key=True)
    tg_id = Column(BigInteger, nullable=False)
    car_id = Column(Integer, ForeignKey("cars.id"), nullable=False)
    full_name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    days = Column(Integer, nullable=False)
    rental_date = Column(DateTime, default=datetime.utcnow)

    # Муносибат (Relationship) бо таблитсаи cars
    car = relationship("Cars", back_populates="rentals")


# Бонус 1: Автоматикӣ пур кардани база, агар он холӣ бошад
def insert_cars():
    session = SessionLocal()
    if not session.query(Cars).first():
        cars_data = [
            Cars(brand="Porsche", model="911 GT3 RS", description="The ultimate track-focused sports car.", price_per_day=500, emoji="🏎️"),
            Cars(brand="Mercedes-Benz", model="G-Class", description="Luxury off-road SUV.", price_per_day=400, emoji="🚙"),
            Cars(brand="Tesla", model="Model S Plaid", description="Insanely fast electric sedan.", price_per_day=200, emoji="⚡"),
            Cars(brand="Lamborghini", model="Huracan Evo", description="V10 Italian masterpiece.", price_per_day=800, emoji="🐂"),
            Cars(brand="BMW", model="M5 Competition", description="The perfect daily driver super saloon.", price_per_day=300, emoji="🚓"),
        ]
        session.add_all(cars_data)
        session.commit()
    session.close()


# Создание таблиц
Base.metadata.create_all(engine)
insert_cars()

# 3. Танзимоти Aiogram
BOT_TOKEN = "8619389701:AAERpNzErMQx6m4sGvwcbkxh-9qzxu3HC9Q" 
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
router = Router()

# 4. Ҳолатҳои FSM (FSM States)
class RentState(StatesGroup):
    full_name = State()
    phone = State()
    days = State()


class UpdateState(StatesGroup):
    new_phone = State()


# 5. Клавиатураҳо (Keyboards)
def main_menu_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🚘 View Fleet"), KeyboardButton(text="📋 My Rentals")],
            [KeyboardButton(text="⚙️ Update Phone"), KeyboardButton(text="❌ Cancel")],
        ],
        resize_keyboard=True,
    )


# 6. Хендлерҳо (Handlers)

# /start Command
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "🏎️ Welcome to Apex Car Rentals!\n\nChoose an option below to get started:",
        reply_markup=main_menu_keyboard(),
    )


# 🚘 View Fleet (READ) + Бонус 2 (Double Booking Prevention)
@router.message(F.text == "🚘 View Fleet")
async def view_fleet(message: Message):
    session = SessionLocal()
    
    # Бонус 2: Ёфтани ID-и мошинҳое, ки ҳозир ба иҷора гирифта шудаанд
    active_rented_car_ids = [r.car_id for r in session.query(Rentals.car_id).all()]
    
    # Филтр кардани мошинҳое, ки холӣ ҳастанд
    available_cars = session.query(Cars).filter(~Cars.id.in_(active_rented_car_ids)).all()
    session.close()

    if not available_cars:
        await message.answer("😔 Набахшед, дар айни замон ҳамаи мошинҳо ба иҷора гирифта шудаанд.")
        return

    keyboard = []
    for car in available_cars:
        keyboard.append([InlineKeyboardButton(
            text=f"{car.emoji} {car.brand} {car.model} (${car.price_per_day}/day)",
            callback_data=f"car_{car.id}"
        )])
    
    reply_markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    await message.answer("Интихоб кунед:", reply_markup=reply_markup)


# Интихоби мошин аз рўи Inline Button
@router.callback_query(F.data.startswith("car_"))
async def car_details(callback: CallbackQuery):
    car_id = int(callback.data.split("_")[1])
    session = SessionLocal()
    car = session.query(Cars).filter(Cars.id == car_id).first()
    session.close()

    if car:
        text = (
            f"{car.emoji} {car.brand} {car.model}\n\n"
            f"📝 Description: {car.description}\n"
            f"💰 Daily Rate: ${car.price_per_day}/day\n\n"
            f"Would you like to rent this car?"
        )
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🔑 Rent Now", callback_data=f"rent_{car.id}")]
        ])
        await callback.message.answer(text, reply_markup=keyboard)
    await callback.answer()


# 🔑 Оғози раванди иҷора (FSM)
@router.callback_query(F.data.startswith("rent_"))
async def start_rent(callback: CallbackQuery, state: FSMContext):
    car_id = int(callback.data.split("_")[1])
    await state.update_data(car_id=car_id)
    await state.set_state(RentState.full_name)
    await callback.message.answer("👤 Please enter your full name (Driver's License name):")
    await callback.answer()


# STEP 1: Гирифтани Ному Насаб
@router.message(RentState.full_name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    await state.set_state(RentState.phone)
    await message.answer("📱 Please enter your contact phone number:")


# STEP 2: Гирифтани Рақами ТЕЛЕФОН
@router.message(RentState.phone)
async def process_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await state.set_state(RentState.days)
    await message.answer("📆 How many days do you want to rent this car? (Enter a number):")


# STEP 3: Гирифтани рўзҳо ва Валидатсия + INSERT ба DB
@router.message(RentState.days)
async def process_days(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("❌ Error! Please enter a valid number of days:")
        return

    days = int(message.text)
    data = await state.get_data()
    car_id = data["car_id"]

    session = SessionLocal()
    car = session.query(Cars).filter(Cars.id == car_id).first()

    if not car:
        await message.answer("Хатогӣ: Мошин ёфт нашуд.")
        await state.clear()
        session.close()
        return

    total_price = car.price_per_day * days

    # Илова кардани Rental-и нав ба DB (CREATE)
    new_rental = Rentals(
        tg_id=message.from_user.id,
        car_id=car_id,
        full_name=data["full_name"],
        phone_number=data["phone"],
        days=days
    )
    session.add(new_rental)
    session.commit()
    session.close()

    # Паёми муваффақият
    success_text = (
        f"✅ Rental confirmed successfully!\n\n"
        f"{car.emoji} Car: {car.brand} {car.model}\n"
        f"👤 Name: {data['full_name']}\n"
        f"📆 Duration: {days} days\n"
        f"💵 Total Price: ${total_price}\n\n"
        f"Our agent will call you at {data['phone']} shortly."
    )
    await message.answer(success_text, reply_markup=main_menu_keyboard())
    await state.clear()


# 📋 My Rentals (READ)
@router.message(F.text == "📋 My Rentals")
async def my_rentals(message: Message):
    session = SessionLocal()
    # Гирифтани иҷораҳо бо истифода аз relationship барои хондани маълумоти мошин
    rentals = session.query(Rentals).filter(Rentals.tg_id == message.from_user.id).all()

    if not rentals:
        await message.answer("🤷‍♂️ Шумо ягон иҷораи фаъол надоред.")
        session.close()
        return

    for rental in rentals:
        car = rental.car
        total_price = car.price_per_day * rental.days
        text = (
            f"📋 Rental ID: #{rental.id}\n"
            f"{car.emoji} Car: {car.brand} {car.model}\n"
            f"📆 Duration: {rental.days} days\n"
            f"💵 Total: ${total_price}"
        )
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🗑️ Cancel Rental", callback_data=f"cancel_{rental.id}")]
        ])
        await message.answer(text, reply_markup=keyboard)
    session.close()


# ⚙️ Update Phone (UPDATE)
@router.message(F.text == "⚙️ Update Phone")
async def start_update_phone(message: Message, state: FSMContext):
    await state.set_state(UpdateState.new_phone)
    await message.answer("📱 Please enter your new contact number:")


@router.message(UpdateState.new_phone)
async def process_update_phone(message: Message, state: FSMContext):
    new_phone = message.text
    session = SessionLocal()
    
    # Ёфтан ва навсозии рақам барои ҳамаи иҷораҳои ин корбар
    rentals = session.query(Rentals).filter(Rentals.tg_id == message.from_user.id).all()
    
    if not rentals:
        await message.answer("❌ Шумо ягон иҷораи фаъол надоред, ки рақамашро тағйир диҳед.")
        await state.clear()
        session.close()
        return

    for rental in rentals:
        rental.phone_number = new_phone

    session.commit()
    session.close()

    await message.answer("✅ Contact number updated for all active rentals.", reply_markup=main_menu_keyboard())
    await state.clear()


# 🗑️ Cancel Rental (DELETE)
@router.callback_query(F.data.startswith("cancel_"))
async def cancel_rental(callback: CallbackQuery):
    rental_id = int(callback.data.split("_")[1])
    session = SessionLocal()
    
    rental = session.query(Rentals).filter(Rentals.id == rental_id).first()
    if rental:
        session.delete(rental)
        session.commit()
        await callback.message.answer("✅ Your car rental has been canceled.")
        await callback.message.delete()
    else:
        await callback.answer("❌ Иҷора ёфт нашуд ё аллакай нест карда шудааст.")
    
    session.close()
    await callback.answer()


# ❌ Cancel тугмачаи менюи асосӣ барои қатъ кардани FSM
@router.message(F.text == "❌ Cancel")
async def cancel_action(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Дархост бекор карда шуд.", reply_markup=main_menu_keyboard())


# 🚀 Оғози бот
async def main():
    logging.basicConfig(level=logging.INFO)
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())