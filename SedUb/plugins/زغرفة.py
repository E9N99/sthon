import random

from HuRe import l313l

from ..core.managers import edit_or_reply
from . import fonts

plugin_category = "extra"


@l313l.ar_cmd(
    pattern="زغرفة1(?:\s|$)([\s\S]*)",
    command=("زغرفة1", plugin_category),)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "**اعـطنـي نـص اولا 🧸🖤**")
        return
    string = "  ".join(args).lower()
    for normalfontcharacter in string:
        if normalfontcharacter in fonts.normalfont:
            musicalcharacter = fonts.musicalfont[
                fonts.normalfont.index(normalfontcharacter)
            ]
            string = string.replace(normalfontcharacter, musicalcharacter)
    await edit_or_reply(event, string)


@l313l.ar_cmd(
    pattern="زغرفة2(?:\s|$)([\s\S]*)",
    command=("زغرفة2", plugin_category),)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "**اعـطنـي نـص اولا 🌺😗🗿**")
        return
    string = "  ".join(args).lower()
    for normalfontcharacter in string:
        if normalfontcharacter in fonts.normalfont:
            ancientcharacter = fonts.ancientfont[
                fonts.normalfont.index(normalfontcharacter)
            ]
            string = string.replace(normalfontcharacter, ancientcharacter)
    await edit_or_reply(event, string)


@l313l.ar_cmd(
    pattern="زغرفة3(?:\s|$)([\s\S]*)",
    command=("زغرفة3", plugin_category),)
async def vapor(event):
    "Changes font style of the given text"
    reply_text = []
    textx = await event.get_reply_message()
    message = event.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await edit_or_reply(event, "اعـطنـي نـص اولا 🧸♥")
        return

    for charac in message:
        if 0x21 <= ord(charac) <= 0x7F:
            reply_text.append(chr(ord(charac) + 0xFEE0))
        elif ord(charac) == 0x20:
            reply_text.append(chr(0x3000))
        else:
            reply_text.append(charac)

    await edit_or_reply(event, "".join(reply_text))


@l313l.ar_cmd(
    pattern="زغرفة4(?:\s|$)([\s\S]*)",
    command=("زغرفة4", plugin_category),
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "**اعـطنـي نـص اولا 🧸🖤**")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            smallcapscharacter = fonts.smallcapsfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, smallcapscharacter)
    await edit_or_reply(event, string)


@l313l.ar_cmd(
    pattern="زغرفة5(?:\s|$)([\s\S]*)",
    command=("زغرفة5", plugin_category),
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "**اعـطنـي نـص اولا 🧸🖤**")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            bubblesblackcharacter = fonts.bubblesblackfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, bubblesblackcharacter)
    await edit_or_reply(event, string)


@l313l.ar_cmd(
    pattern="زغرفة6(?:\s|$)([\s\S]*)",
    command=("زغرفة6", plugin_category),
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "**اعـطنـي نـص اولا 🧸🖤**")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            bubblescharacter = fonts.bubblesfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, bubblescharacter)
    await edit_or_reply(event, string)


@l313l.ar_cmd(
    pattern="زغرفة7(?:\s|$)([\s\S]*)",
    command=("زغرفة7", plugin_category),
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "**اعـطنـي نـص اولا 🧸🖤**")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            tantextcharacter = fonts.tantextfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, tantextcharacter)
    await edit_or_reply(event, string)


@l313l.ar_cmd(
    pattern="زغرفة8(?:\s|$)([\s\S]*)",
    command=("زغرفة8", plugin_category),
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "**اعـطنـي نـص اولا 🧸🖤**")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            littleboxtextcharacter = fonts.littleboxtextfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, littleboxtextcharacter)
    await edit_or_reply(event, string)


@l313l.ar_cmd(
    pattern="زغرفة9(?:\s|$)([\s\S]*)",
    command=("زغرفة9", plugin_category),
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "**اعـطنـي نـص اولا 🧸🖤**")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            hwcapitalcharacter = fonts.hwcapitalfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, hwcapitalcharacter)
    await edit_or_reply(event, string)


@l313l.ar_cmd(
    pattern="زغرفة10(?:\s|$)([\s\S]*)",
    command=("زغرفة10", plugin_category),
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "**اعـطنـي نـص اولا 🧸🖤**")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            doubletextcharacter = fonts.doubletextfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, doubletextcharacter)
    await edit_or_reply(event, string)


@l313l.ar_cmd(
    pattern="زغرفة0(?:\s|$)([\s\S]*)",
    command=("زغرفة0", plugin_category),
)
async def spongemocktext(mock):
    "Changes font style of the given text"
    reply_text = []
    textx = await mock.get_reply_message()
    message = mock.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await edit_or_reply(mock, "اعـطنـي نـص اولا")
        return

    for charac in message:
        if charac.isalpha() and random.randint(0, 1):
            to_app = charac.upper() if charac.islower() else charac.lower()
            reply_text.append(to_app)
        else:
            reply_text.append(charac)

    await edit_or_reply(mock, "".join(reply_text))


