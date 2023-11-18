from helper.toko_apis import *
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

api_key = os.environ.get("API_KEY")

response = get_props(api_key,5)

print(response.text)


