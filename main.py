
tone_choice = input("Select tone: ").strip().lower()

tones = {
    "1": "Friendly",
    "2": "Formal",
    "3": "Empathetic",
    "friendly tone": "Friendly",
    "formal tone": "Formal",
    "empathetic tone": "Empathetic",
    "friendly": "Friendly",
    "formal": "Formal",
    "empathetic": "Empathetic"
}

if tone_choice in tones:
    reply = improve_tone(reply, tones[tone_choice])
    print("\n===== IMPROVED REPLY =====")
    print(reply)
else:
    print("Invalid tone choice.")
```

Save using **Ctrl + S** and restart:

```powershell
python main.py
```

Now you can enter either `1` or `Friendly Tone`.