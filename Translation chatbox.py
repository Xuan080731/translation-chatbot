import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv('GOOGLE_API_KEY')

if not api_key:
    raise ValueError("未找到 GOOGLE_API_KEY,請確保在 .env 檔案中設定了GOOGLE_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.0-flash")  
response = model.generate_content("Write a story about a magic backpack.")
print(response.text)

def translate_text(text, target_language):
    prompt = f"Translate the following text to {target_language}: {text}"
    response = model.generate_content(prompt)
    return response.text

def chat_bot():
    print("Welcome to the translation chatbot!")
    print("Type 'exit' to quit.")

    target_language = input("Please specify the target language (e.g., French, Spanish, Chinese):")

    while True:
        user_input = input("Enter the text you want to translate:：")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        translation = translate_text(user_input, target_language)
        print(f"翻譯成 {target_language}：{translation}")

chat_bot()
