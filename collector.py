from pyrogram import Client, filters

# Твої дані з my.telegram.org
api_id = 1234567  # Заміни на свій
api_hash = "твій_хеш_сюди"

app = Client("my_account", api_id=api_id, api_hash=api_hash)

# Список ID каналів, які ми моніторимо (Анжеліка скине посилання)
SOURCE_CHANNELS = [-100123456789, -100987654321]


@app.on_message(filters.chat(SOURCE_CHANNELS) & filters.text)
async def message_handler(client, message):
    print(f"📥 Отримано новий пост з {message.chat.title}:")
    print(f"Текст: {message.text[:50]}...")

    # Тут ми пізніше додамо відправку в Gemini для рерайту
    # А потім — пересилку тобі на перевірку


print("🚀 Збирач постів запущено...")
app.run()