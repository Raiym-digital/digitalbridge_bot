from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from i18n import i18n

router = Router()

@router.message(F.text == "🏆 Digital Bridge Awards")
async def awards_menu(message: Message):
    lang = message.from_user.language_code or "ru"
    
    await message.answer(
        f"{i18n(lang, 'menu.awards')}\n\n"
        "🏅 Категории, критерии и условия доступны в PDF-гайде.\n"
        "Подать заявку: https://example.com/awards-form"
    )
    
    guide = FSInputFile("files/awards_guide.pdf", filename="Awards_Guide.pdf")
    await message.answer_document(guide)
