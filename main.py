import asyncio
import random
from datetime import datetime, timedelta
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode
from apscheduler.schedulers.asyncio import AsyncIOScheduler

API_TOKEN = '8037472530:AAFjV2OTCdu5akajh8G_f98p83mOYp9pGnE'
GROUP_CHAT_ID = -1002206817997  # замените на ID вашей группы

# Список злобных сообщений
MESSAGES = [
    "😡 Марк уже смотрит твои косяки. А ты даже не начал готовиться.",
    "🧨 Настя предупредила один раз. Второго шанса не будет.",
    "🚫 Что за бардак на полке? Ты правда хочешь, чтобы Марк это увидел?",
    "💀 Инвентаризация близко. А у тебя – тотальный бардак. Удачи объяснять это Насте.",
    "😤 Марк проверит каждую SKU. Даже ту, про которую ты забыл.",
    "⏳ Часики тикают, а Настя уже пишет отчёт. Без тебя.",
    "🔍 Всё будет пересчитано. Твои ошибки – найдены. Удачи выжить.",
    "👀 Ты думаешь, что у тебя есть время? У Марка другое мнение.",
    "📋 Настя уже распечатывает список несостыковок. Там твоя фамилия первая.",
    "☠️ Если ты думаешь, что это просто инвентаризация – ты явно не работал с Настей.",
    "🔥 Каждый твой косяк будет зафиксирован. Не Марком. Судьбой.",
    "💣 На складе бардак? Поздравляю. Настя уже зовёт Марка.",
    "🪓 Марк не режет по живому. Он аккуратно разделяет на части за недостачу.",
    "📦 Ты думаешь, пара недостающих штук — это мелочь? Настя думает иначе.",
    "🩸 С каждой неучтённой коробкой ты приближаешь своё увольнение.",
    "🧾 Ты не заполнил накладную? Тогда накладная заполняет тебя.",
    "👻 Даже призраки на складе боятся инвентаризации с Настей.",
    "🕷️ Марк уже паутину собрал в углу склада. Ты не успел — ты опоздал.",
    "🥶 Кто не подготовился — тот замёрз. Настя не жалеет.",
    "📉 Ошибся в учёте? Надеюсь, ты не привязан к зарплате.",
    "🛑 Склад — не место для слабых. Особенно перед инвентаризацией.",
    "⚠️ Один неправильный штрихкод — и ты в отчёте под номером один.",
    "🔪 Настя идёт. У неё в руках — сканер. И список.",
    "🎯 Марк уже навёл на тебя прицел. Твой последний шанс — порядок на полках.",
    "🧼 Если на складе чисто — Настя улыбается. Если нет — улыбается Марк. Жестоко.",
    "📦 Склад не простит забытые позиции. А Марк — тем более.",
    "💤 Думаешь отдохнуть? Удачи отдыхать под прицелом сканера Насти."
]


# Список ссылок на картинки (или гифки)
IMAGES = [
    "https://imgur.com/1pnqgJT.jpg",
    "https://imgur.com/ejvlpXk.jpg",
    "https://imgur.com/iCcwfBr.jpg",
    "https://imgur.com/U6T00u3.jpg",
    "https://imgur.com/n431QMW.jpg",
    "https://imgur.com/jZwLqfK.jpg",
    "https://imgur.com/ip6jCKU.jpg",
    "https://imgur.com/jUaqPWT.jpg",
    "https://imgur.com/SbeyTf5.jpg",
    "https://imgur.com/q9gLuzI.jpg",
    "https://imgur.com/zgHBADJ.jpg",
    "https://imgur.com/H2MuIuy.jpg",
    "https://imgur.com/vJzwPaW.jpg",
    "https://imgur.com/MbfdPBX.jpg",
    "https://imgur.com/HPzezNL.jpg",
    "https://imgur.com/tZjy5lm.jpg",
    "https://imgur.com/1WFT82K.jpg",
    "https://imgur.com/hmG01Oa.jpg",
    "https://imgur.com/h4lFX9S.jpg",
    "https://imgur.com/h8fYRjR.jpg",
    "https://imgur.com/p0vWjSB.jpg",
    "https://imgur.com/vi1EdsO.jpg",
    "https://imgur.com/uLFQllm.jpg",
    "https://imgur.com/yHSAYnZ.jpg",
    "https://imgur.com/XbMSUdD.jpg",
    "https://imgur.com/I4PaOzX.jpg",
    "https://imgur.com/wIKzrh1.jpg",
    "https://imgur.com/0bpIrKH.jpg",
    "https://imgur.com/MvDoUxn.jpg"

]

# Дата инвентаризации
INVENTORY_DATE = datetime(2025, 4, 21, 0, 0, 0)

# Создание бота и диспетчера
bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())
scheduler = AsyncIOScheduler()

# Функция расчёта оставшегося времени
def get_time_left():
    now = datetime.now()
    delta: timedelta = INVENTORY_DATE - now
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes = remainder // 60
    return days, hours, minutes

# Задача: напоминание
async def send_reminder():
    days, hours, minutes = get_time_left()
    if days < 0:
        message_text = "✅ Инвентаризация уже прошла. Спасибо всем за усилия!"
    else:
        message_text = (
            f"⏰ <b>До инвентаризации осталось:</b> {days} дн, {hours} ч, {minutes} мин\n\n"
            f"{random.choice(MESSAGES)}"
        )
        photo_url = random.choice(IMAGES)
        await bot.send_photo(chat_id=GROUP_CHAT_ID, photo=photo_url, caption=message_text)

# Обработчик команды /start
@dp.message()
async def handle_start(message: Message):
    if message.text == "/start":
        days, hours, minutes = get_time_left()
        if days < 0:
            msg = "✅ Инвентаризация уже прошла. Надеюсь, ты выжил."
        else:
            msg = (
                f"⏰ <b>До инвентаризации осталось:</b> {days} дн, {hours} ч, {minutes} мин\n\n"
                f"{random.choice(MESSAGES)}"
            )
            photo_url = random.choice(IMAGES)
            await bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption=msg)

# Основная функция
async def main():
    scheduler.start()
    scheduler.add_job(send_reminder, 'interval', hours=6)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