@l313l.ar_cmd(pattern="تفعيل الزخرفة 1")
async def zakrafaon(event):
    if not gvarstatus("enzakrafa"):
        addgvar("enzakrafa", "on")
        await edit_delete(event, "**⪼ تـم تـفعـيل الزخـرفـة الإنـجليـزيـة 1**")
        return
    if gvarstatus("enzakrafa"):
        await edit_delete(event, "**⪼ الزخـرفـة الإنـجـليزيـة 1 مفعلـة مسبقًـا**")
        return


@l313l.ar_cmd(pattern="ايقاف الزخرفة 1")
async def zakrafaoff(event):
    if not gvarstatus("enzakrafa"):
        await edit_delete(event, "*⪼ عـذرًا عـزيـزي أنـت لـم تقـم بتفعيـل الزخـرفـة الإنجلـيزية 1*")
        return
    if gvarstatus("enzakrafa"):
        delgvar("enzakrafa")
        await edit_delete(event, "**⪼ تـم تـعطـيل الزخرفـة الإنـجليـزيـة 1**")
        return


@l313l.on(events.NewMessage(outgoing=True))
async def zakrafarun(event):
    if gvarstatus("enzakrafa"):
        text = event.message.message
        uppercase_text = (
            text.replace("a", "𝗮")
            .replace("b", "𝗯")
            .replace("c", "𝗰")
            .replace("d", "𝗱")
            .replace("e", "𝗲")
            .replace("f", "𝗳")
            .replace("g", "𝗴")
            .replace("h", "𝗵")
            .replace("i", "𝗶")
            .replace("j", "𝗷")
            .replace("k", "𝗸")
            .replace("l", "𝗹")
            .replace("m", "𝗺")
            .replace("n", "𝗻")
            .replace("o", "𝗼")
            .replace("p", "𝗽")
            .replace("q", "𝗾")
            .replace("r", "𝗿")
            .replace("s", "𝘀")
            .replace("t", "𝘁")
            .replace("u", "𝘂")
            .replace("v", "𝘃")
            .replace("w", "𝘄")
            .replace("x", "𝘅")
            .replace("y", "𝘆")
            .replace("z", "𝘇")
            .replace("H", "𝗵")
        )
        await event.edit(uppercase_text)
@l313l.ar_cmd(pattern="تفعيل الزخرفة 2")
async def zakrafaon(event):
    if not gvarstatus("enzakrafatwo"):
        addgvar("enzakrafatwo", "on")
        await edit_delete(event, "**⪼ تـم تـفعـيل الزخـرفـة الإنـجليـزيـة 2**")
        return
    if gvarstatus("enzakrafatwo"):
        await edit_delete(event, "**⪼ الزخـرفـة الإنـجـليزيـة 2 مفعلة مسبقًا .**")
        return


@l313l.ar_cmd(pattern="ايقاف الزخرفة 2")
async def zakrafaoff(event):
    if not gvarstatus("enzakrafatwo"):
        await edit_delete(event, "*⪼ عـذرًا عـزيـزي أنـت لـم تقـم بتفعيـل الزخـرفـة الإنجلـيزية 2*")
        return
    if gvarstatus("enzakrafatwo"):
        delgvar("enzakrafatwo")
        await edit_delete(event, "**⪼ تـم تـعطـيل الزخرفـة الإنـجليـزية 2**")
        return


@l313l.on(events.NewMessage(outgoing=True))
async def zakrafarun(event):
    if gvarstatus("enzakrafatwo"):
        text = event.message.message
        uppercase_text = (
            text.replace("a", "ꪖ")
            .replace("b", "Ⴆ")
            .replace("c", "ᥴ")
            .replace("d", "ᦔ")
            .replace("e", "꧖")
            .replace("f", "ƒ")
            .replace("g", "ᧁ")
            .replace("h", "ꫝ")
            .replace("i", "Ꭵ")
            .replace("j", "᧒")
            .replace("k", "ƙ")
            .replace("l", "ᥣ")
            .replace("m", "᧗")
            .replace("n", "ᥒ")
            .replace("o", "᥆")
            .replace("p", "ρ")
            .replace("q", "ᑫ")
            .replace("r", "ᖇ")
            .replace("s", "᥉")
            .replace("t", "ﾋ")
            .replace("u", "ꪊ")
            .replace("v", "ꪜ ")
            .replace("w", "ꪝ")
            .replace("x", "ꪎ")
            .replace("y", "ꪗ")
            .replace("z", "ᤁ")
            .replace("H", "ꫝ")
        )
        await event.edit(uppercase_text)
