import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Parlez maintenant...")
    audio = recognizer.listen(source)

try:
    print("CMU Sphinx pense que vous avez dit : " + recognizer.recognize_sphinx(audio, language="fr-FR"))
except sr.UnknownValueError:
    print("CMU Sphinx n'a pas compris l'audio")
except sr.RequestError as e:
    print(f"Erreur de service de CMU Sphinx; {e}")
