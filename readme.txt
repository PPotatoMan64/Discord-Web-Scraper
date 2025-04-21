#🕵️ Media Scraper
Media Scraper is a robust, multipurpose Discord bot built specifically for lost media research, digital preservation, and internet sleuthing. Designed for researchers, enthusiasts, and archivists, the bot provides streamlined access to a suite of investigative tools — all within a Discord server.

With a single command, Media Scraper can search the web, fetch images, explore archived websites, and retrieve media or metadata from various sources, making it an essential companion for lost media communities, research groups, or anyone digging into the depths of the web.

# 🌐 Core Features
🔍 Web Search
Search the internet via DuckDuckGo for quick fact-checking, obscure info hunting, or lead generation. Offers both basic and extended search capabilities.

🖼️ Image Search
Pulls relevant image results for any keyword using DuckDuckGo's image API. Great for matching visual references, uncovering rare images, or identifying content.

🗞️ News & YouTube
Fetch the latest news articles or related YouTube videos for your query — useful for both recent events and media discovery.

🕰️ Wayback Machine Integration
Quickly lookup and preview archived pages from the Internet Archive (Wayback Machine), allowing you to explore defunct websites, capture historical context, or verify changes over time.

📜 Logging System
All queries are saved to a local log file for record-keeping, tracking, or collaborative research. You’ll never lose a good lead again.

# ⚒️ Commands Overview
bash
Copy
Edit
/search <query>         → DuckDuckGo web search
/deepsearch <query>     → Extended web search (with more results)
/image <query>          → Pulls image results
/news <query>           → Fetches news articles
/youtube <query>        → Gets YouTube video links
/wayback <url>          → Archive.org snapshot fetcher
/logs                   → Shows logged search queries
/ping                   → Measures bot latency
/uptime                 → Bot runtime since launch
/version                → Displays current version
/help                   → Lists all commands

# 📦 Installation
Clone the repository

bash
Copy
Edit
git clone https://github.com/yourusername/media-scraper.git
cd media-scraper
Install the dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set your bot token

Replace "TOKEN_HERE" in the Python file with your actual Discord bot token or set it via environment variable.

Run the bot

bash
Copy
Edit
python bot.py

# 🔍 How It Works
1. Discord Bot Framework
Media Scraper is built on discord.py, allowing it to receive and respond to slash commands and message inputs directly within a Discord server.

2. DuckDuckGo Integration
The bot uses the duckduckgo-search Python package for web, image, and news queries. Results are parsed and returned in a clean embed format for easy viewing in Discord.

3. Wayback Machine API
When given a URL, the bot sends a request to archive.org’s Wayback Machine to check for existing snapshots or redirects users to an archived copy of a page.

4. Logging System
Search inputs and query results are logged to local text files (logs/ directory) to help keep track of past lookups — perfect for research transparency and revisiting leads.

5. Fail-Safes & Timeouts
The bot has timeout handling and error catching for search failures, unreachable APIs, and rate limits to ensure smooth operation even during heavy use.

# 📄 License
This project is open source under the MIT License.
