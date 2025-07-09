from telethon import TelegramClient, events
import os

API_ID = int(os.environ['API_ID'])
API_HASH = os.environ['API_HASH']
BOT_TOKEN = os.environ['BOT_TOKEN']

ALLOWED_USERS = [8040038495]  # ← अपना Telegram ID यहाँ डालें

client = TelegramClient("bot_session", API_ID, API_HASH)

async def main():
    await client.start(bot_token=BOT_TOKEN)

    @client.on(events.NewMessage(incoming=True))
    async def handler(event):
        await event.reply(f"🧾 Your Telegram ID: `{event.sender_id}`")

        if event.sender_id not in ALLOWED_USERS:
            await event.reply("🚫 You are not authorized to use this bot.")
            return

        if event.file:
            await event.reply("🔗 Generating link…")
            path = await event.download_media()
            if path:
                await event.reply(f"✅ Direct link:\n`{path}`")
            else:
                await event.reply("❌ Error: File not downloaded.")
        else:
            await event.reply("❌ Please send a file.")

    print("🤖 Bot is running...")
    await client.run_until_disconnected()

import asyncio
asyncio.run(main())
