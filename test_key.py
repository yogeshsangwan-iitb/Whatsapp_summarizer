import os
# The import must be exactly this:
from dotenv import load_dotenv

# Force it to look in the current folder
load_dotenv(override=True)

api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    print(f"Success! Key found: {api_key[:4]}...") # Prints first 4 chars only
else:
    print("Error: Still cannot find the key.")