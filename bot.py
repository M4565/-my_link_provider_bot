from telethon import TelegramClient, events
import os

API_ID = int(os.environ['API_ID'])
API_HASH = os.environ['API_HASH']
BOT_TOKEN = os.environ['BOT_TOKEN']

client = TelegramClient('filelinkbot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if event.file:
        await event.reply("🔗 Generating link…")
        path = await event.download_media()
        await event.reply(f"✅ Direct link:\n`{path}`")
    else:
        await event.reply("❌ Send a file, please.")
client.run_until_disconnected()
