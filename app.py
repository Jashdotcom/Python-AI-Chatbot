import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    api_key = api_key,
    base_url="https://openrouter.ai/api/v1"
)

messages = []

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        print("\nAI: Goodbye!")
        break

    messages.append({
        "role": "user",
        "content": question
    })

    response = client.chat.completions.create(
        model="anthropic/claude-sonnet-4.6",
        messages = messages,
        max_tokens=500
    )
    answer = response.choices[0].message.content

    messages.append({
        "role": "assistant",
        "content": answer
    })
    print("\nAI: ", answer)


