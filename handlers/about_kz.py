from aiogram import Router, F
from aiogram.types import Message
from i18n import i18n

router = Router()

@router.message(F.text == "ℹ️ Информация о Казахстане")
async def about_kazakhstan(message: Message):
    lang = message.from_user.language_code or "ru"

    await message.answer(
        f"{i18n(lang, 'menu.kazakhstan')}\n\n"
        "🗺 Туристическая информация, виза, проживание, трансферы:\n"
        "https://kazakhstan.travel\n\n"
        "📘 Электронный гид: https://el.kz\n\n"
        "✈️ Информация для иностранных гостей доступна на сайте форума."
    )
