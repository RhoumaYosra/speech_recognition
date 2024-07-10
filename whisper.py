import os
import time
import speech_recognition as sr

# Set the OpenAI API key as an environment variable
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")   # Remplacez par votre clé API OpenAI

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Parlez maintenant...")
    audio = recognizer.listen(source)

try:
    # Start timing
    start_time = time.time()
    
    # Call the API
    response = recognizer.recognize_whisper_api(audio)
    
    # End timing
    end_time = time.time()
    
    # Calculate the response time
    response_time = end_time - start_time
    
    print("OpenAI Whisper API pense que vous avez dit : " + response)
    print(f"Temps de réponse : {response_time:.2f} secondes")
except sr.UnknownValueError:
    print("OpenAI Whisper API n'a pas compris l'audio")
except sr.RequestError as e:
    print(f"Erreur de service de OpenAI Whisper API; {e}")

# import os
# import time
# import speech_recognition as sr
# from dotenv import load_dotenv

# # Load environment variables from .env
# load_dotenv()

# # Set the OpenAI API key as an environment variable
# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")  # Remplacez par votre clé API OpenAI

# recognizer = sr.Recognizer()

# # Chemin vers votre fichier audio WAV
# audio_file = "./converted_audio.wav"

# # Chargez le fichier audio
# with sr.AudioFile(audio_file) as source:
#     audio = recognizer.record(source)

# try:
#     # Start timing
#     start_time = time.time()
    
#     # Call the API
#     response = recognizer.recognize_whisper_api(audio)
    
#     # End timing
#     end_time = time.time()
    
#     # Calculate the response time
#     response_time = end_time - start_time
    
#     print("OpenAI Whisper API pense que vous avez dit : " + response)
#     print(f"Temps de réponse : {response_time:.2f} secondes")
# except sr.UnknownValueError:
#     print("OpenAI Whisper API n'a pas compris l'audio")
# except sr.RequestError as e:
#     print(f"Erreur de service de OpenAI Whisper API; {e}")
