import tweepy
import time
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import os

# CLAVES (cambia solo si quieres las tuyas propias)
API_KEY = "TU_API_KEY_AQUI"
API_SECRET = "TU_API_SECRET_AQUI"
ACCESS_TOKEN = "TU_ACCESS_TOKEN_AQUI"
ACCESS_TOKEN_SECRET = "TU_ACCESS_TOKEN_SECRET_AQUI"
BEARER_TOKEN = "TU_BEARER_TOKEN_AQUI"

client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

def crear_imagen(texto):
    img = Image.new('RGB', (1080, 1080), color='black')
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 90)
    except:
        font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), texto, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    draw.text(((1080-w)/2, (1080-h)/2), texto, fill='white', font=font, align="center")
    img.save("post.png")

frases = [
    "Trabaja mientras duermen.",
    "El éxito se construye, no se espera.",
    "Disciplina > motivación.",
    "Sin excusas, solo resultados.",
    "Hoy es el día 1 del resto de tu vida."
]

print("HUSTLE DIARIO BOT INICIADO – @HustleDiario")

while True:
    for frase in frases:
        crear_imagen(frase)
        media = client.media_upload(filename="post.png")
        client.create_tweet(text="", media_ids=[media.media_id])
        print(f"[{datetime.now().strftime('%H:%M')}] Publicado: {frase}")
        time.sleep(21600)  # 6 horas
