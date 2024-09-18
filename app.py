import os

import google.generativeai as genai

from chat_bot import chat_bot

def main():
    genai.configure(api_key = os.environ['API_KEY'])
    model = genai.GenerativeModel("gemini-1.5-flash")
    chat_bot(model)

if __name__ == "__main__":
    main()
