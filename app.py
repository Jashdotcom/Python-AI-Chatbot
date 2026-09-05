import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("sk-370db56b232a19ba-b3323f-f292ea80")

print(api_key)