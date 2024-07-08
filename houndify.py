# import speech_recognition as sr
# import time

# recognizer = sr.Recognizer()

# with sr.Microphone() as source:
#     print("Parlez maintenant...")
#     audio = recognizer.listen(source)

# houndify_client_id = ""  # Remplacez par votre ID client Houndify
# houndify_client_key = ""  # Remplacez par votre clé client Houndify

# try:
#     start_time = time.time()  # Début de la mesure du temps
#     response = recognizer.recognize_houndify(audio, client_id=houndify_client_id, client_key=houndify_client_key)
#     end_time = time.time()  # Fin de la mesure du temps
#     response_time = end_time - start_time
#     print("Houndify API pense que vous avez dit : " + response[0])
#     print(f"Temps de réponse de l'API Houndify: {response_time} secondes")
# except sr.UnknownValueError:
#     print("Houndify API n'a pas compris l'audio")
# except sr.RequestError as e:
#     print(f"Erreur de service de Houndify API; {e}")



import speech_recognition as sr
from pydub import AudioSegment
import time
import os 
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Chemin vers votre fichier audio 
audio_file = "./audio.wav"
converted_audio_file = "converted_audio.wav"

# Convertir le fichier MP3 en WAV
audio = AudioSegment.from_mp3(audio_file)
audio.export(converted_audio_file, format="wav")

recognizer = sr.Recognizer()

# Utilisez le fichier WAV converti
with sr.AudioFile(converted_audio_file) as source:
    audio_data = recognizer.record(source)  # Lire l'audio du fichier

# Accéder aux variables d'environnement
houndify_client_id = os.getenv("HOUNDIFY_CLIENT_ID")  # Remplacez par votre ID client Houndify
houndify_client_key = os.getenv("HOUNDIFY_CLIENT_KEY")  # Remplacez par votre clé client Houndify

# Vérifier les valeurs récupérées
print(f"Client ID: {houndify_client_id}")
print(f"Client Key: {houndify_client_key}")

# Check if client_id or client_key are None
if houndify_client_id is None or houndify_client_key is None:
    raise ValueError("Houndify credentials not found. Check your .env file.")

try:
    start_time = time.time()  # Début de la mesure du temps
    response = recognizer.recognize_houndify(audio_data, client_id=houndify_client_id, client_key=houndify_client_key)
    end_time = time.time()  # Fin de la mesure du temps
    response_time = end_time - start_time
    
    # Handle response based on its type
    if isinstance(response, tuple):
        # Convert each item to string if not already
        response_text = " ".join(str(item) for item in response)
    else:
        response_text = response
    
    print("Houndify API pense que vous avez dit : " + response_text)
    print(f"Temps de réponse de l'API Houndify: {response_time} secondes")
except sr.UnknownValueError:
    print("Houndify API n'a pas compris l'audio")
except sr.RequestError as e:
    print(f"Erreur de service de Houndify API; {e}")
