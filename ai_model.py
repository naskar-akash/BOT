from openai import OpenAI
import os
from dotenv import load_dotenv
from system_message import system_prompt

# Load .env file
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_chatgpt(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content
    
    
    except Exception as e:
        print("ChatGPT Error:", e)
        return "Sorry, I couldn't process that."