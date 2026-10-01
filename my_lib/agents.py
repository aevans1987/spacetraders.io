import requests, json
from dotenv import load_dotenv
import os
load_dotenv()

agent = os.getenv("AGENT")
account = os.getenv("ACCOUNT")
url_base = os.getenv("URL_BASE")
headers = { "Authorization": f"Bearer {agent}" }

def get_agents(page = 1, limit =10):
    result = requests.get(f"{url_base}/agents?page={page}&limit={limit}")
    return json.loads(result.content)

def get_agent(symbol = ""):
    result = requests.get(f"{url_base}/agents/{symbol}", headers = headers)
    return json.loads(result.content)

def get_my_agent():
    result = requests.get(f"{url_base}/my/agent", headers = headers)
    return json.loads(result.content)

def get_my_agent_events():
    result = requests.get(f"{url_base}/my/agent/events", headers = headers)
    return json.loads(result.content)