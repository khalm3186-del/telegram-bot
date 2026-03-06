from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import random
import datetime
import logging

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "7723426334:AAHWILUje9_oo5wSw5tz3gJ_5Ub-PVLV--M"

first_names = [
"Oleksandr","Andriy","Dmytro","Serhii","Maksym",
"Ivan","Taras","Yurii","Artem","Mykola"
]

middle_names = [
"Ivanovych","Petrovych","Serhiiovych",
"Oleksandrovych","Mykolaiovych"
]

last_names = [
"Shevchenko","Kovalenko","Melnyk","Tkachenko",
"Bondarenko","Tymoshenko","Boyko","Kravchenko",
"Polishchuk","Lysenko"
]

cities = [
"Kyiv","Kharkiv","Odessa","Dnipro","Lviv",
"Zaporizhzhia","Vinnytsia","Poltava"
]

districts = [
"Shevchenkivskyi District",
"Holosiivskyi District",
"Pecherskyi District",
"Sviatoshynskyi District"
]

streets = [
"Hrushevskoho Street",
"Shevchenko Street",
"Central Street",
"Freedom Street",
"Independence Street"
]


def generate_profile():

    first = random.choice(first_names)
    middle = random.choice(middle_names)
    last = random.choice(last_names)

    name = f"{first} {middle} {last}"

    gender = random.choice(["Male","Female"])

    year = random.randint(1965,2002)
    month = random.randint(1,12)
    day = random.randint(1,28)

    dob = datetime.date(year,month,day)
    age = datetime.date.today().year - year

    username = (first + last).lower() + str(random.randint(10,99))
    email = username + "@" + random.choice(["gmail.com","yahoo.com"])

    phone = "+380 " + str(random.randint(50,99)) + " " + str(random.randint(100,999)) + " " + str(random.randint(10,99)) + " " + str(random.randint(10,99))

    city = random.choice(cities)
    district = random.choice(districts)
    street = random.choice(streets)

    house = random.randint(1,200)
    apartment = random.randint(1,50)

    address = f"{street}, {house}/{apartment}, {district}, {city}"

    postal = random.randint(10000,99999)

    passport = "MC" + str(random.randint(10000000,99999999))
    additional = "PX" + str(random.randint(10000,99999))
    session = "SESS" + str(random.randint(100000000,999999999))

    now = datetime.datetime.now().strftime("%d-%b-%Y %H:%M")

    profile = f"""
🌸 Paypal Information 🌸

👤 Name: {name}
⚧ Gender: {gender}
🌍 Nationality: Ukrainian 🇺🇦
🎂 DOB: {dob} ({age} years)

📧 Email: {email} ✅
📞 Phone: {phone}

🏠 Address: {address}
📮 Postal Code: {postal}

🪪 Passport: {passport}

🔐 Additional Info: {additional}
🔑 Security Code: Session ID: {session}

📍 Location: {city}, Ukraine
👨‍💻 Dev: @FailedFr

Generated: {now}
"""

    return profile


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    profile = generate_profile()

    keyboard = [
        [InlineKeyboardButton("🔄 Generate Again", callback_data="gen")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        profile,
        reply_markup=reply_markup
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.data == "gen":

        profile = generate_profile()

        keyboard = [
            [InlineKeyboardButton("🔄 Generate Again", callback_data="gen")]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.message.reply_text(
            profile,
            reply_markup=reply_markup
        )


def main():

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("Bot Running...")

    app.run_polling()


if name == "main":
    main()
