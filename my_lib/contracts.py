import requests, json
from dotenv import load_dotenv
import os
load_dotenv()

agent = os.getenv("AGENT")
account = os.getenv("ACCOUNT")
url_base = os.getenv("URL_BASE")
headers = { "Authorization": f"Bearer {agent}" }

def get_contracts(page = 1, limit = 10, contract_id = None):
    if not contract_id:
        result = requests.get(f"{url_base}/my/contracts?page={page}&limit={limit}", headers = headers)
        if result.status_code == 200:
            return json.loads(result.content)['data']
    else:
        result = requests.get(f"{url_base}/my/contracts/{contract_id}", headers = headers)
        if result.status_code == 200:
            return json.loads(result.content)['data']

def post_accept_contract(contract_id):
        result = requests.post(f"{url_base}/my/contracts/{contract_id}/accept", headers = headers)
        if result.status_code == 200:
            return json.loads(result.content)['data']