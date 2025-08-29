import aiohttp
import asyncio
from dotenv import load_dotenv
import os
import urllib.parse
import webbrowser

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REFRESH_TOKEN = os.getenv('REFRESH_TOKEN')
REDIRECT_URI = "https://www.developers.strava.com"

def build_auth_url():
    params = {
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
        "approval_prompt": "auto",  # "force" if you want to always re-ask
        "scope": "activity:read_all"
    }

    auth_url = f"https://www.strava.com/oauth/authorize?{urllib.parse.urlencode(params)}"
    print("Open this URL in your browser to authorize:", auth_url)

    # Automatically open the browser
    webbrowser.open(auth_url)

build_auth_url()


async def refresh_access_token():
    url = "https://www.strava.com/api/v3/oauth/token"
    payload = {
        "client_id": {CLIENT_ID},
        "client_secret": {CLIENT_SECRET},
        "grant_type": "refresh_token",
        "refresh_token": {REFRESH_TOKEN},
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload) as resp:
            response_data = await resp.json()
            print(response_data)
            return response_data['access_token']

access_token = asyncio.run(refresh_access_token())


async def get_athlete():
    token = f"{access_token}"
    headers = {"Authorization": f"Bearer {token}"}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get('https://www.strava.com/api/v3/athlete') as resp:
            print(resp.status)
            print(await resp.text())

asyncio.run(get_athlete())


async def get_activities():
    url = "https://www.strava.com/api/v3/athlete/activities"
    token = f"{access_token}"
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "before": "",
        "after": "",
        "page": "",
        "per_page": ""
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, headers=headers) as resp:
            print(resp.status)
            print(await resp.text())

asyncio.run(get_activities())