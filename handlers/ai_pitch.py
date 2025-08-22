from aiogram import Router, F
from aiogram.types import Message
from i18n import i18n

router = Router()

@router.message(F.text == "🧠 AI Movement Pitch")
async def pitch_menu(message: Message):
    lang = message.from_user.language_code or "ru"
    await message.answer(
        f"{i18n(lang, 'menu.pitch')}\n\n"
        "📝 Подать заявку можно по ссылке:\n"
        "https://example.com/ai-pitch-form\n\n"
        "📚 Подробнее о программе: https://example.com/pitch-info"
    )
