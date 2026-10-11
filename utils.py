
from datetime import datetime
import os

def save_reply(name, email, reply, intent):
    os.makedirs("outputs", exist_ok=True)

    with open(
        "outputs/generated_reply.txt",
        "a",
        encoding="utf-8"
    ) as file:
        file.write("\n" + "=" * 50 + "\n")
        file.write("Customer Name: " + name + "\n")
        file.write("Customer Email: " + email + "\n")
        file.write("Generated Reply:\n" + reply + "\n")
        file.write("Intent: " + intent + "\n")
        file.write("Date: " + datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ) + "\n")

    print("Reply saved successfully!")
