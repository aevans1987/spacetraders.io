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
    if result.status_code == 200:
        return json.loads(result.content)['data']

def get_agent(symbol = ""):
    result = requests.get(f"{url_base}/agents/{symbol}", headers = headers)
    if result.status_code == 200:
        return json.loads(result.content)['data']

def get_my_agent():
    result = requests.get(f"{url_base}/my/agent", headers = headers)
    if result.status_code == 200:
        return json.loads(result.content)['data']

def get_my_agent_events():
    result = requests.get(f"{url_base}/my/agent/events", headers = headers)
    if result.status_code == 200:
        return json.loads(result.content)['data']