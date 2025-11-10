import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8267691318:AAE7CE88EcEWAjnU4PrpHgycPj9aRivgEQI"

dp = Dispatcher()

# /start buyrug‘i
@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"Salom yangi o‘yinchi, {message.from_user.full_name}!\n"
        "MLBB (Mobile Legends: Bang Bang) o‘yinini o‘rganishga tayyormisan?",
        reply_markup=button1
    )

# Tugma: Geroylarni o‘rganamiz
@dp.message(F.text == "Geroylarni o'rganamiz")
async def button_handler1(msg: Message):
    await msg.answer("Qaysi liniyani geroyi kerak?", reply_markup=Geroyliniya)

# Tugma: Liniyalarni o‘rganamiz
@dp.message(F.text == "Liniyalarni o'rganamiz")
async def button_handler2(msg: Message):

    await msg.answer("Qaysi liniyani o‘rganmoqchisan?")

# Tugma: Qayerdan donat qilaman?
@dp.message(F.text == "Qayerdan donat qilaman?")
async def button_handler3(msg: Message):
    await msg.answer("💰 Donat qilish uchun quyidagi tugmani bosing:", reply_markup=donate_button)

# Tugma: Yangilanishlar
@dp.message(F.text == "Yangilanishlar")
async def button_handler4(msg: Message):
    await msg.answer("Hozircha yangilanishlar yo‘q 😉")



@dp.message(F.text == "Mid liniya")
async def button_handler6(msg: Message):
    await msg.answer("Qaysi geroy:")

@dp.message(F.text == "Gold liniya")
async def button_handler7(msg: Message):
    await msg.answer("Qaysi geroy:")

@dp.message(F.text == "Roum liniya")
async def button_handler8(msg: Message):
    await msg.answer("Qaysi geroy:")

@dp.message(F.text == "Jungler liniya")
async def button_handler9(msg: Message):
    await msg.answer("Qaysi geroy:")



@dp.message(F.text == "Exp liniya")
async def button_handler5(msg: Message):
    await msg.answer("Qaysi geroy:",reply_markup=Exp1)


@dp.message(F.text == "Orqaga🔙")
async def button_handler10(msg: Message):
    await msg.answer("Bosh meinu:",reply_markup=button1)

@dp.message(F.text == "Bosh menuga qaytish🔙")
async def button_handler11(msg: Message):
    await msg.answer("Bosh meinu:",reply_markup=button1)

@dp.message(F.text == "Keyingi1➡")
async def button_handler12(msg: Message):
    await msg.answer("Qaysi qahramon:",reply_markup=Exp2)

@dp.message(F.text == "Orqaga qaytish1⬅")
async def button_handler5(msg: Message):
    await msg.answer("Qaysi geroy:",reply_markup=Exp1)

@dp.message(F.text == "Keyingi2➡")
async def button_handler12(msg: Message):
    await msg.answer("Qaysi qahramon:",reply_markup=Exp3)

@dp.message(F.text == "Orqaga qaytish2⬅")
async def button_handler5(msg: Message):
    await msg.answer("Qaysi geroy:",reply_markup=Exp2)

@dp.message(F.text == "Keyingi3➡")
async def button_handler12(msg: Message):
    await msg.answer("Qaysi qahramon:",reply_markup=Exp4)

@dp.message(F.text == "Orqaga qaytish3⬅")
async def button_handler5(msg: Message):
    await msg.answer("Qaysi geroy:",reply_markup=Exp3)





@dp.message(F.text == "Cici")
async def exp_handler(msg: Message):
    await msg.answer("  🌀 CICI — Joyful Spinner\n     Rol: Fighter\n    Lane: EXP Lane\n    Kelib chiqishi: “Joyful Spinner” — yo-yo bilan jang qiluvchi, harakatchan va crowd controlga ega qahramon.",reply_markup=Cici)

@dp.message(F.text == "Passive(Cici)")
async def button_handler7(msg: Message):
    await msg.answer("   🧩 PASSIVE — Joyful Beat\n        Ta’siri:\n    Har safar Cici o‘zining yo-yo’si bilan dushmanga urilganda “Joyful Beat” faollashadi.\n     Har zarba Cici’ga HP qaytaradi (ya’ni lifesteal).\n     Bu passive skill va basic attack bilan ham ishlaydi.\n      Yo-yo dushmanlarga ketma-ket tegib qaytgani sari, Cici tezroq harakatlanadi.\n      Cici dushmanni doimiy urib tursa, yo-yo’si loopda aylanadi, bu unga combo davomida katta sustain beradi.\n         📘 Maslahat:\n    – Passive’ni saqlab turish uchun dushmanga ketma-ket zarba ber.\n   – Qochayotgan dushman ortidan yo-yo qaytishini hisobla – shunda lifesteal olasan.\n    – Teamfightda passivni yo‘qotmaslik uchun minionga yoki yaqin dushmanga yo-yo tashlab tur.")

