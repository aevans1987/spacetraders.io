import requests
from dotenv import load_dotenv
import os
load_dotenv()

bearer = os.getenv("BEARER")
print(bearer)