# import os

# apikey = os.getenv("API_KEY")

# print(apikey)

import os

from dotenv import load_dotenv
load_dotenv()
print(os.getenv("API_KEY"))