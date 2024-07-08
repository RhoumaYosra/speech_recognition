import speech_recognition as sr
import time

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Parlez maintenant...")
    audio = recognizer.listen(source)

start_time = time.time()
try:
    # Replace "<your-azure-key>" with your actual Azure Speech API key
    result = recognizer.recognize_azure(audio, key="157c347a3b33426f98adb425454a32f9")
    print("Microsoft Azure Speech : " + result)
except sr.UnknownValueError:
    print("La reconnaissance vocale n'a pas compris l'audio")
except sr.RequestError as e:
    print(f"Erreur de service de Microsoft Azure Speech : {e}")

print(f"Temps de réponse : {time.time() - start_time} secondes")
