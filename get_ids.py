import os
from pyrogram import Client, filters
from dotenv import load_dotenv

load_dotenv()

# Створюємо клієнт БЕЗ asyncio (синхронно)
app = Client(
    "my_account",
    api_id=int(os.getenv("TELEGRAM_API_ID")),
    api_hash=os.getenv("TELEGRAM_API_HASH")
)

@app.on_message() # Прибираємо всі фільтри, слухаємо ВСЕ
def print_ids(client, message):
    # Перевіряємо, чи це переслане повідомлення
    if message.forward_from_chat:
        chat = message.forward_from_chat
        print(f"✅ ЗНАЙДЕНО КАНАЛ: {chat.title} | ID: {chat.id}")
    else:
        # Якщо просто пишеш у чат
        chat_name = message.chat.title or message.chat.first_name or "Приватний чат"
        print(f"📌 Повідомлення в чаті: {chat_name} | ID: {message.chat.id}")

app.run()