import speech_recognition as sr
import time

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Parlez maintenant...")
    audio = recognizer.listen(source)

start_time = time.time()
try:
    result = recognizer.recognize_google(audio, language="fr-FR")
    print("Google Speech Recognition : " + result)
except sr.UnknownValueError:
    print("La reconnaissance vocale n'a pas compris l'audio")
except sr.RequestError as e:
    print(f"Erreur de service de reconnaissance vocale; {e}")
print(f"Temps de réponse : {time.time() - start_time} secondes")



# import speech_recognition as sr
# import time
# from pydub import AudioSegment

# # Convertir le fichier MP3 en WAV
# audio_file_path = "./audio.wav"
# audio = AudioSegment.from_mp3(audio_file_path)  # Correction ici
# audio.export("converted.wav", format="wav")

# # Utiliser le fichier WAV pour la transcription
# recognizer = sr.Recognizer()

# with sr.AudioFile("converted.wav") as source:
#     print("Lecture de l'audio...")
#     audio_data = recognizer.record(source)

# start_time = time.time()
# try:
#     result = recognizer.recognize_google(audio_data, language="fr-FR")
#     print("Google Speech Recognition : " + result)
# except sr.UnknownValueError:
#     print("La reconnaissance vocale n'a pas compris l'audio")
# except sr.RequestError as e:
#     print(f"Erreur de service de reconnaissance vocale; {e}")
# print(f"Temps de réponse : {time.time() - start_time} secondes")

