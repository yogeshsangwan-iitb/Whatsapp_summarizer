import os

# 1. Ask Python where it thinks it is running
print("--- DIAGNOSTIC START ---")
current_folder = os.getcwd()
print(f"Python is working in: {current_folder}")

# 2. Ask Python what files it sees in this folder
files_seen = os.listdir()
print(f"Files found: {files_seen}")

# 3. Check specifically for .env
if ".env" in files_seen:
    print("SUCCESS: Python sees the .env file!")
    
    # Let's peek inside (without printing the whole key for security)
    with open(".env", "r") as f:
        content = f.read().strip()
        if "GEMINI_API_KEY=" in content:
            print("SUCCESS: The file contains the correct variable name.")
        else:
            print("ISSUE: The file exists, but I don't see 'GEMINI_API_KEY=' inside.")
            print(f"File content is actually: {content}")
else:
    print("FAILURE: Python does NOT see .env. It sees: " + str(files_seen))

print("--- DIAGNOSTIC END ---")