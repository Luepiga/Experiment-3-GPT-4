
import requests

def generate_reply(email, previous_reply):
    prompt = f"""
Write a professional customer service email reply.
Use the previous reply as a reference, not as a
guaranteed statement about the current case.
Do not invent order status, refunds, or actions taken.

Customer email:
{email}

Previous reply for reference:
{previous_reply}

Write only the email reply.
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "qwen2.5:3b",
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )
        response.raise_for_status()
        return response.json()["response"].strip()

    except requests.RequestException as e:
        print("Reply generation error:", e)
        return "Dear Customer,\n\nThank you for contacting us. We will review your concern and assist you shortly.\n\nRegards,\nSupport Team"
