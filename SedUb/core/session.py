import sys
from SedUb.core.logger import logging
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions import StringSession
from telethon.errors import AccessTokenExpiredError, AccessTokenInvalidError
from ..Config import Config
from .AlsedUb import AlsedPyro
from .client import HuReClient
LOGS = logging.getLogger(" ")

__version__ = "2.10.6"

loop = None

if Config.STRING_SESSION:
    session = StringSession(str(Config.STRING_SESSION))
else:
    session = "SedUb"

try:
    l313l = HuReClient(
        session=session,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        loop=loop,
        app_version=__version__,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
except Exception as e:
    print(f"[STRING SESSION] - {str(e)}")
    sys.exit()

 try:
     l313l = HuReClient(
         aljokerPyro(Config.STRING_SESSION, LOGS),
         api_id=Config.APP_ID,
         api_hash=Config.API_HASH,
         loop=loop,
         app_version=__version__,
         connection=ConnectionTcpAbridged,
         auto_reconnect=True,
         connection_retries=None,
     )
 except Exception as e:
     print(f"[STRING ALJOKER] - {str(e)}")
     sys.exit()

try:
    l313l.tgbot = tgbot = HuReClient(
        session="arTgbot",
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        loop=loop,
        app_version=__version__,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    ).start(bot_token=Config.TG_BOT_TOKEN)
except AccessTokenExpiredError:
    LOGS.error("توكن البوت منتهي الصلاحية قم باستبداله ليعمل السورس")
except AccessTokenInvalidError:
    LOGS.error("توكن البوت غير صحيح قم باستبداله ليعمل السورس")
