from telethon import events
from SedUb imbort l313l

@l313l.ar_cmd(events.NewMessage(pattern=r"استدعاء المطور", outgoing=True))
async def dev(event):
    await event.edit("أنا هنا للمساعدة! كيف يمكنني مساعدتك؟")

