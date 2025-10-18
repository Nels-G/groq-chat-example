from groq import Groq
from dotenv import load_dotenv
import os

# Charger la clé API depuis le fichier .env
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

client = Groq()

# Exemple de requête
completion = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "system", "content": "Tu es un assistant utile."},
        {"role": "user", "content": "Explique-moi ce qu’est Groq."}
    ],
    temperature=0.7,
    max_completion_tokens=256,
    stream=True
)

# Affichage de la réponse
for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
