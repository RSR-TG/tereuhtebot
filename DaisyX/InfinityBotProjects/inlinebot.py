#    Copyright (C) Midhun KM 2020-2021
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


import re
import urllib
from re import findall
from urllib.parse import quote

import requests
from pornhub_api import PornhubApi
from search_engine_parser import GoogleSearch
from telethon import Button, custom, events
from youtube_search import YoutubeSearch
from DaisyX import telethn as tgbot
from DaisyX.function import _deezer_dl, _ytdl


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"deezer_dl_(.*)")))
async def rip(event):
    sun = event.data_match.group(1).decode("UTF-8")
    await _deezer_dl(sun, event, tgbot)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"yt_vid_(.*)")))
async def rip(event):
    yt_dl_data = event.data_match.group(1).decode("UTF-8")
    link_s = yt_dl_data
    is_it = False
    await _ytdl(link_s, is_it, event, tgbot)


@tgbot.on(events.InlineQuery(pattern=r"torrent (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    testinput = event.pattern_match.group(1)
    starkisnub = urllib.parse.quote_plus(testinput)
    results = []
    sedlyf = "https://api.sumanjay.cf/torrent/?query=" + starkisnub
    try:
        okpro = requests.get(url=sedlyf, timeout=10).json()
    except:
        pass
    sed = len(okpro)
    if sed == 0:
        resultm = builder.article(
            title="No Results Found.",
            description="Check Your Spelling / Keyword",
            text="**Please, Search Again With Correct Keyword, Thank you !**",
            buttons=[
                [
                    Button.switch_inline(
                        "Search Again", query="torrent ", same_peer=True
                    )
                ],
            ],
        )
        await event.answer([resultm])
        return
    if sed > 30:
        for i in range(30):
            seds = okpro[i]["age"]
            okpros = okpro[i]["leecher"]
            sadstark = okpro[i]["magnet"]
            okiknow = okpro[i]["name"]
            starksize = okpro[i]["size"]
            starky = okpro[i]["type"]
            seeders = okpro[i]["seeder"]
            okayz = f"**Title :** `{okiknow}` \n**Size :** `{starksize}` \n**Type :** `{starky}` \n**Seeder :** `{seeders}` \n**Leecher :** `{okpros}` \n**Magnet :** `{sadstark}` "
            sedme = f"Size : {starksize} Type : {starky} Age : {seds}"
            results.append(
                await event.builder.article(
                    title=okiknow,
                    description=sedme,
                    text=okayz,
                    buttons=Button.switch_inline(
                        "Search Again", query="torrent ", same_peer=True
                    ),
                )
            )
    else:
        for sedz in okpro:
            seds = sedz["age"]
            okpros = sedz["leecher"]
            sadstark = sedz["magnet"]
            okiknow = sedz["name"]
            starksize = sedz["size"]
            starky = sedz["type"]
            seeders = sedz["seeder"]
            okayz = f"**Title :** `{okiknow}` \n**Size :** `{starksize}` \n**Type :** `{starky}` \n**Seeder :** `{seeders}` \n**Leecher :** `{okpros}` \n**Magnet :** `{sadstark}` "
            sedme = f"Size : {starksize} Type : {starky} Age : {seds}"
            results.append(
                await event.builder.article(
                    title=okiknow,
                    description=sedme,
                    text=okayz,
                    buttons=[
                        Button.switch_inline(
                            "Search Again", query="torrent ", same_peer=True
                        )
                    ],
                )
            )
    await event.answer(results)


@tgbot.on(events.InlineQuery(pattern=r"yt (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    testinput = event.pattern_match.group(1)
    urllib.parse.quote_plus(testinput)
    results = []
    moi = YoutubeSearch(testinput, max_results=9).to_dict()
    if not moi:
        resultm = builder.article(
            title="No Results Found.",
            description="Check Your Spelling / Keyword",
            text="**Please, Search Again With Correct Keyword, Thank you !**",
            buttons=[
                [Button.switch_inline("Search Again", query="yt ", same_peer=True)],
            ],
        )
        await event.answer([resultm])
        return
    for moon in moi:
        hmm = moon["id"]
        mo = f"https://www.youtube.com/watch?v={hmm}"
        kek = f"https://www.youtube.com/watch?v={hmm}"
        stark_name = moon["title"]
        stark_chnnl = moon["channel"]
        total_stark = moon["duration"]
        stark_views = moon["views"]
        moon["long_desc"]
        kekme = f"https://img.youtube.com/vi/{hmm}/hqdefault.jpg"
        okayz = f"**Title :** `{stark_name}` \n**Link :** `{kek}` \n**Channel :** `{stark_chnnl}` \n**Views :** `{stark_views}` \n**Duration :** `{total_stark}`"
        hmmkek = f"Video Name : {stark_name} \nChannel : {stark_chnnl} \nDuration : {total_stark} \nViews : {stark_views}"
        results.append(
            await event.builder.document(
                file=kekme,
                title=stark_name,
                description=hmmkek,
                text=okayz,
                include_media=True,
                buttons=[
                    [custom.Button.inline("Download Video - mp4", data=f"yt_vid_{mo}")],
                    [custom.Button.inline("Download Audio - mp3", data=f"yt_dla_{mo}")],
                    [Button.switch_inline("Search Again", query="yt ", same_peer=True)],
                ],
            )
        )
    await event.answer(results)


@tgbot.on(events.InlineQuery(pattern=r"jm (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    event.builder
    testinput = event.pattern_match.group(1)
    starkisnub = urllib.parse.quote_plus(testinput)
    results = []
    search = f"http://starkmusic.herokuapp.com/result/?query={starkisnub}"
    seds = requests.get(url=search).json()
    for okz in seds:
        okz["album"]
        okmusic = okz["music"]
        hmmstar = okz["perma_url"]
        singer = okz["singers"]
        hmm = okz["duration"]
        langs = okz["language"]
        hidden_url = okz["media_url"]
        okayz = (
            f"**Song Name :** `{okmusic}` \n**Singer :** `{singer}` \n**Song Url :** `{hmmstar}`"
            f"\n**Language :** `{langs}` \n**Download Able Url :** `{hidden_url}`"
            f"\n**Duration :** `{hmm}`"
        )
        hmmkek = (
            f"Song : {okmusic} Singer : {singer} Duration : {hmm} \nLanguage : {langs}"
        )
        results.append(
            await event.builder.article(
                title=okmusic,
                description=hmmkek,
                text=okayz,
                buttons=Button.switch_inline(
                    "Search Again", query="jm ", same_peer=True
                ),
            )
        )
    await event.answer(results)


@tgbot.on(events.InlineQuery(pattern=r"google (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    event.builder
    results = []
    match = event.pattern_match.group(1)
    page = findall(r"page=\d+", match)
    try:
        page = page[0]
        page = page.replace("page=", "")
        match = match.replace("page=" + page[0], "")
    except IndexError:
        page = 1

    search_args = (str(match), int(page))
    gsearch = GoogleSearch()
    gresults = await gsearch.async_search(*search_args)
    for i in range(len(gresults["links"])):
        try:
            title = gresults["titles"][i]
            link = gresults["links"][i]
            desc = gresults["descriptions"][i]
            okiknow = f"**GOOGLE - SEARCH** \n[{title}]({link})\n\n`{desc}`"
            results.append(
                await event.builder.article(
                    title=title,
                    description=desc,
                    text=okiknow,
                    buttons=[
                        Button.switch_inline(
                            "Search Again", query="google ", same_peer=True
                        )
                    ],
                )
            )
        except IndexError:
            break
    await event.answer(results)


@tgbot.on(events.InlineQuery(pattern=r"ph (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    event.builder
    results = []
    input_str = event.pattern_match.group(1)
    api = PornhubApi()
    data = api.search.search(input_str, ordering="mostviewed")
    ok = 1
    for vid in data.videos:
        if ok <= 5:
            lul_m = f"**PORN-HUB SEARCH** \n**Video title :** `{vid.title}` \n**Video link :** `https://www.pornhub.com/view_video.php?viewkey={vid.video_id}`"
            results.append(
                await event.builder.article(
                    title=vid.title,
                    text=lul_m,
                    buttons=[
                        Button.switch_inline(
                            "Search Again", query="ph ", same_peer=True
                        )
                    ],
                )
            )
        else:
            pass
    await event.answer(results)


@tgbot.on(events.InlineQuery(pattern=r"xkcd (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    input_str = event.pattern_match.group(1)
    xkcd_id = None
    if input_str:
        if input_str.isdigit():
            xkcd_id = input_str
        else:
            xkcd_search_url = "https://relevantxkcd.appspot.com/process?"
            queryresult = requests.get(
                xkcd_search_url, params={"action": "xkcd", "query": quote(input_str)}
            ).text
            xkcd_id = queryresult.split(" ")[2].lstrip("\n")
    if xkcd_id is None:
        xkcd_url = "https://xkcd.com/info.0.json"
    else:
        xkcd_url = "https://xkcd.com/{}/info.0.json".format(xkcd_id)
    r = requests.get(xkcd_url)
    if r.ok:
        data = r.json()
        year = data.get("year")
        month = data["month"].zfill(2)
        day = data["day"].zfill(2)
        xkcd_link = "https://xkcd.com/{}".format(data.get("num"))
        safe_title = data.get("safe_title")
        data.get("transcript")
        alt = data.get("alt")
        img = data.get("img")
        data.get("title")
        output_str = """
[XKCD]({})
Title: {}
Alt: {}
Day: {}
Month: {}
Year: {}""".format(
            xkcd_link, safe_title, alt, day, month, year
        )
        lul_k = builder.photo(file=img, text=output_str)
        await event.answer([lul_k])
    else:
        resultm = builder.article(title="- No Results :/ -", text=f"No Results Found !")
        await event.answer([resultm])


@tgbot.on(events.InlineQuery(pattern=r"deezer ?(.*)"))
async def inline_id_handler(event):
    event.buildernt.answer([resultm])
    results = []
    input_str = event.pattern_match.group(1)
    link = f"https://api.deezer.com/search?q={input_str}&limit=7"
    dato = requests.get(url=link).json()
    # data_s = json.loads(data_s)
    for match in dato.get("data"):
        ro = str(match.get("id"))
        hmm_m = f"Title : {match['title']} \nLink : {match['link']} \nDuration : {match['duration']} seconds \nBy : {match['artist']['name']}"
        results.append(
            await event.builder.document(
                file=match["album"]["cover_big"],
                title=match["title"],
                text=hmm_m,
                description=f"Artist: {match['artist']['name']}\nAlbum: {match['album']['title']}",
                buttons=[
                    [
                        custom.Button.inline(
                            "Download Audio - mp3", data=f"deezer_dl_{ro}"
                        )
                    ],
                ],
            ),
        )
    if results:
        try:
            await event.answer(results)
        except TypeError:
            pass
