from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from i18n import i18n

def get_main_menu(lang: str):
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=i18n(lang, "menu.program")),
         KeyboardButton(text=i18n(lang, "menu.expo"))],
        [KeyboardButton(text=i18n(lang, "menu.pitch")),
         KeyboardButton(text=i18n(lang, "menu.awards"))],
        [KeyboardButton(text=i18n(lang, "menu.kazakhstan"))],
        [KeyboardButton(text=i18n(lang, "menu.materials"))],
        [KeyboardButton(text=i18n(lang, "menu.contacts"))]
    ], resize_keyboard=True)
