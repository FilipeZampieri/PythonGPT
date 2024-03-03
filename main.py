from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "Listar apenas os nomes dos produtos, considerar descrição."
        },
        {
            "role": "user",
            "content": "Liste 3 produtos sustentáveis"
        }
    ],
    model="gpt-3.5-turbo",
    stream=False
)
print(response.choices[0].message.content)