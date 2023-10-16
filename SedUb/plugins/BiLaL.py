from telethon.sync import TelegramClient, events

api_id = 8897410
api_hash = '43cb89a7b70782868b77ace21c1341a9'
bot_token = "5379446716:AAEjjTjO9gVYdPLAP6MexaJFBJUv6qDeJ3g"

client = TelegramClient('bboi', api_id, api_hash).start(bot_token=bot_token)

ban = ['خالتك', 'كسك']

@client.on(events.NewMessage)
async def handle_new_message(event):
    sender = await event.get_sender()
    if sender.id:
        for word in ban:
            if word in event.raw_text:
                await event.delete()
                break
        chat = await event.get_chat()
        if chat.admin_rights:
            return
        

print('BiLaL')

client.start()
client.run_until_disconnected()
