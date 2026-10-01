from helpers import *

agent = os.getenv("AGENT")
account = os.getenv("ACCOUNT")
url_base = os.getenv("URL_BASE")

headers = { "Authorization": f"Bearer {agent}" }

result = requests.get(f"{url_base}/my/agent", headers = headers)
result_dict = json.loads(result.content)

#print(result_dict['data'])