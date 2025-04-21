import discord
from discord.ext import commands
import requests
import datetime
import os
import time
from duckduckgo_search import DDGS

BOT_VERSION = "1.0.0"
START_TIME = time.time()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)
# === Utility Functions ===
def format_search_results(results, query):
    message = f"**Results for `{query}`:**\n\n"
    for i, res in enumerate(results, 1):
        message += f"**{i}. [{res['title']}]({res['url']})**\n> {res['snippet'][:200]}...\n\n"
        if len(message) > 1900:
            message += "...(truncated)"
            break
    return message

def duck_search(query, max_results=5):
    with DDGS() as ddgs:
        return [
            {
                "title": r.get("title", "No Title"),
                "url": r.get("href", "No URL"),
                "snippet": r.get("body", "")
            } for r in ddgs.text(query, region='wt-wt', safesearch='Off', max_results=max_results)
        ]

# === Bot Events ===
@bot.event
async def on_ready():
    print(f"🤖 Logged in as {bot.user}")

# === Basic Commands ===
@bot.command()
async def help(ctx):
    commands_list = """
    **📚 Available Commands:**
    `!search [query]` - Search DuckDuckGo
    `!lookup [query]` - Alias for search
    `!deepsearch [query]` - Extended search with more results
    `!image [query]` - Image search
    `!news [query]` - Search news results
    `!ytsearch [query]` - Search YouTube
    `!findvideo [query]` - Prioritize video sites
    `!findforum [query]` - Search forum sources
    `!archive [url]` - Check Wayback Machine
    `!log [note]` - Save a local research note
    `!ping` - Bot status check
    `!uptime` - Bot running time
    `!version` - Bot version
    """
    await ctx.send(commands_list)

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

@bot.command()
async def uptime(ctx):
    uptime_seconds = int(time.time() - START_TIME)
    await ctx.send(f"🕒 Uptime: {str(datetime.timedelta(seconds=uptime_seconds))}")

@bot.command()
async def version(ctx):
    await ctx.send(f"📦 Bot Version: `{BOT_VERSION}`")

# === Search Commands ===
@bot.command()
async def search(ctx, *, query):
    await ctx.send(f"🔍 Searching for `{query}`...")
    results = duck_search(query)
    if not results:
        await ctx.send("❌ No results found.")
        return
    await ctx.send(format_search_results(results, query))

@bot.command()
async def lookup(ctx, *, query):
    await search(ctx, query=query)

@bot.command()
async def deepsearch(ctx, *, query):
    await ctx.send(f"🔎 Deep searching for `{query}`...")
    results = duck_search(query, max_results=20)
    if not results:
        await ctx.send("❌ No deep results found.")
        return
    await ctx.send(format_search_results(results, query))

@bot.command()
async def image(ctx, *, query):
    with DDGS() as ddgs:
        images = ddgs.images(query, max_results=3)
        if not images:
            await ctx.send("❌ No images found.")
            return
        for img in images:
            await ctx.send(img['image'])

@bot.command()
async def news(ctx, *, query):
    with DDGS() as ddgs:
        news = ddgs.news(query, max_results=5)
        if not news:
            await ctx.send("❌ No news found.")
            return
        for item in news:
            await ctx.send(f"📰 [{item['title']}]({item['url']})")

@bot.command()
async def ytsearch(ctx, *, query):
    results = duck_search(f"site:youtube.com {query}")
    await ctx.send(format_search_results(results, query))

@bot.command()
async def findvideo(ctx, *, query):
    results = duck_search(f"site:youtube.com OR site:vimeo.com OR site:dailymotion.com {query}")
    await ctx.send(format_search_results(results, query))

@bot.command()
async def findforum(ctx, *, query):
    results = duck_search(f"site:reddit.com OR site:4chan.org OR site:forums.net {query}")
    await ctx.send(format_search_results(results, query))

# === Archive & Logging ===
@bot.command()
async def archive(ctx, url):
    wayback = f"http://archive.org/wayback/available?url={url}"
    r = requests.get(wayback).json()
    snapshots = r.get("archived_snapshots", {})
    if "closest" in snapshots:
        await ctx.send(f"📦 Archived: {snapshots['closest']['url']}")
    else:
        await ctx.send("❌ No archive found for that URL.")

@bot.command()
async def log(ctx, *, note):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] {note}\n"
    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(log_line)
    await ctx.send("📝 Note logged.")

# === Start Bot ===
bot.run("TOKEN_HERE")
