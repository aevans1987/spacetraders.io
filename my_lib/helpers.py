import requests, json
from dotenv import load_dotenv
import os
load_dotenv()

agent = os.getenv("AGENT")
account = os.getenv("ACCOUNT")
url_base = os.getenv("URL_BASE")

def get_agent():
    headers = { "Authorization": f"Bearer {agent}" }

    result = requests.get(f"{url_base}/my/agent", headers = headers)
    return json.loads(result.content)