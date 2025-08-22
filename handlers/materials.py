from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from i18n import i18n

router = Router()

@router.message(F.text == "ℹ️ Презентационные материалы")
async def presentation_materials(message: Message):
    lang = message.from_user.language_code or "ru"

    await message.answer(
        f"{i18n(lang, 'menu.materials')}\n\n"
        "📎 Ниже вы можете скачать презентацию форума."
    )

    doc = FSInputFile("files/forum_presentation.pdf", filename="Forum_Presentation.pdf")
    await message.answer_document(doc)
