# AI Telegram Content Aggregator

An asynchronous Python application designed to actively monitor target Telegram channels, extract new text posts, rewrite them using AI (via the `g4f` library), and automatically forward the processed content to an administrator for moderation. 

Built with resilience in mind, this bot utilizes a polling mechanism via the Pyrogram library to bypass standard Webhook/Update restrictions, ensuring stable data collection.

## 🚀 Features
* **Active Polling System:** Periodically checks target channels to avoid silent connection drops or missed updates.
* **AI Integration:** Automatically rewrites content to maintain originality, powered by free AI models via `g4f`.
* **Asynchronous Architecture:** Built with `asyncio` for non-blocking operations and high performance.
* **Secure Setup:** Keeps sensitive session data and API keys completely separated from the main logic.

## 🛠️ Technologies
* Python 3.12+
* [Pyrogram](https://docs.pyrogram.org/) (MTProto API framework)
* `g4f` (Free GPT provider)
* `asyncio` & `python-dotenv`

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/ai-telegram-aggregator.git](https://github.com/yourusername/ai-telegram-aggregator.git)
   cd ai-telegram-aggregator