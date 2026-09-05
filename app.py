import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    api_key = api_key,
    base_url="https://openrouter.ai/api/v1"
)

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    response = client.chat.completions.create(
        model="anthropic/claude-sonnet-4.6",
        messages = [
            {
                "role": "user",
                "content": question
            }
        ],
        max_tokens=500
    )
    answer = response.choices[0].message.content
    print("\nAI: ", answer)


