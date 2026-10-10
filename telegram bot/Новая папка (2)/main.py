import telebot
from telebot import types
import sqlite3
from datetime import datetime

TOKEN = "8939423985:AAHkK7pKDw0mtH6hcgn6MxdlwGJbE1wR5us"
bot = telebot.TeleBot(TOKEN)


# ----------------- БАЗАИ МАЪЛУМОТ (DATABASE) -----------------
def init_db():
    conn = sqlite3.connect("hamsafar.db")
    cursor = conn.cursor()
    
    # Ҷадвали корбарон
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            full_name TEXT,
            phone TEXT,
            is_driver INTEGER DEFAULT 0,
            car_info TEXT
        )
    ''')
    
    # Ҷадвали эълонҳо
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rides (
            ride_id INTEGER PRIMARY KEY AUTOINCREMENT,
            driver_id INTEGER,
            route_from TEXT,
            route_to TEXT,
            departure_time TEXT,
            price REAL,
            seats_total INTEGER,
            seats_available INTEGER,
            status TEXT DEFAULT 'active'
        )
    ''')
    
    # Ҷадвали бронҳо
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
            ride_id INTEGER,
            client_id INTEGER,
            booking_time TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

init_db()

# ----------------- ЁРИДИҲАНДАҲО (HELPERS) -----------------
def get_user(user_id):
    conn = sqlite3.connect("hamsafar.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

# ----------------- КЛАВИАТУРАҲО (KEYBOARDS) -----------------
def main_menu_keyboard(user_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    user = get_user(user_id)
    
    markup.row("🚗 Дидани эълонҳо")
    
    if user and user[3] == 1: # Агар ронанда бошад
        markup.row("➕ Иловаи эълон", "📋 Эълонҳои ман")
        markup.row("👤 Профили ронанда (Навсозӣ)")
    else:
        markup.row("🚕 Ронанда шудан")
        
    markup.row("🗂 Бронҳои ман")
    return markup

# ----------------- ОҒОЗ /START -----------------
@bot.message_handler(commands=['start'])
def start_cmd(message):
    user = get_user(message.from_user.id)
    if not user:
        msg = bot.send_message(message.chat.id, "Хуш омадед ба боти Hamsafar!\nЛутфан барои сабти ном Ном ва Насаби худро ворид кунед:")
        bot.register_next_step_handler(msg, register_name)
    else:
        bot.send_message(message.chat.id, f"Хуш омадед, {user[1]}!", reply_markup=main_menu_keyboard(message.from_user.id))

def register_name(message):
    name = message.text.strip()
    if not name:
        msg = bot.send_message(message.chat.id, "Ном наметавонад холӣ бошад. Лутфан дуруст ворид кунед:")
        bot.register_next_step_handler(msg, register_name)
        return
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(types.KeyboardButton("📞 Фиристодани рақам", request_contact=True))
    msg = bot.send_message(message.chat.id, "Рақами телефони худро фиристед:", reply_markup=markup)
    bot.register_next_step_handler(msg, register_phone, name)

def register_phone(message, name):
    phone = ""
    if message.contact:
        phone = message.contact.phone_number
    else:
        phone = message.text.strip()
        
    conn = sqlite3.connect("hamsafar.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (user_id, full_name, phone) VALUES (?, ?, ?)", (message.from_user.id, name, phone))
    conn.commit()
    conn.close()
    
    bot.send_message(message.chat.id, "Регистратсия бо муваффақият анҷом ёфт!", reply_markup=main_menu_keyboard(message.from_user.id))

# ----------------- РОНАНДА ШУДАН ВА НАВСОЗӢ -----------------
@bot.message_handler(func=lambda m: m.text in ["🚕 Ронанда шудан", "👤 Профили ронанда (Навсозӣ)"])
def become_driver(message):
    msg = bot.send_message(message.chat.id, "Маълумоти мошини худро ворид кунед (масалан: Opel Astra, рақами 0101ТТ01):")
    bot.register_next_step_handler(msg, save_car_info)

def save_car_info(message):
    car_info = message.text.strip()
    conn = sqlite3.connect("hamsafar.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET is_driver = 1, car_info = ? WHERE user_id = ?", (car_info, message.from_user.id))
    conn.commit()
    conn.close()
    bot.send_message(message.chat.id, "Маълумоти ронандагии шумо сабт/навсозӣ шуд!", reply_markup=main_menu_keyboard(message.from_user.id))

# ----------------- ИЛОВАИ ЭЪЛОН (АГАР РОНАНДА БОШАД) -----------------
@bot.message_handler(func=lambda m: m.text == "➕ Иловаи эълон")
def add_ride(message):
    user = get_user(message.from_user.id)
    if not user or user[3] != 1:
        bot.send_message(message.chat.id, "Шумо ронанда нестед!")
        return
    msg = bot.send_message(message.chat.id, "Аз куҷо меравед? (Масалан: Душанбе)")
    bot.register_next_step_handler(msg, ride_from)

def ride_from(message):
    r_from = message.text.strip()
    msg = bot.send_message(message.chat.id, "Ба куҷо меравед? (Масалан: Хуҷанд)")
    bot.register_next_step_handler(msg, ride_to, r_from)

def ride_to(message, r_from):
    r_to = message.text.strip()
    msg = bot.send_message(message.chat.id, "Вақти рафтанро ворид кунед (Масалан: Пагоҳ соати 10:00):")
    bot.register_next_step_handler(msg, ride_time, r_from, r_to)

def ride_time(message, r_from, r_to):
    r_time = message.text.strip()
    msg = bot.send_message(message.chat.id, "Нархи як ҷой (бо сомонӣ, масалан: 100):")
    bot.register_next_step_handler(msg, ride_price, r_from, r_to, r_time)

def ride_price(message, r_from, r_to, r_time):
    try:
        price = float(message.text.strip())
    except ValueError:
        msg = bot.send_message(message.chat.id, "Нархро бо рақам ворид кунед:")
        bot.register_next_step_handler(msg, ride_price, r_from, r_to, r_time)
        return
    msg = bot.send_message(message.chat.id, "Шумораи ҷойҳои холӣ (Масалан: 4):")
    bot.register_next_step_handler(msg, ride_seats, r_from, r_to, r_time, price)

def ride_seats(message, r_from, r_to, r_time, price):
    try:
        seats = int(message.text.strip())
    except ValueError:
        msg = bot.send_message(message.chat.id, "Шумораи ҷойҳоро бо рақам ворид кунед:")
        bot.register_next_step_handler(msg, ride_seats, r_from, r_to, r_time, price)
        return
        
    conn = sqlite3.connect("hamsafar.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO rides (driver_id, route_from, route_to, departure_time, price, seats_total, seats_available)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (message.from_user.id, r_from, r_to, r_time, price, seats, seats))
    conn.commit()
    conn.close()
    
    bot.send_message(message.chat.id, "Эълони шумо бо муваффақият илова шуд!", reply_markup=main_menu_keyboard(message.from_user.id))

# ----------------- ДИДАНИ ЭЪЛОНҲО ВА БРОН КАРДАН -----------------
@bot.message_handler(func=lambda m: m.text == "🚗 Дидани эълонҳо")
def view_rides(message):
    conn = sqlite3.connect("hamsafar.db")
    cursor = conn.cursor()
    cursor.execute('''
        SELECT rides.*, users.full_name, users.phone, users.car_info 
        FROM rides 
        JOIN users ON rides.driver_id = users.user_id 
        WHERE rides.seats_available > 0 AND rides.status = 'active'
    ''')
    rides = cursor.fetchall()
    conn.close()
    
    if not rides:
        bot.send_message(message.chat.id, "Дар айни замон ҳеҷ эълоне мавҷуд нест.")
        return
        
    for r in rides:
        text = f"🚗 Ронанда: {r[9]}\n" \
               f"📞 Тел: {r[10]}\n" \
               f"🚘 Мошин: {r[11]}\n" \
               f"📍 Самт: Аз {r[2]} ба {r[3]}\n" \
               f"⏰ Вақт: {r[4]}\n" \
               f"💰 Нарх: {r[5]} сомонӣ\n" \
               f"💺 Ҷойҳои холӣ: {r[7]} аз {r[6]}"
               
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Брон кардан 📌", callback_data=f"book_{r[0]}"))
        bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("book_"))
def process_booking(call):
    ride_id = int(call.data.split("_")[1])
    client_id = call.from_user.id
    
    conn = sqlite3.connect("hamsafar.db")
    cursor = conn.cursor()
    
    # Санҷиши мавҷудияти ҷой
    cursor.execute("SELECT seats_available, driver_id FROM rides WHERE ride_id = ?", (ride_id,))
    ride = cursor.fetchone()
    
    if not ride:
        bot.answer_callback_query(call.id, "Эълон ёфт нашуд!")
        conn.close()
        return
        
    if ride[1] == client_id:
        bot.answer_callback_query(call.id, "Шумо эълони худро брон карда наметавонед!", show_alert=True)
        conn.close()
        return
        
    if ride[0] <= 0:
        bot.answer_callback_query(call.id, "Ҷойҳои холӣ тамом шудаанд!", show_alert=True)
        conn.close()
        return
        
    # Сабти брон
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO bookings (ride_id, client_id, booking_time) VALUES (?, ?, ?)", (ride_id, client_id, now_str))
    cursor.execute("UPDATE rides SET seats_available = seats_available - 1 WHERE ride_id = ?", (ride_id,))
    conn.commit()
    conn.close()
    
    bot.answer_callback_query(call.id, "Ҷой бо муваффақият брон карда шуд!", show_alert=True)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)

# ----------------- ЭЪЛОНҲОИ РОНАНДА (ИВАЗ ВА НЕСТ КАРДАН) -----------------
@bot.message_handler(func=lambda m: m.text == "📋 Эълонҳои ман")
def my_rides(message):
    conn = sqlite3.connect("hamsafar.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rides WHERE driver_id = ? AND status = 'active'", (message.from_user.id,))
    rides = cursor.fetchall()
    conn.close()
    
    if not rides:
        bot.send_message(message.chat.id, "Шумо ягон эълони фаъол надоред.")
        return
        
    for r in rides:
        text = f"📍 Аз {r[2]} ба {r[3]}\n⏰ Вақт: {r[4]}\n💰 Нарх: {r[5]} сомонӣ\n💺 Ҷойҳо: {r[7]}/{r[6]}"
        markup = types.InlineKeyboardMarkup()
        markup.add(
            types.InlineKeyboardButton("🔄 Иваз кардан", callback_data=f"edit_{r[0]}"),
            types.InlineKeyboardButton("❌ Нест кардан", callback_data=f"del_{r[0]}")
        )
        bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith(("del_", "edit_")))
