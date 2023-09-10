import requests


async def check_telegram_connectivity():
    ping_url = 'https://google.com'
    try:
        response = requests.get(ping_url)
        if response.status_code == 200:
            # print(response.status_code)
            return 200
    except Exception as ex:
        pass
# import asyncio
#
# asyncio.run(check_telegram_connectivity())