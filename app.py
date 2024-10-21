import asyncio
from playwright.async_api import async_playwright

async def get_view_source():
    async with async_playwright() as p:
        # Launch browser in headless mode
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Navigate to the view-source URL of Google
        await page.goto('view-source:https://google.com')

        # Get the full page content (HTML source code)
        page_content = await page.content()

        # Print the source code
        print(page_content)

        # Close the browser
        await browser.close()

# Run the async function
asyncio.run(get_view_source())
