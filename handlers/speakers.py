from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from i18n import i18n

router = Router()

@router.message(F.text == "🎙 Участие в программе форума")
async def speakers_menu(message: Message):
    lang = message.from_user.language_code or "ru"
    
    await message.answer(
        f"{i18n(lang, 'menu.program')}\n\n"
        "✍️ Чтобы подать заявку — перейдите по ссылке:\n"
        "https://example.com/speakers-form\n\n"
        "📥 Гайдбук спикера:"
    )

    doc = FSInputFile("files/speakers_guide.pdf", filename="Спикерский_гайд.pdf")
    await message.answer_document(doc)
