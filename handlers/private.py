
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**
๐๐๐ก๐ก๐ค ๐'๐ข๐ฅ๐ถ ๐๐ง๐๐จ ๐๐ช๐จ๐๐ ๐๐ก๐๐ฎ๐๐งโ๏ธ \nแด แดแดสแดษขสแดแด แดแด๊ฑษชแด ๊ฑแดสแดแดแดษชษดษข สแดแด แดกษชแดส ๊ฑแดแดแด แด๊ฑแด๊ฐแดส ๊ฐแดแดแดแดสแด๊ฑ\nโญ๏ธ๐๐๐ฏ๐๐ฅ๐จ๐ฉ๐๐ ๐๐ฒ [ูญใ๐ฉ๐๐จ๐ง๐ ๐๐๐๐ แตแดน๐ชใูญ](https://t.me/BLACKSTORM_OWNER)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โฐ๐ข๐๐ป๐ฒ๐ฟ๐คดโฑ", url="https://t.me/BlackStorm_Owner")
                  ],[
                    InlineKeyboardButton(
                        "โฐ๐ฆ๐๐ฝ๐ฝ๐ผ๐ฟ๐๐โฑ", url="https://t.me/ERISxCHAT"
                    ),
                    InlineKeyboardButton(
                        "โฐ๐๐ฟ๐ผ๐๐ฝ๐ฉโฑ", url="https://t.me/ERISxCHAT"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "โฐ๐๐ก๐๐ญ ๐๐ซ๐จ๐ฎ๐ฉ๐ฅโฑ", url="https://t.me/SweetBuddiesClub"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("Support") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**๐๐๐๐๐ญ๐๐๐๐๐พ๐ฅ ๐๐ง๐ฅ๐ข๐ง๐\n๐ @BlackStorm_Owner ๐ฅ**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ฆ๐๐ฝ๐ฝ๐ผ๐ฟ๐โค๏ธ", url="https://t.me/ERISxCHAT")
                ]
            ]
        )
   )
