# (c) @AbirHasan2005 & Jigar Varma & Hemanta Pokharel & Akib Hridoy

import asyncio
from pyrogram import Client, filters
from pyrogram.errors import QueryIdInvalid, FloodWait
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, InlineQuery, \
    InlineQueryResultArticle, InputTextMessageContent

from configs import Config
from tool import SearchYTS, SearchAnime, Search1337x, SearchPirateBay, SearchLime, SearchRarbg, \
    SearchGalaxy, SearchTorlock, SearchEztv, SearchKickass, SearchZooqle, SearchBit, \
    SearchGlodls, SearchMagnetdl, SearchTorrentfunk, SearchTpro, SearchTorrentz, \
    SearchPH, SearchXVID, SearchRT

TorrentBot = Client(session_name=Config.SESSION_NAME, api_id=Config.API_ID,
                    api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN)
DEFAULT_SEARCH_MARKUP = [
    [InlineKeyboardButton("Search Anime", switch_inline_query_current_chat="!a "),
     InlineKeyboardButton("Inline", switch_inline_query="!a ")],
    [InlineKeyboardButton("Search in YTS", switch_inline_query_current_chat="!y "),
     InlineKeyboardButton("Inline", switch_inline_query="!y ")],
    [InlineKeyboardButton("Search in 1337x", switch_inline_query_current_chat="!x "),
     InlineKeyboardButton("Inline", switch_inline_query="!x ")],
    [InlineKeyboardButton("Search in PirateBay", switch_inline_query_current_chat="!p "),
     InlineKeyboardButton("Inline", switch_inline_query_current_chat="!p ")],
    [InlineKeyboardButton("Search in LimeTorrent", switch_inline_query_current_chat="!l "),
     InlineKeyboardButton("Inline", switch_inline_query_current_chat="!l ")],
    [InlineKeyboardButton("Search in Rarbg", switch_inline_query_current_chat="!r "),
     InlineKeyboardButton("Inline", switch_inline_query_current_chat="!r ")],
    [InlineKeyboardButton("Search in TorrentGalaxy", switch_inline_query_current_chat=""),
     InlineKeyboardButton("Inline", switch_inline_query_current_chat="")],
    #[InlineKeyboardButton("Search in TorLock", switch_inline_query_current_chat="!t "),
     #InlineKeyboardButton("Inline", switch_inline_query_current_chat="!t ")],
    [InlineKeyboardButton("Search in EzTV", switch_inline_query_current_chat="!e "),
     InlineKeyboardButton("Inline", switch_inline_query_current_chat="!e ")],
    #[InlineKeyboardButton("Search in KickAss", switch_inline_query_current_chat="!k "),
     #InlineKeyboardButton("Inline", switch_inline_query_current_chat="!k ")],
    #[InlineKeyboardButton("Search in ZooQle", switch_inline_query_current_chat="!z "),
     #InlineKeyboardButton("Inline", switch_inline_query_current_chat="!z ")],
    # [InlineKeyboardButton("Search in BitSearch", switch_inline_query_current_chat="!b "),
    # InlineKeyboardButton("Inline", switch_inline_query_current_chat="!b ")],
    #[InlineKeyboardButton("Search in GloDLs", switch_inline_query_current_chat="!gd "),
     #InlineKeyboardButton("Inline", switch_inline_query_current_chat="!gd ")],
    #[InlineKeyboardButton("Search in MagnetDL", switch_inline_query_current_chat="!md "),
     #InlineKeyboardButton("Inline", switch_inline_query_current_chat="!md ")],
    [InlineKeyboardButton("Search in TorrentFunk", switch_inline_query_current_chat="!tf "),
     InlineKeyboardButton("Inline", switch_inline_query_current_chat="!tf ")],
    [InlineKeyboardButton("Search in TorrentProject", switch_inline_query_current_chat="!tp "),
     InlineKeyboardButton("Inline", switch_inline_query_current_chat="!tp ")],
    [InlineKeyboardButton("Search in TorrentZ", switch_inline_query_current_chat="!tz "),
     InlineKeyboardButton("Inline", switch_inline_query_current_chat="!tz ")],
    [InlineKeyboardButton("OWNER", url="https://t.me/jettastic")]
    [InlineKeyboardButton("Channel", url="https://t.me/jetbots")]
    [InlineKeyboardButton("Our Other Bots", url="https://t.me/jetbots/26")]
]


