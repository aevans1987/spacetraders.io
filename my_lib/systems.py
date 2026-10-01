import requests, json
from dotenv import load_dotenv
import os
load_dotenv()

agent = os.getenv("AGENT")
account = os.getenv("ACCOUNT")
url_base = os.getenv("URL_BASE")
headers = { "Authorization": f"Bearer {agent}" }

def get_systems(system = None):
        if not system:
            result = requests.get(f"{url_base}/systems", headers = headers)
            return json.loads(result.content)
        else:
            result = requests.get(f"{url_base}/systems/{system}", headers = headers)
            return json.loads(result.content)