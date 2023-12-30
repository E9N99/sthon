@app.on_message(command("رفع رقاصه"))
async def yasooo(client, message):
    try:
        
        excluded_user_id = 1488114134
        if message.reply_to_message.from_user.id == excluded_user_id:
            await message.reply_text("لا يمكن رفع هذا المستخدم كرقاصة.")
        else:
            if message.reply_to_message.from_user.mention not in raqsa:
                raqsa.append(message.reply_to_message.from_user.mention)
            await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n رقاصه واحد يذب فلوس عليها 😂💃")
    except Exception as e:
        await message.reply_text(f"حدث خطأ: {e}")


