from telethon import TelegramClient, events
import os

# 🔑 Telegram API credentials (Render Environment Variables)
API_ID = 27812739
API_HASH = os.environ['API_HASH']
BOT_TOKEN = os.environ['BOT_TOKEN']

# 🔐 Only allow this Telegram user ID (you)
ALLOWED_USERS = [8040038495]

# 🔌 Initialize the bot client
client = TelegramClient('filelinkbot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    sender = await event.get_sender()
    sender_id = sender.id

    # ❌ Block unauthorized users
    if sender_id not in ALLOWED_USERS:
        await event.reply("🚫 You are not authorized to use this bot.")
        return

    # ✅ Handle file messages
    if event.file:
        await event.reply("🔗 Generating direct link, please wait...")
        try:
            path = await event.download_media()
            if path:
                await event.reply(f"✅ File saved at:\n`{path}`\n\n📥 Paste this in 1DM to download.")
            else:
                await event.reply("⚠️ Error: File could not be saved.")
        except Exception as e:
            await event.reply(f"❌ Failed to process:\n`{str(e)}`")
    else:
        await event.reply("📎 Please send a file to generate a direct link.")

# 🔁 Keep the bot running
client.run_until_disconnected()
