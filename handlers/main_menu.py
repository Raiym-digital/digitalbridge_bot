from aiogram import Router, F
from aiogram.types import Message
from keyboards.menu import get_main_menu
from i18n import i18n

router = Router()

@router.message(F.text == "/start")
async def start(message: Message):
    lang = message.from_user.language_code or "ru"
    await message.answer(i18n(lang, "welcome"), reply_markup=get_main_menu(lang))
