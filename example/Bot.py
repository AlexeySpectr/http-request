import asyncio
import requests
import json
from API_TOKEN import API_TOKEN
from aiogram import Bot, Dispatcher
from aiogram.types import Message, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.filters import Command
from ТОКЕН_ОТ_BOTFATHER import ТОКЕН_ОТ_BOTFATHER

TOKEN = ТОКЕН_ОТ_BOTFATHER
bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Привет! 😊\nХочешь узнать текущую погоду в своём городе? (да/нет)"
    )


# Единый обработчик всех сообщений
@dp.message()
async def all_messages(message: Message):
    # Геопозиция
    if message.content_type == "location":
        lat = message.location.latitude
        lon = message.location.longitude
        coords = f"{lat},{lon}"
        params={"q":coords,"key":API_TOKEN}

        response_weather=requests.get("http://api.weatherapi.com/v1/current.json?",params=params)
        x=response_weather.json()
        await message.answer(
            f"Спасибо! 📍\nКоординаты: {coords}",
            reply_markup=ReplyKeyboardRemove()
        )
        await message.answer(f" Погода в вашем городе:{x["location"]["name"]}\nЧасовой пояс:{x["location"]["tz_id"]}\nТемпература:{x["current"]["temp_c"]}°C\nСкорость ветра:{x["current"]["wind_kph"]}км/ч\nВремя в регионе:{x["location"]["localtime"]}")
        # Спрашиваем про повтор
        await message.answer("Хотите узнать погоду ещё раз? (да/нет)")
        return

    # Текст
    if message.text is None:
        return  # Игнорируем все, что не текст

    text = message.text.lower()

    if text in ["да", "хочу", "конечно"]:
        # Создаём кнопку геопозиции
        kb = ReplyKeyboardBuilder()
        kb.add(
            KeyboardButton(
                text="Отправить геолокацию 📍",
                request_location=True
            )
        )
        await message.answer(
            "Отлично! Поделись своей геолокацией 👇",
            reply_markup=kb.as_markup(resize_keyboard=True, one_time_keyboard=True)
        )

    elif text in ["нет", "не хочу"]:
        await message.answer("Хорошо 😊 Если передумаешь — просто напиши 'погода'.")
    else:
        await message.answer("Напиши 'да' или 'нет' 🙂")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
