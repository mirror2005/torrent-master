# (c) @AbirHasan2005
# Scrappers

import aiohttp
#from configs import Config
from requests.utils import requote_uri

API_1337x = "https://api.abirhasan.wtf/1337x?query={}&limit={}"
API_YTS = "https://api.abirhasan.wtf/yts?query={}&limit={}"
API_PIRATEBAY = "https://dev.abirxo.cf/piratebay/{}"
API_ANIME = "https://dev.abirxo.cf/nyaasi/{}"
API_LIME = "https://dev.abirxo.cf/limetorrent/{}"
API_RARBG = "https://dev.abirxo.cf/rarbg/{}"
API_GALAXY = "https://dev.abirxo.cf/galaxy/{}"
API_TORLOCK = "https://dev.abirxo.cf/torlock/{}"
API_EZTV = "https://dev.abirxo.cf/eztv/{}"
API_KICK = "https://dev.abirxo.cf/kickass/{}"
API_ZOOQLE = "https://dev.abirxo.cf/zooqle/{}"
API_BIT = "https://dev.abirxo.cf/bitsearch/{}"
API_GLODLS = "https://dev.abirxo.cf/glodls/{}"
API_MAGDLS = "https://dev.abirxo.cf/magnetdl/{}"
API_FUNK = "https://dev.abirxo.cf/torrentfunk/{}"
API_TPRO = "https://dev.abirxo.cf/torrentproject/{}"
API_TZ = "https://dev.abirxo.cf/torrentz/{}"
API_PH = "https://appsdev.cyou/xv-ph-rt/api/?site_id=pornhub&video_id={}"
API_XVID = "https://appsdev.cyou/xv-ph-rt/api/?site_id=xvideos&video_id={}"
API_RT = "https://appsdev.cyou/xv-ph-rt/api/?site_id=redtube&video_id={}"

async def SearchPH(query: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(requote_uri(API_PH.format(query))) as res:
            return (await res.json())["mp4"] if ((await res.json()).get("mp4", None) is not None) else []

async def SearchXVID(query: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(requote_uri(API_PH.format(query))) as res:
            return (await res.json())["mp4"] if ((await res.json()).get("mp4", None) is not None) else []
        
async def SearchRT(query: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(requote_uri(API_PH.format(query))) as res:
            return (await res.json())["mp4"] if ((await res.json()).get("mp4", None) is not None) else []

async def Search1337x(query: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(requote_uri(API_1337x.format(query, 50))) as res:
            return (await res.json())["results"] if ((await res.json()).get("results", None) is not None) else []

async def SearchYTS(query: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(requote_uri(API_YTS.format(query, 50))) as res:
            return (await res.json())["results"] if ((await res.json()).get("results", None) is not None) else []

async def SearchPirateBay(query: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(requote_uri(API_PIRATEBAY.format(query))) as res:
            return (await res.json()) if ((await res.json()) is not None) else []

async def SearchAnime(query: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(requote_uri(API_ANIME.format(query))) as res:
            return (await res.json()) if ((await res.json()) is not None) else []

async def SearchLime(query: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(requote_uri(API_LIME.format(query))) as res:
            return (await res.json()) if ((await res.json()) is not None) else []
        
async def SearchRarbg(query: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(requote_uri(API_RARBG.format(query))) as res:
            return (await res.json()) if ((await res.json()) is not None) else []
        
async def SearchGalaxy(query: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(requote_uri(API_GALAXY.format(query))) as res:
            return (await res.json()) if ((await res.json()) is not None) else []
        
async def SearchTorlock(query: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(requote_uri(API_TORLOCK.format(query))) as res:
            return (await res.json()) if ((await res.json()) is not None) else []
        
async def SearchEztv(query: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(requote_uri(API_EZTV.format(query))) as res:
            return (await res.json()) if ((await res.json()) is not None) else []
        
async def SearchKickass(query: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(requote_uri(API_KICK.format(query))) as res:
            return (await res.json()) if ((await res.json()) is not None) else []       
        
async def SearchZooqle(query: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(requote_uri(API_ZOOQLE.format(query))) as res:
            return (await res.json()) if ((await res.json()) is not None) else []
        
async def SearchBit(query: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(requote_uri(API_BIT.format(query))) as res:
            return (await res.json()) if ((await res.json()) is not None) else []
        
async def SearchGlodls(query: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(requote_uri(API_GLODLS.format(query))) as res:
            return (await res.json()) if ((await res.json()) is not None) else []
        
async def SearchMagnetdl(query: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(requote_uri(API_MAGDLS.format(query))) as res:
            return (await res.json()) if ((await res.json()) is not None) else []
        
async def SearchTorrentfunk(query: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(requote_uri(API_FUNK.format(query))) as res:
            return (await res.json()) if ((await res.json()) is not None) else []
               
async def SearchTpro(query: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(requote_uri(API_TPRO.format(query))) as res:
            return (await res.json()) if ((await res.json()) is not None) else []
        
async def SearchTorrentz(query: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(requote_uri(API_TZ.format(query))) as res:
            return (await res.json()) if ((await res.json()) is not None) else []
