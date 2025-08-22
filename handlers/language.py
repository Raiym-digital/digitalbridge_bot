from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from keyboards.menu import get_main_menu
from i18n import i18n

router = Router()

@router.message(Command("language"))
async def set_language(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🇷🇺 Русский")],
            [KeyboardButton(text="🇰🇿 Қазақша")],
            [KeyboardButton(text="🇬🇧 English")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )

    await message.answer(
        "🌐 Выберите язык:",
        reply_markup=keyboard
    )
