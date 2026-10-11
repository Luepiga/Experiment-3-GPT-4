
import requests

def summarize_email(email):
    prompt = f"""
Summarize the customer's issue in exactly 50 words.
Do not add facts that are not in the email.

Customer email:
{email}

Return only the summary.
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
        summary = response.json()["response"].strip()

        words = summary.split()
        if len(words) != 50:
            print("Note: The AI returned", len(words), "words.")

        return summary

    except requests.RequestException as e:
        print("Summary error:", e)
        return "The customer has reported an issue and requests assistance from the support team."
