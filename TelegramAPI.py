from telethon import TelegramClient, events
import asyncio
from TelegramCred import api_id, api_hash, session
import CheckTConnectivity


async def main():
    # async with TelegramClient(session, api_id, api_hash) as client:
    #     me = await client.get_me()
    #     print(f"My info: {me.stringify()}")
    #     print(f"My username: {me.username}")
    #     print(f"My phone number: {me.phone}")
    #
    #     print("Dialogs:")
    #     async for dialog in client.iter_dialogs():
    #         print(f"{dialog.name} has ID {dialog.id}")

    status = await CheckTConnectivity.check_telegram_connectivity()
    print(status)

if __name__ == '__main__':
    asyncio.run(main())
