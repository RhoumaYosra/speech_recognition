# import speech_recognition as sr
# import time

# recognizer = sr.Recognizer()

# with sr.Microphone() as source:
#     print("Parlez maintenant...")
#     audio = recognizer.listen(source)

# start_time = time.time()
# try:
#     result = recognizer.recognize_wit(audio, key="")
#     print("Wit.ai : " + result)
# except sr.UnknownValueError:
#     print("La reconnaissance vocale n'a pas compris l'audio")
# except sr.RequestError as e:
#     print(f"Erreur de service de Wit.ai; {e}")
# print(f"Temps de réponse : {time.time() - start_time} secondes")


import speech_recognition as sr
from pydub import AudioSegment
import time
import os 
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Charger le fichier audio MP3 et le convertir en format WAV
audio_file = "./audio.wav"
audio = AudioSegment.from_mp3(audio_file)
audio.export("converted.wav", format="wav")

recognizer = sr.Recognizer()

# Utiliser AudioFile pour lire le fichier converti
with sr.AudioFile("converted.wav") as source:
    print("Lecture du fichier audio...")
    audio_data = recognizer.record(source)

start_time = time.time()
try:
    # Remplacez 'YOUR_WIT_AI_API_KEY' par votre clé API de Wit.ai
    result = recognizer.recognize_wit(audio_data, key=os.getenv("WIT_KEY"))
    print("Wit.ai : " + result)
except sr.UnknownValueError:
    print("La reconnaissance vocale n'a pas compris l'audio")
except sr.RequestError as e:
    print(f"Erreur de service de Wit.ai; {e}")
print(f"Temps de réponse : {time.time() - start_time} secondes")
