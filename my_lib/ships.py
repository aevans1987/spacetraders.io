import requests, json
from dotenv import load_dotenv
import os
load_dotenv()

agent = os.getenv("AGENT")
account = os.getenv("ACCOUNT")
url_base = os.getenv("URL_BASE")
headers = { "Authorization": f"Bearer {agent}" }

def get_ships(page = 1, limit = 10):
    result = requests.get(f"{url_base}/my/ships?page={page}&limit={limit}", headers = headers)
    if result.status_code == 200:
        return json.loads(result.content)['data']