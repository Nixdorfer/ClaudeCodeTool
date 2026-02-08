#!/usr/bin/env python3
import sys
import asyncio
import json

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("Error: playwright not installed. Run: pip install playwright && playwright install chromium", file=sys.stderr)
    sys.exit(1)

async def fetch_spa_content(url, wait_time=5000, scroll=True):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.set_viewport_size({"width": 1920, "height": 1080})
        await page.goto(url, wait_until="networkidle", timeout=60000)
        start_time = asyncio.get_event_loop().time()
        while asyncio.get_event_loop().time() - start_time < 30:
            has_content = await page.evaluate('''() => {
                const article = document.querySelector('article, .markdown-body, main');
                const tables = document.querySelectorAll('table');
                const text = document.body.innerText;
                return (article && article.innerText.length > 500) || tables.length > 0 || text.length > 2000;
            }''')
            if has_content:
                break
            await asyncio.sleep(0.5)
        if scroll:
            await page.evaluate('''async () => {
                await new Promise((resolve) => {
                    let totalHeight = 0;
                    const distance = 500;
                    const timer = setInterval(() => {
                        const scrollHeight = document.body.scrollHeight;
                        window.scrollBy(0, distance);
                        totalHeight += distance;
                        if (totalHeight >= scrollHeight) {
                            clearInterval(timer);
                            window.scrollTo(0, 0);
                            resolve();
                        }
                    }, 100);
                });
            }''')
        await page.wait_for_timeout(wait_time)
        html = await page.evaluate('''() => {
            const clone = document.documentElement.cloneNode(true);
            clone.querySelectorAll('script, style, noscript, svg, img, iframe, link[rel="stylesheet"], video, audio, canvas, picture, source').forEach(el => el.remove());
            clone.querySelectorAll('[style]').forEach(el => el.removeAttribute('style'));
            clone.querySelectorAll('[onclick], [onload], [onerror]').forEach(el => {
                el.removeAttribute('onclick');
                el.removeAttribute('onload');
                el.removeAttribute('onerror');
            });
            return clone.outerHTML;
        }''')
        await browser.close()
        return html

def main():
    if len(sys.argv) < 2:
        print("Usage: python fetch_spa.py <URL> [--wait <ms>] [--no-scroll]", file=sys.stderr)
        sys.exit(1)
    url = sys.argv[1]
    wait_time = 5000
    scroll = True
    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == "--wait" and i + 1 < len(sys.argv):
            wait_time = int(sys.argv[i + 1])
            i += 2
        elif sys.argv[i] == "--no-scroll":
            scroll = False
            i += 1
        else:
            i += 1
    html = asyncio.run(fetch_spa_content(url, wait_time, scroll))
    print(html)

if __name__ == "__main__":
    main()
