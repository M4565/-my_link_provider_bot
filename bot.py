from telethon import TelegramClient, events
import os

API_ID = int(os.environ['API_ID'])
API_HASH = os.environ['API_HASH']
BOT_TOKEN = os.environ['BOT_TOKEN']

ALLOWED_USERS = [8040038495]  # ← यहां अपना सही Telegram ID डालें

client = TelegramClient('filelinkbot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    await event.reply(f"🧾 Your Telegram ID: `{event.sender_id}`")

    if event.sender_id not in ALLOWED_USERS:
        await event.reply("🚫 You are not authorized to use this bot.")
        return

    if event.file:
        await event.reply("🔗 Generating link…")
        try:
            path = await event.download_media()
            if path:
                await event.reply(f"✅ Direct link:\n`{path}`")
            else:
                await event.reply("❌ Error: File not downloaded.")
        except Exception as e:
            await event.reply(f"❌ Failed to download:\n{str(e)}")
    else:
        await event.reply("❌ Please send a file.")

client.run_until_disconnected()
