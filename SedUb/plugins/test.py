from telethon import events
from SedUb import l313l
@l313l.ar_cmd(events.NewMessage(pattern=r"\.notify", outgoing=True))
async def notify_dev(event):
    #BiLaL
    developer_id = 1488114134
    message = "تم استدعاء المطور!"

    
    await borg.send_message(developer_id, message)

    
    await event.edit("تم إرسال إشعار للمطور!")

