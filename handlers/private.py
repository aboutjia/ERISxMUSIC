
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**
𝙃𝙚𝙡𝙡𝙤 𝙄'𝙢🥀🎶 𝙀𝙧𝙞𝙨 𝙈𝙪𝙨𝙞𝙘 𝙋𝙡𝙖𝙮𝙚𝙧♀️ \nᴀ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴜꜱɪᴄ ꜱᴛʀᴇᴀᴍɪɴɢ ʙᴏᴛ ᴡɪᴛʜ ꜱᴏᴍᴇ ᴜꜱᴇꜰᴜʟ ꜰᴇᴀᴛᴜʀᴇꜱ\n⭐️𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲 [٭〖𓆩𝗖𝗨𝗧𝗘 𝐊𝐈𝐍𝐆 ᵀᴹ𓆪〗٭](https://t.me/BLACKSTORM_OWNER)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❰𝗢𝘄𝗻𝗲𝗿🤴❱", url="https://t.me/BlackStorm_Owner")
                  ],[
                    InlineKeyboardButton(
                        "❰𝗦𝘂𝗽𝗽𝗼𝗿𝘁🌎❱", url="https://t.me/ERISxCHAT"
                    ),
                    InlineKeyboardButton(
                        "❰𝗚𝗿𝗼𝘂𝗽🚩❱", url="https://t.me/ERISxCHAT"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "❰𝐂𝐡𝐚𝐭 𝐆𝐫𝐨𝐮𝐩🥀❱", url="https://t.me/SweetBuddiesClub"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("Support") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**𝙀𝙍𝙄𝙎𝙭𝙈𝙐𝙎𝙄𝘾🥀 𝐎𝐧𝐥𝐢𝐧𝐞\n🌠@BlackStorm_Owner 🥀**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝗦𝘂𝗽𝗽𝗼𝗿𝘁❤️", url="https://t.me/ERISxCHAT")
                ]
            ]
        )
   )
