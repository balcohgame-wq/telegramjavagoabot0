Create an advanced Telegram bot using Python (python-telegram-bot) with Google Gemini AI integration.

Features:

1. /start command:
Send message:

"🤖 Welcome to Umar Trades AI Bot 🚀

📊 This is an AI-powered trading assistant.

You can:
✔️ Ask trading questions
✔️ Get market guidance
✔️ Learn SMC & ICT concepts

💼 Our Services:
1 - Signals
2 - Account Management
3 - Other Services

💬 Or just send any message to chat with AI."

2. Menu system:
If user sends:
"1" → Signals message
"2" → Account Management message
"3" → Other services message

3. AI Chat Feature:
If user sends any other message:
👉 Send it to Google Gemini API
👉 Get response
👉 Reply back to user

4. Use Gemini API (google.generativeai)

5. Keep API key in variable:
GEMINI_API_KEY = "YOUR_API_KEY"

6. Telegram Bot Token:
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

7. Create files:
- main.py
- requirements.txt

8. requirements.txt must include:
python-telegram-bot
google-generativeai

9. Use polling

10. Clean, professional, commented code

11. Add instructions:
- where to put API keys
- how to run
- how to deploy on Render
