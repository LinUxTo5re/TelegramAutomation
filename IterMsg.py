from telethon.sync import TelegramClient
from TelegramCred import api_id, api_hash, session
import asyncio
from telethon.tl.types import InputMessagesFilterUrl
import re

group_name = '793 Mega Pro Digital Marketing'
receptionist_name = ''
mission_dict = dict()
# Regular expression pattern to match YouTube URLs
youtube_url_pattern = r'https://www\.youtube\.com/'


async def get_messages():
    async with TelegramClient(session, api_id, api_hash) as client:
        # Find the group by name or username
        chats = await client.get_dialogs()
        target_group = None
        for chat in chats:
            if chat.title == group_name or chat.name == group_name:
                target_group = chat
                break
            # Check which participants are admins
        # participants = await client.get_participants(target_group)

        if target_group:
            # Retrieve messages from the group
            async for message in client.iter_messages(target_group, limit=1, filter=InputMessagesFilterUrl):
                filter_msg(message.text)


def filter_msg(message_text):
    # Regular expressions to extract the URL, next mission value, and current mission number
    url_pattern = r'https://[^\s]+'
    next_mission_pattern = r'The next mission is (\d{1,2}:\d{2})'
    current_mission_pattern = r'Mission: (\d+)'

    # Search for matches using the patterns
    url_match = re.search(url_pattern, message_text)
    next_mission_time = re.search(next_mission_pattern, message_text)
    current_mission_match = re.search(current_mission_pattern, message_text)

    try:
        # Extract and print the results
        if url_match:
            url = url_match.group(0).rstrip('*')
            if re.search(youtube_url_pattern, url):
                mission_dict['URL'] = url
            else:
                raise FileNotFoundError(f"{url} is not a YouTube link.")
        if next_mission_time:
            next_mission_value = next_mission_time.group(1)
            mission_dict['next_mission_time'] = next_mission_value

        if current_mission_match:
            current_mission_number = current_mission_match.group(1)
            mission_dict['Mission'] = current_mission_number
        print(mission_dict)
    except Exception as ex:
        pass


if __name__ == '__main__':
    asyncio.run(get_messages())
