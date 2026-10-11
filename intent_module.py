
import requests

def detect_intent(email):
    prompt = f"""
Classify this customer email into exactly one category:
Delivery Issue, Refund Request, Product Complaint,
Technical Support, Order Cancellation, General Inquiry.

Return only the category name.

Customer email: {email}
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
        result = response.json()["response"].strip()

        categories = [
            "Delivery Issue", "Refund Request",
            "Product Complaint", "Technical Support",
            "Order Cancellation", "General Inquiry"
        ]

        for category in categories:
            if category.lower() in result.lower():
                return category

        return "General Inquiry"

    except requests.RequestException as e:
        print("Ollama error:", e)
        return "General Inquiry"
