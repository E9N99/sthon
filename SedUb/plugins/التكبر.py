import asyncio
from telethon import events
from SedUb import l313l


bilal_enabled = False
sed_enabled = False
Sedthon_ID = {}

@l313l.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def mark_as_read(event):
    global sed_enabled, Sedthon_ID
    sender_id = event.sender_id
    if sed_enabled and sender_id in Sedthon_ID:
        Sedthon_time = Sedthon_ID[sender_id]
        if Sedthon_time > 0:
            await asyncio.sleep(Sedthon_time)
        await event.mark_read()

@l313l.on(events.NewMessage(outgoing=True, pattern=r'^\.التكبر تعطيل$'))
async def Hussein(event):
    global sed_enabled
    sed_enabled = False
    await event.edit('**᯽︙ تم تعطيل امر التكبر بنجاح ✅**')

@l313l.on(events.NewMessage(outgoing=True, pattern=r'^\.التكبر (\d+) (\d+)$'))
async def Hussein(event):
    global sed_enabled, Sedthon_ID
    Sedthon_time = int(event.pattern_match.group(1))
    user_id = int(event.pattern_match.group(2)) 
    Sedthon_ID[user_id] = Sedthon_time
    sed_enabled = True
    await event.edit(f'**᯽︙ تم تفعيل امر التكبر بنجاح مع  {Sedthon_time} ثانية للمستخدم {user_id}**')

@l313l.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def Hussein(event):
    global bilal_enabled
    if bilal_enabled:
        if Sedthon_time > 0:
            await asyncio.sleep(Sedthon_time)
        await event.mark_read()

@l313l.on(events.NewMessage(outgoing=True, pattern=r'^\.مود التكبر تعطيل$'))
async def Hussein(event):
    global bilal_enabled
    bilal_enabled = False
    await event.edit('**᯽︙ تم تعطيل امر التكبر على الجميع بنجاح ✅**')

@l313l.on(admin_cmd(pattern=f"مود التكبر (\d+)"))
async def Hussein(event):
    global bilal_enabled
    Sedthon_time = int(event.pattern_match.group(1))
    bilal_enabled = True
    await event.edit(f'**᯽︙ تم تفعيل امر التكبر بنجاح مع  {Sedthon_time} ثانية**')
