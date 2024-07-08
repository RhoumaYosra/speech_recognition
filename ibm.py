import speech_recognition as sr
import time

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Parlez maintenant...")
    audio = recognizer.listen(source)

start_time = time.time()
try:
    result = recognizer.recognize_ibm(audio, username="yossra.rhouma@umanlink.com", password="Yasssoura12#", language="fr-FR")
    print("IBM Speech to Text : " + result)
except sr.UnknownValueError:
    print("La reconnaissance vocale n'a pas compris l'audio")
except sr.RequestError as e:
    print(f"Erreur de service de IBM Speech to Text; {e}")
print(f"Temps de réponse : {time.time() - start_time} secondes")
