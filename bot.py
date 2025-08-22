import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties  # ✅ добавлено
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand
from config import BOT_TOKEN
from handlers import main_menu, speakers, expo, ai_pitch, awards, materials, about_kz, contacts, language

async def main():
    bot = Bot(BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))  # ✅ обновлено
    dp = Dispatcher(storage=MemoryStorage())
    
    for handler in (language.router, main_menu.router, speakers.router, expo.router, ai_pitch.router, awards.router, materials.router, about_kz.router, contacts.router):
        dp.include_router(handler)
    
    await bot.delete_webhook(drop_pending_updates=True)
    
    await bot.set_my_commands([
        BotCommand(command="start", description="Запуск бота"),
        BotCommand(command="language", description="Сменить язык")
    ])
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
