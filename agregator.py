import asyncio
import os
import logging
import g4f
from pyrogram import Client
from dotenv import load_dotenv

# Налаштування професійного логування
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

load_dotenv()

# Завантаження конфігурації
API_ID = os.getenv("TELEGRAM_API_ID")
API_HASH = os.getenv("TELEGRAM_API_HASH")
ADMIN_ID = int(os.getenv("ADMIN_ID"))
# Канал можна буде легко змінювати через .env
SOURCE_CHANNEL = os.getenv("SOURCE_CHANNEL")

app = Client("my_account", api_id=API_ID, api_hash=API_HASH)


async def rewrite_text(text: str) -> str:
    """Функція для рерайту тексту через ШІ-провайдер."""
    try:
        response = await g4f.ChatCompletion.create_async(
            model=g4f.models.default,
            messages=[{"role": "user", "content": f"Зроби рерайт тексту українською мовою: {text}"}],
        )
        return response
    except Exception as e:
        logger.error(f"Помилка ШІ: {e}")
        return text


async def main():
    logger.info("Запуск AI Telegram Aggregator...")

    async with app:
        last_msg_id = 0

        # Ініціалізація: отримуємо ID останнього повідомлення
        async for message in app.get_chat_history(SOURCE_CHANNEL, limit=1):
            last_msg_id = message.id
            logger.info(f"Підключено до {SOURCE_CHANNEL}. ID останнього поста: {last_msg_id}")

        logger.info("Активний моніторинг розпочато...")

        # Цикл пулінгу (Polling) для обходу обмежень
        while True:
            try:
                async for message in app.get_chat_history(SOURCE_CHANNEL, limit=1):
                    if message.id > last_msg_id and message.text:
                        logger.info(f"Знайдено новий пост! ID: {message.id}")

                        rewritten_text = await rewrite_text(message.text)
                        await app.send_message(ADMIN_ID, f"🔔 **НОВИЙ РЕРАЙТ:**\n\n{rewritten_text}")

                        last_msg_id = message.id
                        logger.info("Пост успішно оброблено та відправлено адміністратору.")

                await asyncio.sleep(10)  # Інтервал перевірки
            except Exception as e:
                logger.error(f"Помилка пулінгу: {e}")
                await asyncio.sleep(5)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Роботу бота зупинено користувачем.")