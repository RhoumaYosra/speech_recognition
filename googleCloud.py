# import os
# import speech_recognition as sr
# import time

# # Set the environment variable for Google Cloud credentials
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'./speechrecognition-428115-1ceea7a65211.json'

# recognizer = sr.Recognizer()

# with sr.Microphone() as source:
#     print("Parlez maintenant...")
#     audio = recognizer.listen(source)

# start_time = time.time()
# try:
#     result = recognizer.recognize_google_cloud(audio, language="fr-FR")
#     print("Google Cloud Speech API : " + result)
# except sr.UnknownValueError:
#     print("La reconnaissance vocale n'a pas compris l'audio")
# except sr.RequestError as e:
#     print(f"Erreur de service de Google Cloud Speech API; {e}")
# print(f"Temps de réponse : {time.time() - start_time} secondes")



import os
import speech_recognition as sr
import time
from pydub import AudioSegment

# Set the environment variable for Google Cloud credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'./speechrecognition-428115-1ceea7a65211.json'

# Chemin vers le fichier MP3
audio_file_path = './audio.wav'

# Convertir le fichier MP3 en format WAV
audio = AudioSegment.from_mp3(audio_file_path)
audio.export("converted_audio.wav", format="wav")

recognizer = sr.Recognizer()

# Utiliser le fichier audio converti pour la reconnaissance vocale
with sr.AudioFile("converted_audio.wav") as source:
    audio_data = recognizer.record(source)

start_time = time.time()
try:
    result = recognizer.recognize_google_cloud(audio_data, language="fr-FR")
    print("Google Cloud Speech API : " + result)
except sr.UnknownValueError:
    print("La reconnaissance vocale n'a pas compris l'audio")
except sr.RequestError as e:
    print(f"Erreur de service de Google Cloud Speech API; {e}")
print(f"Temps de réponse : {time.time() - start_time} secondes")
