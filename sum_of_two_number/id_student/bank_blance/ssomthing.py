import asyncio
import aiohttp
from bs4 import BeautifulSoup

class AsyncWebCrawler:
    def __init__(self, urls):
        self.urls = urls

    async def fetch(self, session, url):
        try:
            async with session.get(url, timeout=10) as response:
                html = await response.text()
                return url, html
        except Exception as e:
            return url, f"Error: {e}"

    async def extract_title(self, session, url):
        url, html = await self.fetch(session, url)

        if html.startswith("Error:"):
            return {"url": url, "title": None, "error": html}

        soup = BeautifulSoup(html, "html.parser")
        title = soup.title.string.strip() if soup.title else "No Title"

        return {
            "url": url,
            "title": title,
            "error": None
        }

    async def crawl(self):
        async with aiohttp.ClientSession() as session:
            tasks = [
                self.extract_title(session, url)
                for url in self.urls
            ]
            return await asyncio.gather(*tasks)

async def main():
    urls = [
        "https://python.org",
        "https://github.com",
        "https://stackoverflow.com",
    ]

    crawler = AsyncWebCrawler(urls)
    results = await crawler.crawl()

    for result in results:
        print(f"URL   : {result['url']}")
        print(f"Title : {result['title']}")
        print("-" * 50)

if __name__ == "__main__":
    asyncio.run(main())