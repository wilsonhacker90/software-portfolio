from dotenv import load_dotenv
import os

load_dotenv(r"C:\Users\wilso\Desktop\x\x\matplotlib_vscode\SIMULACION PROTEUS\variables.env")  # Carga las variables desde el archivo .env

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_TOKEN = os.getenv("TWILIO_TOKEN")
TWILIO_FROM = os.getenv("TWILIO_FROM")
print(TWILIO_FROM)

if not TWILIO_SID or not TWILIO_TOKEN or not TWILIO_FROM:
    raise ValueError("⚠️ Falta configurar las variables de entorno de Twilio.")
    
else:
    print("bien hecho")