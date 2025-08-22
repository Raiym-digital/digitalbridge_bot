from aiogram import Router, F
from aiogram.types import Message
from i18n import i18n

router = Router()

@router.message(F.text == "🏢 Участие в выставочной зоне")
async def expo_menu(message: Message):
    lang = message.from_user.language_code or "ru"
    await message.answer(
        f"{i18n(lang, 'menu.expo')}\n\n"
        "📝 Заявка на участие доступна по ссылке:\n"
        "https://example.com/expo-form\n\n"
        "📐 Укажите размер стенда, интернет, пожелания и т.д."
    )