@dp.message(F.text == "1-skill(Cici)")
async def button_handler7(msg: Message):
    await msg.answer("   ⚔️ SKILL 1 — Yo-Yo Blitz\n        Ta’siri:\n     Cici yo-yo’sini tanlangan yo‘nalishda otadi va u bir necha dushmanni urib, keyin qaytadi.\n      Har zarba fizik zarar beradi va passivni faollashtiradi.\n      Yo-yo qaytishda ham zarar yetkazadi.\n      📘 Maslahat:\n     – Yo-yo’ni devorga yaqin tashla, qaytishda ham dushmanga tegsin.\n     – Har doim minion to‘dasi ichida ishlat – damage ikki hissa oshadi.\n     – Teamfightda “yo-yo looping”ni saqlab turish uchun har safar dushman tanlang.")

@dp.message(F.text == "2-skill(Cici)")
async def button_handler7(msg: Message):
    await msg.answer("     💥 SKILL 2 — Jump & Spin (Joyful Combo)\n      Ta’siri:\n  Cici oldinga sakraydi, dushmanni uradi.\n  Bu CC (crowd control) turi, ya’ni dushman qocholmaydi.\n  Agar Cici zarba paytida yo-yo faol bo‘lsa, yo-yo ham shu dushmanga zarba beradi.\n Shuningdek, bu skill mobility beradi — dushmanga yaqinlashish yoki qochish uchun ishlatiladi.\n    📘 Maslahat:\n – Buni “engage” yoki “escape” uchun ishlat.\n – Skill 1 → Skill 2 combo – Cici uchun eng asosiy kombo.\n – Teamfightda CC’ni dushmanning Gold Lane yoki Mid’iga ishlat.")

@dp.message(F.text == "3-skill(Cici)")
async def button_handler7(msg: Message):
    await msg.answer("    🔮 SKILL 3 (ULTIMATE) — Finale Spin\n      Ta’siri:\n  Cici yo-yo’sini katta radiusda aylantirib, atrofdagi barcha dushmanlarni ichkariga tortadi.\n  Ularga jiddiy zarar beradi va qisqa vaqt davomida movement speed oshadi.\n  Bu Cici’ning eng kuchli teamfight skilli — katta AOE (Area of Effect) CC.\n      📘 Maslahat:\n – Teamfightda orqadan kirib ulti’ni ur — dushmanlarni bir joyga tortadi.\n – Agar Fredrinn, Tigreal yoki Atlas kabi CC hero bo‘lsa, ulardan keyin ur.\n – Ulti paytida passiv va skill 1 ni birga ishlat – HP tiklanadi, o‘lmay chiqasan.")

@dp.message(F.text == "Ortga⬅")
async def button_handler7(msg: Message):
    await msg.answer("Qaysi geroy:",reply_markup=Exp1)


    

@dp.message(F.text == "Yu Zhong")
async def exp_handler(msg: Message):
    await msg.answer("  🐉 YU ZHONG — The Black Dragon\n   Rol: Fighter\n   Lane: EXP Lane\n   Asosiy kuchi: Sustain + Lifesteal + Crowd Control + Teamfight",reply_markup=YuZhong)

@dp.message(F.text == "Passive(Yu Zhong)")
async def button_handler7(msg: Message):
    await msg.answer("   🩸 PASSIVE — Cursing Touch (Sha Residue)\n Ta’siri:\n      Har safar Yu Zhong dushmanga basic attack yoki skill bilan zarba berganda, u “Sha Residue” degan belgi qoldiradi.\n      Belgilar 5 taga yetganda dushman “Sha Energy” portlashini oladi va Yu Zhong o‘ziga HP qaytaradi (ya’ni lifesteal).\n      Passive’ning eng kuchli tomoni — jangda doimiy shifo olish (regen).\n      Belgilar 7 soniya ichida yo‘qoladi, lekin yangilanishi mumkin.\n 📘 Maslahat:\n      Har doim bir dushmanga ketma-ket zarba ber, belgilar 5 taga to‘lishi uchun.\n      Belgilar to‘lishi bilan skill 1 yoki 2 bilan combo qil, chunki passiv portlashi katta zarar beradi.\n      HP past bo‘lganda minion yoki jungleda passive bilan HP’ni qayta tiklab ol.")



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



async def main() -> None:
    print("✅ Bot ishga tushdi...")
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


