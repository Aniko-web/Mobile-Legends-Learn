from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

button1 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Geroylarni o'rganamiz"), KeyboardButton(text="Liniyalarni o'rganamiz")],
        [KeyboardButton(text="Qayerdan donat qilaman?"), KeyboardButton(text="Yangilanishlar")],
    ],
    resize_keyboard=True
)

Geroyliniya = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Exp liniya"), KeyboardButton(text="Mid liniya")],
        [KeyboardButton(text="Gold liniya"), KeyboardButton(text="Roum liniya")],
        [KeyboardButton(text="Jungler liniya"), KeyboardButton(text="Orqaga🔙")]
    ],
    resize_keyboard=True
)
Exp1= ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Aldous"),KeyboardButton(text="Alucard")],
        [KeyboardButton(text="Arlott"),KeyboardButton(text="Balmond")],
        [KeyboardButton(text="Badang"),KeyboardButton(text="Bane")],
        [KeyboardButton(text="Cici"),KeyboardButton(text="Dyrroth")],
        [KeyboardButton(text="Freya"),KeyboardButton(text="Guinevere")],
        [KeyboardButton(text="Bosh menuga qaytish🔙"),KeyboardButton(text="Keyingi1➡")]
    ]
)
Exp2= ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Hilda"),KeyboardButton(text="Jawhead")],
        [KeyboardButton(text="Julian"),KeyboardButton(text="Lapu-Lapu")],
        [KeyboardButton(text="Leomord"),KeyboardButton(text="Masha")],
        [KeyboardButton(text="Martis"),KeyboardButton(text="Paquito")],
        [KeyboardButton(text="Phoveus"),KeyboardButton(text="Ruby")],
        [KeyboardButton(text="Orqaga qaytish1⬅"),KeyboardButton(text="Keyingi2➡")]
    ]
)
Exp3= ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Silvanna"),KeyboardButton(text="Sun")],
        [KeyboardButton(text="Terizla"),KeyboardButton(text="Thamuz")],
        [KeyboardButton(text="X.Borg"),KeyboardButton(text="Yu Zhong")],
        [KeyboardButton(text="Yin"),KeyboardButton(text="Zilong")],
        [KeyboardButton(text="Edith"),KeyboardButton(text="Gatotkaca")],
        [KeyboardButton(text="Orqaga qaytish2⬅"),KeyboardButton(text="Keyingi3➡")]
    ]
)
Exp4= ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Esmeralda"),KeyboardButton(text="Uranus")],
        [KeyboardButton(text="Barats"),KeyboardButton(text="Fredrinn")],
        [KeyboardButton(text="Grock"),KeyboardButton(text="Khaleed")],
        [KeyboardButton(text="Alice"),KeyboardButton(text="Gloo")],
        [KeyboardButton(text="Orqaga qaytish3⬅"), KeyboardButton(text="Bosh menuga qaytish🔙")]
    ]
)
Cici= ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Passive(Cici)"),KeyboardButton(text="1-skill(Cici)")],
        [KeyboardButton(text="2-skill(Cici)"),KeyboardButton(text="3-skill(Cici)")],
        [KeyboardButton(text="Ortga⬅")],
    ]
)
YuZhong= ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Passive(Yu Zhong)"),KeyboardButton(text="1-skill(Yu Zhong)")],
        [KeyboardButton(text="2-skill(Yu Zhong)"),KeyboardButton(text="3-skill(Yu Zhong)")],
        [KeyboardButton(text="4-skill(Yu Zhong)"),KeyboardButton(text="Ortga⬅")]
    ]
)
donate_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text="💸 Donat qilish botga o‘tish",
                url="https://t.me/uzpinbot"
            )]
        ]
    )