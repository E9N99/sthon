from telethon.sync import TelegramClient, events

api_id = 8897410
api_hash = '43cb89a7b70782868b77ace21c1341a9'
bot_token = "6770759431:AAE_pP4K0ug0ZVboc-Mll0nJuhaQ4B7YEuw"

client = TelegramClient('bboi', api_id, api_hash).start(bot_token=bot_token)

ban = ['خالتك', 'كسك','كفر','انعل','الفروخ','هينك','خرب','الحيوان','بايو','وجل','ينيج','اهلك','خوات','لعير','انيجك','بلاعين','عمتك','اصمطك','راس','كلخرا','طبك','كسه','خرـب','ابن','طبك','كسه','كسك','ك.س','نيك','شلابسة','شلابسه','مك','كسمك','ابنل','مص','مـص','عرضك','لطيز','بطيزگ','دمشي','كس','دنجب','لكحاب','عطل','كسي','خصاوي','اه كص','موص','يكفر','نيج','انبح','نيج','بول','نعال','غبي','ومرض','كسا','قناتي','مطلقة','فضيحه','فضيحة','جادة','ملطلط','انضمو','خرا','عقلك','كضو','كوم','اهينك','فعله','قحبة','ونجب','انجب','گسم','سرسح','خايس','طيز','طيژ','كفرتني','رب','لكحبة','عيرر','كلخره','ربك','زربان','دعبل','تمضرط','لقحبه','بطيزگ','بختك','فاشل','خصوه','نعل','زب','بدلي','انيج','اخ','ينعلك','كلب','طيز','ختك','ذبح','حلك','دعابل','خياش','جروب','فعلة','كحبه','تنبح','مناو','جاده','نيجه','بمك','قسمك','عطلات','شتركو','قوم','فاهين','تبريد','تبن','اتفل','كسم','طي','وانجب','دي','زراب','ازرب','كواد','خالتك','خواتك','اخواتك','بامك','لفروخ','بلبايو','فاهي','شعليك','بعمتك','دكم','اكل','نغل','كح','اخواتكم','توزيع','فعلو','بخالتك','منيوك','گواد','زيج','قت','نبي','يني','كمبي','مرض','كلخرة','زبي','امهاتكم','دكل','بطيز','مطي','عزك','ديي','جلغ','بيك','تخليني','اشتركو','سلم','توكل','فضيحه','عيررر','ابول','اكفر','بربك','مطاية','دعبله','الكحبه','كسك','كسعمتك','خره','يجدي','يربح','فروخكم','كواويد','قتل','مضرط','مطايه','لانيجك','خواتل','سكس','لحش','نيجك','شلابس','امك','كسة','حملة','ابو','جلب','عيري','گحاب','لتنبح','گحب','مسابقات','مسابقا']

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
        

print('sthon')

client.start()
client.run_until_disconnected()
