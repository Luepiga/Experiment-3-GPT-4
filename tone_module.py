
import requests

def improve_tone(reply, tone):
    prompt = f"""
Rewrite this customer service email in a {tone} tone.
Keep the meaning and important facts unchanged.
Return only the rewritten email.

Email:
{reply}
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
        print("Tone improvement error:", e)
        return reply
