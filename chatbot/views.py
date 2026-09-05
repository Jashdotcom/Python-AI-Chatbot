import os
import json


from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    api_key = api_key,
    base_url="https://openrouter.ai/api/v1"
)

def chat_page(request):
    return render(request, "chatbot/index.html")

@csrf_exempt
def chat_api(request):
    if request.method != "POST":
        return JsonResponse(
            {"error": "Only POST requests are allowed."},
            status = 405
        )

    try:
        data = json.loads(request.body)
        messages = data.get("messages", [])

        response = client.chat.completions.create(
            model="anthropic/claude-sonnet-4.6",
            messages = messages,
            max_tokens = 500
        )

        answer = response.choices[0].message.content

        return JsonResponse({
            "answer": answer
        })

    except Exception as e:
        return JsonResponse(
            {"error": "str(e)"},
            status = 500
        )