def handle_driver_action(call):
    action, ride_id = call.data.split("_")
    ride_id = int(ride_id)
    
    if action == "del":
        conn = sqlite3.connect("hamsafar.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE rides SET status = 'deleted' WHERE ride_id = ?", (ride_id,))
        conn.commit()
        conn.close()
        bot.answer_callback_query(call.id, "Эълон нест карда шуд!")
        bot.delete_message(call.message.chat.id, call.message.message_id)
        
    elif action == "edit":
        msg = bot.send_message(call.message.chat.id, "Вақт ва маълумоти нави эълонро ворид кунед (Масалан: Пагоҳ соати 12:00, 4 ҷой, 90с):")
        bot.register_next_step_handler(msg, process_edit_ride, ride_id)

def process_edit_ride(message, ride_id):
    new_details = message.text.strip()
    conn = sqlite3.connect("hamsafar.db")
    cursor = conn.cursor()
    # Барои соддагӣ матни вақтро нав мекунем
    cursor.execute("UPDATE rides SET departure_time = ? WHERE ride_id = ?", (new_details, ride_id))
    conn.commit()
    conn.close()
    bot.send_message(message.chat.id, "Эълон нав карда шуд!", reply_markup=main_menu_keyboard(message.from_user.id))

# ----------------- БРОНҲОИ МУШТАРӢ ВА ДАСТ КАШИДАН -----------------
@bot.message_handler(func=lambda m: m.text == "🗂 Бронҳои ман")
def my_bookings(message):
    conn = sqlite3.connect("hamsafar.db")
    cursor = conn.cursor()
    cursor.execute('''
        SELECT bookings.booking_id, rides.route_from, rides.route_to, rides.departure_time, rides.price
        FROM bookings
        JOIN rides ON bookings.ride_id = rides.ride_id
        WHERE bookings.client_id = ?
        ORDER BY bookings.booking_id DESC
    ''', (message.from_user.id,))
    bookings = cursor.fetchall()
    conn.close()
    
    if not bookings:
        bot.send_message(message.chat.id, "Шумо ягон брон надоред.")
        return
        
    text = "📋 Рӯйхати бронҳои шумо:\n\n"
    for b in bookings:
        text += f"🆔 Брон №{b[0]}: Аз {b[1]} ба {b[2]} | Вақт: {b[3]} | Нарх: {b[4]}с\n"
        
    # Даст кашидан аз брони охирин
    latest_booking_id = bookings[0][0]
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("❌ Даст кашидан аз брони охирин", callback_data=f"cancel_{latest_booking_id}"))
    
    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("cancel_"))
def cancel_booking(call):
    booking_id = int(call.data.split("_")[1])
    
    conn = sqlite3.connect("hamsafar.db")
    cursor = conn.cursor()
    
    # Ёфтани ride_id барои баргардонидани ҷойи холӣ
    cursor.execute("SELECT ride_id FROM bookings WHERE booking_id = ?", (booking_id,))
    res = cursor.fetchone()
    
    if res:
        ride_id = res[0]
        cursor.execute("DELETE FROM bookings WHERE booking_id = ?", (booking_id,))
        cursor.execute("UPDATE rides SET seats_available = seats_available + 1 WHERE ride_id = ?", (ride_id,))
        conn.commit()
        bot.answer_callback_query(call.id, "Брон бекор карда шуд!", show_alert=True)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    else:
        bot.answer_callback_query(call.id, "Брон ёфт нашуд!")
        
    conn.close()

# Иҷрои бот
if __name__ == "__main__":
    print("Бот кор карда истодааст...")
    bot.infinity_polling()