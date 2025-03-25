import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_gpt_dream(dream_text):
    prompt = f"""
당신은 한국 전통 꿈해몽 전문가입니다.
다음 꿈을 해석해 주세요:

"{dream_text}"
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 또는 "gpt-4"
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.8,
        max_tokens=800
    )
    return response['choices'][0]['message']['content']