@TorrentBot.on_message(filters.command("start"))
async def start_handler(_, message: Message):
    try:
        await message.reply_text(
            text="Hello, I am Torrent Search Bot!\n"
                 "I can search Torrents from Inline.\n\n"
                 "Credit: @AbirHasan2005\n\n\n",
            disable_web_page_preview=True,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(DEFAULT_SEARCH_MARKUP)
        )
    except FloodWait as e:
        print(f"[{Config.SESSION_NAME}] - Sleeping for {e.x}s")
        await asyncio.sleep(e.x)
        await start_handler(_, message)


@TorrentBot.on_inline_query()
async def inline_handlers(_, inline: InlineQuery):
    search_ts = inline.query
    answers = []
    if search_ts == "":
        answers.append(
            InlineQueryResultArticle(
                title="Search Something...",
                description="Search For Torrents...",
                input_message_content=InputTextMessageContent(
                    message_text="Search for Torrents from Inline!",
                    parse_mode="Markdown"
                ),
                reply_markup=InlineKeyboardMarkup(DEFAULT_SEARCH_MARKUP)
            )
        )
    elif search_ts.startswith("!rt"):
        query = search_ts.split(" ", 1)[-1]
        if (query == "") or (query == " "):
            answers.append(
                InlineQueryResultArticle(
                    title="!rt [id]",
                    description="So, you've already discovered me!",
                    input_message_content=InputTextMessageContent(
                        message_text="`!ph [id]`\n\nSearch PornHub from Inline!",
                        parse_mode="Markdown"
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="!rt ")]])
                )
            )
        else:
            torrentList = await SearchRT(query)
            if not torrentList:
                answers.append(
                    InlineQueryResultArticle(
                        title="No video found associated this ID",
                        description=f"Can't find video for '{query}'",
                        input_message_content=InputTextMessageContent(
                            message_text=f"No Videos Found For `{query}`",
                            parse_mode="Markdown"
                        ),
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton("Try Again", switch_inline_query_current_chat="!rt ")]])
                    )
                )
            else:
                for i in range(len(torrentList)):
                        answers.append(
                            InlineQueryResultArticle(
                                title="LINK HERE",
                                #description=f"Seeders: {torrentList[i]['Seeders']}, Leechers: {torrentList[i]['Leechers']}\nSize: {torrentList[i]['Size']}",
                                input_message_content=InputTextMessageContent(
                                    message_text=f"**1080_PIX:** `{torrentList[i]['1080p']}`\n"
                                                 f"**720_PIX:** `{torrentList[i]['720p']}`\n"
                                                 f"**480_PIX:** `{torrentList[i]['480p']}`\n"
                                                 f"**240_PIX:** `{torrentList[i]['240p']}`\n",
                                    parse_mode="Markdown"
                                ),
                                reply_markup=InlineKeyboardMarkup(
                                    [[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="!rt ")]])
                            )
                        )
    elif search_ts.startswith("!xv"):
        query = search_ts.split(" ", 1)[-1]
        if (query == "") or (query == " "):
            answers.append(
                InlineQueryResultArticle(
                    title="!xv [id]",
                    description="So, you've already discovered me!",
                    input_message_content=InputTextMessageContent(
                        message_text="`!ph [id]`\n\nSearch PornHub from Inline!",
                        parse_mode="Markdown"
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="!xv ")]])
                )
            )
        else:
            torrentList = await SearchXVID(query)
            if not torrentList:
                answers.append(
                    InlineQueryResultArticle(
                        title="No Torrents Found in ThePirateBay!",
                        description=f"Can't find torrents for '{query}'",
                        input_message_content=InputTextMessageContent(
                            message_text=f"No Torrents Found For `{query}`",
                            parse_mode="Markdown"
                        ),
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton("Try Again", switch_inline_query_current_chat="!xv ")]])
                    )
                )
            else:
                for i in range(len(torrentList)):
                        answers.append(
                            InlineQueryResultArticle(
                                title="LINK HERE",
                                #description=f"Seeders: {torrentList[i]['Seeders']}, Leechers: {torrentList[i]['Leechers']}\nSize: {torrentList[i]['Size']}",
                                input_message_content=InputTextMessageContent(
                                    message_text=f"**HD:** `{torrentList[i]['high']}`\n"
                                                 f"**LOW:** `{torrentList[i]['low']}`\n",
                                    parse_mode="Markdown"
                                ),
                                reply_markup=InlineKeyboardMarkup(
                                    [[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="!xv ")]])
                            )
                        )
    elif search_ts.startswith("!ph"):
        query = search_ts.split(" ", 1)[-1]
        if (query == "") or (query == " "):
            answers.append(
                InlineQueryResultArticle(
                    title="!ph [id]",
                    description="So, you discovered me!",
                    input_message_content=InputTextMessageContent(
                        message_text="`!ph [id]`\n\nSearch PornHub from Inline!",
                        parse_mode="Markdown"
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="!ph ")]])
                )
            )
        else:
            torrentList = await SearchPH(query)
            if not torrentList:
                answers.append(
                    InlineQueryResultArticle(
                        title="No Video fonnd!",
                        description=f"Can't find video for '{query}'",
                        input_message_content=InputTextMessageContent(
                            message_text=f"No Videos Found For `{query}`",
                            parse_mode="Markdown"
                        ),
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton("Try Again", switch_inline_query_current_chat="!ph ")]])
                    )
                )
            else:
                for i in range(len(torrentList)):
                        answers.append(
                            InlineQueryResultArticle(
                                title="LINK HERE",
                                #description=f"Seeders: {torrentList[i]['Seeders']}, Leechers: {torrentList[i]['Leechers']}\nSize: {torrentList[i]['Size']}",
                                input_message_content=InputTextMessageContent(
                                    message_text=f"**1080_PIX:** `{torrentList[i]['1080p']}`\n"
                                                 f"**720_PIX:** `{torrentList[i]['720p']}`\n"
                                                 f"**480_PIX:** `{torrentList[i]['480p']}`\n"
                                                 f"**240_PIX:** `{torrentList[i]['240p']}`\n",
                                    parse_mode="Markdown"
                                ),
                                reply_markup=InlineKeyboardMarkup(
                                    [[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="!ph ")]])
                            )
                        )
    elif search_ts.startswith("!p"):
        query = search_ts.split(" ", 1)[-1]
        if (query == "") or (query == " "):
            answers.append(
                InlineQueryResultArticle(
                    title="!p [text]",
                    description="Search For Torrent in ThePirateBay...",
                    input_message_content=InputTextMessageContent(
                        message_text="`!p [text]`\n\nSearch ThePirateBay Torrents from Inline!",
                        parse_mode="Markdown"
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="!p ")]])
                )
            )
        else:
            torrentList = await SearchPirateBay(query)
            if not torrentList:
                answers.append(
                    InlineQueryResultArticle(
                        title="No Torrents Found in ThePirateBay!",
                        description=f"Can't find torrents for '{query}'",
                        input_message_content=InputTextMessageContent(
                            message_text=f"No Torrents Found For `{query}`",
                            parse_mode="Markdown"
                        ),
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton("Try Again", switch_inline_query_current_chat="!p ")]])
                    )
                )
            else:
                for i in range(len(torrentList)):
                        answers.append(
                            InlineQueryResultArticle(
                                title=f"{torrentList[i]['Name']}",
                                description=f"Seeders: {torrentList[i]['Seeders']}, Leechers: {torrentList[i]['Leechers']}\nSize: {torrentList[i]['Size']}",
                                input_message_content=InputTextMessageContent(
                                    message_text=f"**Category:** `{torrentList[i]['Category']}`\n"
                                                 f"**Name:** `{torrentList[i]['Name']}`\n"
                                                 f"**Size:** `{torrentList[i]['Size']}`\n"
                                                 f"**Seeders:** `{torrentList[i]['Seeders']}`\n"
                                                 f"**Leechers:** `{torrentList[i]['Leechers']}`\n"
                                                 f"**Uploader:** `{torrentList[i]['Uploader']}`\n"
                                                 f"**Uploaded on {torrentList[i]['Date']}**\n\n"
                                                 f"**Magnet:**\n`{torrentList[i]['Magnet']}`\n\n",
                                    parse_mode="Markdown"
                                ),
                                reply_markup=InlineKeyboardMarkup(
                                    [[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="!p ")]])
                            )
                        )
    elif search_ts.startswith("!tz"):
        query = search_ts.split(" ", 1)[-1]
        if (query == "") or (query == " "):
            answers.append(
                InlineQueryResultArticle(
                    title="!tz [text]",
                    description="Search For Torrent in TorrentZ...",
                    input_message_content=InputTextMessageContent(
                        message_text="`!tz [text]`\n\nSearch TorrentZ Torrents from Inline!",
                        parse_mode="Markdown"
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="!tz ")]])
                )
            )
        else:
            torrentList = await SearchTorrentz(query)
            if not torrentList:
                answers.append(
                    InlineQueryResultArticle(
                        title="No Torrents Found in TorrentZ!",
                        description=f"Can't find torrents for '{query}'",
                        input_message_content=InputTextMessageContent(
                            message_text=f"No Torrents Found For `{query}`",
                            parse_mode="Markdown"
                        ),
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton("Try Again", switch_inline_query_current_chat="!tz ")]])
                    )
                )
            else:
                if len(torrentList) > 20:
                   for i in range(20):
                        answers.append(
                            InlineQueryResultArticle(
                                title=f"{torrentList[i]['Name']}",
                                description=f"Seeders: {torrentList[i]['Seeders']}, Leechers: {torrentList[i]['Leechers']}\nSize: {torrentList[i]['Size']}",
                                input_message_content=InputTextMessageContent(
                                    message_text=f"**Name:** `{torrentList[i]['Name']}`\n"
                                                 f"**Size:** `{torrentList[i]['Size']}`\n"
                                                 f"**Seeders:** `{torrentList[i]['Seeders']}`\n"
                                                 f"**Leechers:** `{torrentList[i]['Leechers']}`\n"
                                                 f"**Uploaded {torrentList[i]['Updated']}**\n\n"
                                                 f"**Magnet:**\n`{torrentList[i]['Magnet']}`\n\n",
                                    parse_mode="Markdown"
                                ),
                                reply_markup=InlineKeyboardMarkup(
                                    [[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="!tz ")]])
                            )
                        )
                else:
                    pass
    elif search_ts.startswith("!tp"):
        query = search_ts.split(" ", 1)[-1]
        if (query == "") or (query == " "):
            answers.append(
                InlineQueryResultArticle(
                    title="!tp [text]",
                    description="Search For Torrent in TorrentProject...",
                    input_message_content=InputTextMessageContent(
                        message_text="`!tp [text]`\n\nSearch TorrentProject from Inline!",
                        parse_mode="Markdown"
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="!tp ")]])
                )
            )
        else:
            torrentList = await SearchTpro(query)
            if not torrentList:
                answers.append(
                    InlineQueryResultArticle(
                        title="No Torrents Found in TorrentProject!",
                        description=f"Can't find torrents for '{query}'",
                        input_message_content=InputTextMessageContent(
                            message_text=f"No Torrents Found For `{query}`",
                            parse_mode="Markdown"
                        ),
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton("Try Again", switch_inline_query_current_chat="!tp ")]])
                    )
                )
            else:
                if len(torrentList) > 20:
                   for i in range(20):
                        answers.append(
                            InlineQueryResultArticle(
                                title=f"{torrentList[i]['Name']}",
                                description=f"Seeders: {torrentList[i]['Seeders']}, Leechers: {torrentList[i]['Leechers']}\nSize: {torrentList[i]['Size']}",
                                input_message_content=InputTextMessageContent(
                                    message_text=f"**Name:** `{torrentList[i]['Name']}`\n"
                                                 f"**Size:** `{torrentList[i]['Size']}`\n"
                                                 f"**Seeders:** `{torrentList[i]['Seeders']}`\n"
                                                 f"**Leechers:** `{torrentList[i]['Leechers']}`\n"
                                                 f"**Uploaded about {torrentList[i]['DateUploaded']}**\n\n"
                                                 f"**Magnet:**\n`{torrentList[i]['Magnet']}`\n\n",
                                    parse_mode="Markdown"
                                ),
                                reply_markup=InlineKeyboardMarkup(
                                    [[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="!tp ")]])
                            )
                        )
                else:
                    pass
    elif search_ts.startswith("!l"):
        query = search_ts.split(" ", 1)[-1]
        if (query == "") or (query == " "):
            answers.append(
                InlineQueryResultArticle(
                    title="!l [text]",
                    description="Search For Torrent in TorrentProject...",
                    input_message_content=InputTextMessageContent(
                        message_text="`!l [text]`\n\nSearch TorrentProject from Inline!",
                        parse_mode="Markdown"
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="!l ")]])
                )
            )
        else:
            torrentList = await SearchLime(query)
            if not torrentList:
                answers.append(
                    InlineQueryResultArticle(
                        title="No Torrents Found in LimeTorrent!",
                        description=f"Can't find torrents for '{query}'",
                        input_message_content=InputTextMessageContent(
                            message_text=f"No Torrents Found For `{query}`",
                            parse_mode="Markdown"
                        ),
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton("Try Again", switch_inline_query_current_chat="!l ")]])
                    )
                )
            else:
                if len(torrentList) > 20:
                   for i in range(20):
                        answers.append(
                            InlineQueryResultArticle(
                                title=f"{torrentList[i]['Name']}",
                                description=f"Seeders: {torrentList[i]['Seeders']}, Leechers: {torrentList[i]['Leechers']}\nSize: {torrentList[i]['Size']}",
                                input_message_content=InputTextMessageContent(
                                    message_text=f"**Category:** `{torrentList[i]['Category']}`\n"
                                                 f"**Name:** `{torrentList[i]['Name']}`\n"
                                                 f"**Size:** `{torrentList[i]['Size']}`\n"
                                                 f"**Seeders:** `{torrentList[i]['Seeders']}`\n"
                                                 f"**Leechers:** `{torrentList[i]['Leechers']}`\n"
                                                 f"**Uploaded about {torrentList[i]['Age']}**\n\n"
                                                 f"**Torrent:**\n`{torrentList[i]['Torrent']}`\n\n",
                                    parse_mode="Markdown"
                                ),
                                reply_markup=InlineKeyboardMarkup(
                                    [[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="!l ")]])
                            )
                        )
                else:
                    pass
    elif search_ts.startswith("!tf"):
        query = search_ts.split(" ", 1)[-1]
        if (query == "") or (query == " "):
            answers.append(
                InlineQueryResultArticle(
                    title="!tf [text]",
                    description="Search For Torrent in TorrentFunk...",
                    input_message_content=InputTextMessageContent(
                        message_text="`!tf [text]`\n\nSearch TorrentFunk from Inline!",
                        parse_mode="Markdown"
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="!tf ")]])
                )
            )
        else:
            torrentList = await SearchTorrentfunk(query)
            if not torrentList:
                answers.append(
                    InlineQueryResultArticle(
                        title="No Torrents Found in TorrentFunk!",
                        description=f"Can't find torrents for '{query}'",
                        input_message_content=InputTextMessageContent(
                            message_text=f"No Torrents Found For `{query}`",
                            parse_mode="Markdown"
                        ),
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton("Try Again", switch_inline_query_current_chat="!tf ")]])
                    )
                )
            else:
                if len(torrentList) > 20:
                   for i in range(20):
                        answers.append(
                            InlineQueryResultArticle(
                                title=f"{torrentList[i]['Name']}",
                                description=f"Seeders: {torrentList[i]['Seeders']}, Leechers: {torrentList[i]['Leechers']}\nSize: {torrentList[i]['Size']}",
                                input_message_content=InputTextMessageContent(
                                    message_text=f"**Name:** `{torrentList[i]['Name']}`\n"
                                                 f"**Size:** `{torrentList[i]['Size']}`\n"
                                                 f"**Seeders:** `{torrentList[i]['Seeders']}`\n"
                                                 f"**Leechers:** `{torrentList[i]['Leechers']}`\n"
                                                 f"**Uploaded By {torrentList[i]['Uploader']}**\n"
                                                 f"**Uploaded on {torrentList[i]['DateUploaded']} ago**\n\n"
                                                 f"**Torrent:**\n`{torrentList[i]['Torrent']}`\n\n",
                                    parse_mode="Markdown"
                                ),
                                reply_markup=InlineKeyboardMarkup(
                                    [[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="!tf ")]])
                            )
                        )
                else:
                    pass
    elif search_ts.startswith("!e"):
        query = search_ts.split(" ", 1)[-1]
        if (query == "") or (query == " "):
            answers.append(
                InlineQueryResultArticle(
                    title="!e [text]",
                    description="Search For Torrent in EzTV...",
                    input_message_content=InputTextMessageContent(
                        message_text="`!e [text]`\n\nSearch EzTV from Inline!",
                        parse_mode="Markdown"
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="!e ")]])
                )
            )
        else:
            torrentList = await SearchEztv(query)
            if not torrentList:
                answers.append(
                    InlineQueryResultArticle(
                        title="No Torrents Found in EzTV!",
                        description=f"Can't find torrents for '{query}'",
                        input_message_content=InputTextMessageContent(
                            message_text=f"No Torrents Found For `{query}`",
                            parse_mode="Markdown"
                        ),
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton("Try Again", switch_inline_query_current_chat="!e ")]])
                    )
                )
            else:
                if len(torrentList) > 20:
                   for i in range(20):
                        answers.append(
                            InlineQueryResultArticle(
                                title=f"{torrentList[i]['Name']}",
                                description=f"Size: {torrentList[i]['Size']}",
                                input_message_content=InputTextMessageContent(
                                    message_text=f"**Name:** `{torrentList[i]['Name']}`\n"
                                                 f"**Size:** `{torrentList[i]['Size']}`\n"
                                                 f"**Uploaded about {torrentList[i]['DateUploaded']} ago**\n\n"
                                                 f"**Torrent:** `{torrentList[i]['Torrent']}`\n\n"
                                                 f"**Magnet:**\n`{torrentList[i]['Magnet']}`\n\n",
                                    parse_mode="Markdown"
                                ),
                                reply_markup=InlineKeyboardMarkup(
                                    [[InlineKeyboardButton(
                                        "Search Again", switch_inline_query_current_chat="!e ")]]
                                )
                            )
                        )
                else:
                    pass
    elif search_ts.startswith("!r"):
        query = search_ts.split(" ", 1)[-1]
        if (query == "") or (query == " "):
            answers.append(
                InlineQueryResultArticle(
                    title="!r [text]",
                    description="Search For Torrent in Rarbg...",
                    input_message_content=InputTextMessageContent(
                        message_text="`!r [text]`\n\nSearch Rarbg from Inline!",
                        parse_mode="Markdown"
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="!r ")]])
                )
            )
        else:
            torrentList = await SearchRarbg(query)
            if not torrentList:
                answers.append(
                    InlineQueryResultArticle(
                        title="No Torrents Found in Rarbg!",
                        description=f"Can't find torrents for '{query}'",
                        input_message_content=InputTextMessageContent(
                            message_text=f"No Torrents Found For `{query}`",
                            parse_mode="Markdown"
                        ),
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton("Try Again", switch_inline_query_current_chat="!r ")]])
                    )
                )
            else:
                for i in range(len(torrentList)):
                        answers.append(
                            InlineQueryResultArticle(
                                title=f"{torrentList[i]['Name']}",
                                description=f"Seeders: {torrentList[i]['Seeders']}, Leechers: {torrentList[i]['Leechers']}\nSize: {torrentList[i]['Size']}",
                                input_message_content=InputTextMessageContent(
                                    message_text=f"**Category:** `{torrentList[i]['Category']}`\n"
                                                 f"**Name:** `{torrentList[i]['Seeders']}`\n"
                                                 f"**Size:** `{torrentList[i]['Size']}`\n"
                                                 f"**Seeders:** `{torrentList[i]['Seeders']}`\n"
                                                 f"**Leechers:** `{torrentList[i]['Leechers']}`\n"
                                                 f"**Uploaded By:** `{torrentList[i]['UploadedBy']}`\n"
                                                 f"**Uploaded {torrentList[i]['DateUploaded']}**\n\n",
                                    parse_mode="Markdown",
                                    disable_web_page_preview=True
                                ),
                                reply_markup=InlineKeyboardMarkup(
                                    [[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="!r ")]]),
                                thumb_url=torrentList[i]["Poster"]
                            )
                        )
    elif search_ts.startswith("!x"):
        query = search_ts.split(" ", 1)[-1]
        if (query == "") or (query == " "):
            answers.append(
                InlineQueryResultArticle(
                    title="!x [text]",
                    description="Search For Torrent in 1337X",
                    input_message_content=InputTextMessageContent(
                        message_text="`!x [text]`\n\nSearch 1337X from Inline!",
                        parse_mode="Markdown"
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="!x ")]])
                )
            )
        else:
            torrentList = await Search1337x(query)
            if not torrentList:
                answers.append(
                    InlineQueryResultArticle(
                        title="No Torrents Found in 1337X!",
                        description=f"Can't find torrents for '{query}'",
                        input_message_content=InputTextMessageContent(
                            message_text=f"No Torrents Found For `{query}`",
                            parse_mode="Markdown"
                        ),
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton("Try Again", switch_inline_query_current_chat="!x ")]])
                    )
                )
            else:
                for i in range(len(torrentList)):
                        answers.append(
                            InlineQueryResultArticle(
                                title=f"{torrentList[i]['Name']}",
                                description=f"Seeders: {torrentList[i]['Seeders']}, Leechers: {torrentList[i]['Leechers']}\nSize: {torrentList[i]['Size']}, Downloads: {torrentList[i]['Downloads']}",
                                input_message_content=InputTextMessageContent(
                                    message_text=f"**Category:** `{torrentList[i]['Category']}`\n"
                                                 f"**Name:** `{torrentList[i]['Name']}`\n"
                                                 f"**Language:** `{torrentList[i]['Language']}`\n"
                                                 f"**Seeders:** `{torrentList[i]['Seeders']}`\n"
                                                 f"**Leechers:** `{torrentList[i]['Leechers']}`\n"
                                                 f"**Size:** `{torrentList[i]['Size']}`\n"
                                                 f"**Downloads:** `{torrentList[i]['Downloads']}`\n"
                                                 f"__Uploaded by {torrentList[i]['UploadedBy']}__\n"
                                                 f"__Uploaded {torrentList[i]['DateUploaded']}__\n"
                                                 f"__Last Checked {torrentList[i]['LastChecked']}__\n\n"
                                                 f"**Magnet:**\n`{torrentList[i]['Magnet']}`\n\n",
                                    parse_mode="Markdown",
                                    disable_web_page_preview=True
                                ),
                                reply_markup=InlineKeyboardMarkup(
                                    [[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="")]]),
                                thumb_url=torrentList[i]["Poster"]
                            )
                        )
    elif search_ts.startswith("!y"):
        query = search_ts.split(" ", 1)[-1]
        if (query == "") or (query == " "):
            answers.append(
                InlineQueryResultArticle(
                    title="!y [text]",
                    description="Search For Torrent in YTS ...",
                    input_message_content=InputTextMessageContent(
                        message_text="`!y [text]`\n\nSearch YTS Torrents from Inline!",
                        parse_mode="Markdown"
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="!y ")]])
                )
            )
        else:
            torrentList = await SearchYTS(query)
            if not torrentList:
                answers.append(
                    InlineQueryResultArticle(
                        title="No Torrents Found!",
                        description=f"Can't find YTS torrents for {query}!",
                        input_message_content=InputTextMessageContent(
                            message_text=f"No YTS Torrents Found For `{query}`",
                            parse_mode="Markdown"
                        ),
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton("Try Again", switch_inline_query_current_chat="!y ")]])
                    )
                )
            else:
                for i in range(len(torrentList)):
                    dl_links = "- " + "\n\n- ".join(torrentList[i]['Downloads'])
                    answers.append(
                        InlineQueryResultArticle(
                            title=f"{torrentList[i]['Name']}",
                            description=f"Language: {torrentList[i]['Language']}\nLikes: {torrentList[i]['Likes']}, Rating: {torrentList[i]['Rating']}",
                            input_message_content=InputTextMessageContent(
                                message_text=f"**Genre:** `{torrentList[i]['Genre']}`\n"
                                             f"**Name:** `{torrentList[i]['Name']}`\n"
                                             f"**Language:** `{torrentList[i]['Language']}`\n"
                                             f"**Likes:** `{torrentList[i]['Likes']}`\n"
                                             f"**Rating:** `{torrentList[i]['Rating']}`\n"
                                             f"**Duration:** `{torrentList[i]['Runtime']}`\n"
                                             f"**Released on {torrentList[i]['ReleaseDate']}**\n\n"
                                             f"**Torrent Download Links:**\n{dl_links}\n\n",
                                parse_mode="Markdown",
                                disable_web_page_preview=True
                            ),
                            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="!y ")]]),
                            thumb_url=torrentList[i]["Poster"]
                        )
                    )
    elif search_ts.startswith("!a"):
        query = search_ts.split(" ", 1)[-1]
        if (query == "") or (query == " "):
            answers.append(
                InlineQueryResultArticle(
                    title="!a [text]",
                    description="Search For Torrents for Anime ...",
                    input_message_content=InputTextMessageContent(
                        message_text="`!a [text]`\n\nSearch Anime Torrents from Inline!",
                        parse_mode="Markdown"
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="!a ")]])
                )
            )
        else:
            torrentList = await SearchAnime(query)
            if not torrentList:
                answers.append(
                    InlineQueryResultArticle(
                        title="No Torrents Found in NyaaSI!",
                        description=f"Can't find torrents for '{query}'",
                        input_message_content=InputTextMessageContent(
                            message_text=f"No Torrents Found For `{query}`",
                            parse_mode="Markdown"
                        ),
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton("Try Again", switch_inline_query_current_chat="!a ")]])
                    )
                )
            else:
                if len(torrentList) > 20:
                    for i in range(20):
                        answers.append(
                            InlineQueryResultArticle(
                                title=f"{torrentList[i]['Name']}",
                                description=f"Seeders: {torrentList[i]['Seeder']}, Leechers: {torrentList[i]['Leecher']}\nSize: {torrentList[i]['Size']}",
                                input_message_content=InputTextMessageContent(
                                    message_text=f"**Category:** `{torrentList[i]['Category']}`\n"
                                                 f"**Name:** `{torrentList[i]['Name']}`\n"
                                                 f"**Seeders:** `{torrentList[i]['Seeder']}`\n"
                                                 f"**Leechers:** `{torrentList[i]['Leecher']}`\n"
                                                 f"**Size:** `{torrentList[i]['Size']}`\n"
                                                 f"**Upload Date:** `{torrentList[i]['Date']}`\n\n"
                                                 f"**Magnet:** \n`{torrentList[i]['Magnet']}`\n\n",
                                    parse_mode="Markdown"
                                ),
                                reply_markup=InlineKeyboardMarkup(
                                    [[InlineKeyboardButton(
                                        "Search Again", switch_inline_query_current_chat="!a ")]]
                                )
                            )
                        )
                    else:
                        pass               
    else:
        torrentList = await SearchGalaxy(search_ts)
        if not torrentList:
            answers.append(
                InlineQueryResultArticle(
                    title="No Torrents Found!",
                    description=f"Can't find torrents for {search_ts}!",
                    input_message_content=InputTextMessageContent(
                        message_text=f"No Torrents Found For `{search_ts}`!",
                        parse_mode="Markdown"
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton("Try Again", switch_inline_query_current_chat="")]])
                )
            )
        else:
            for i in range(len(torrentList)):
                answers.append(
                    InlineQueryResultArticle(
                        title=f"{torrentList[i]['Name']}",
                        description=f"Seeders: {torrentList[i]['Seeders']}, Leechers: {torrentList[i]['Leechers']}\nSize: {torrentList[i]['Size']}",
                        input_message_content=InputTextMessageContent(
                            message_text=f"**Category:** `{torrentList[i]['Category']}`\n"
                                         f"**Name:** `{torrentList[i]['Seeders']}`\n"
                                         f"**Size:** `{torrentList[i]['Size']}`\n"
                                         f"**Seeders:** `{torrentList[i]['Seeders']}`\n"
                                         f"**Leechers:** `{torrentList[i]['Leechers']}`\n"
                                         f"**Uploaded By:** `{torrentList[i]['UploadedBy']}`\n"
                                         f"**Uploaded {torrentList[i]['DateUploaded']}**\n\n"
                                         f"**Torrent:** `{torrentList[i]['Torrent']}`\n\n"
                                         f"**Magnet:**\n`{torrentList[i]['Magnet']}`\n\n",
                            parse_mode="Markdown",
                            disable_web_page_preview=True
                        ),
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="")]]
                        ),
                        thumb_url=torrentList[i]['Poster']
                    )
                )
    try:
        await inline.answer(
            results=answers,
            cache_time=0
        )
        print(
            f"[{Config.SESSION_NAME}] - Answered Successfully - {inline.from_user.first_name}")
    except QueryIdInvalid:
        print(
            f"[{Config.SESSION_NAME}] - Failed to Answer - {inline.from_user.first_name} - Sleeping for 5s")
        await asyncio.sleep(5)
        try:
            await inline.answer(
                results=answers,
                cache_time=0,
                switch_pm_text="Error: Search timed out!",
                switch_pm_parameter="start",
            )
        except QueryIdInvalid:
            print(
                f"[{Config.SESSION_NAME}] - Failed to Answer Error - {inline.from_user.first_name} - Sleeping for 5s")
            await asyncio.sleep(5)


TorrentBot.run()
