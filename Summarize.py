import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-2.0-flash')

print("---Whatsapp chat summarizer---")
filename = input("Enter the name of your chat file (press enter for 'chat.txt'): ").strip()
if filename == "":
    filename = "chat.txt"

try:
    with open(filename, "r", encoding="utf-8") as f:
        chat_content = f.read()
        print(f"\nSuccessfully read {len(chat_content)} characters from the chat.")
except FileNotFoundError:
    print(f"Error: no file '{filename}")        
    exit()

prompt = f"""
You are an expert assistant. I am providing you with a WhatsApp chat log.
Please analyze it and provide a summary following this exact structure:

1. **Summary**: A short paragraph summarizing the conversation.
2. **Key Points**: Bullet points of the main topics discussed.
3. **Decisions/Actions**: List any decisions made or actions required.
4. **Tone**: Describe the overall mood (e.g., friendly, angry, business-like).

Here is the chat text:
{chat_content}
"""

print("Sending data to Gemini... (this might take a few seconds)")

try:
    response = model.generate_content(prompt)

    print("\n" + "="*40)
    print("  summary ")
    print("="*40 + "\n")
    print (response.text)
    print("\n" + "="*40)
          
except Exception as e:
    print(f"An error occurred while talking to Google: {e}")