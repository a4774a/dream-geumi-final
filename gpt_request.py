import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_gpt_dream(dream_text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "당신은 한국 전통 해몽 전문가입니다."},
            {"role": "user", "content": f"""
'{dream_text}' 라는 꿈을 한국 전통 해몽 전문가처럼 해석해줘.

- 500자 이상으로 상세하고 구체적으로 설명해줘.
- 등장한 상징, 감정, 배경 등을 분석해줘.
- 긍정적인 해석과 함께 주의해야 할 점도 알려줘.
- 이해하기 쉬운 문장으로 써줘.
"""}
        ]
    )
    return response.choices[0].message.content
