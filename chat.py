from google import genai
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
chat = client.chats.create(model="gemini-2.0-flash") 

def chat_bot(prompt): 
    response = chat.send_message(f"Jawab pertanyaanku {prompt}")
    return response.text 

# input_text = input("chat: ")
# print(input_text)
# print(chat_bot(input_text))

