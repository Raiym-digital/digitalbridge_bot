from aiogram import Router, F
from aiogram.types import Message
from i18n import i18n

router = Router()

@router.message(F.text == "📤 Контакты команды")
async def show_contacts(message: Message):
    lang = message.from_user.language_code or "ru"

    await message.answer(
        f"{i18n(lang, 'menu.contacts')}\n\n"
        "📧 Email: team@digitalbridge.kz\n"
        "📞 Телефон: +7 7172 123 456\n"
        "📍 Адрес: г. Астана, пр. Мангилик Ел, 55/18"
    )
