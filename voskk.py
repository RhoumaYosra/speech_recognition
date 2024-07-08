# import time
# import speech_recognition as sr
# import vosk
# import json

# # Specify the path to the Vosk model
# model_path = "./vosk/vosk-model-small-fr-0.22"  # Adjust this path based on where you placed the model

# # Initialize Vosk recognizer with the specified model and sample rate
# vosk.SetLogLevel(-1)  # Suppress Vosk log messages (optional)
# model = vosk.Model(model_path)
# recognizer = vosk.KaldiRecognizer(model, 16000)

# # Use SpeechRecognition library for microphone input
# r = sr.Recognizer()

# with sr.Microphone() as source:
#     print("Parlez maintenant...")
#     start_time = time.time()  # Start measuring time
#     audio_data = r.record(source, duration=5)  # Record audio for 5 seconds
#     end_time = time.time()  # Stop measuring time

# try:
#     # Recognize speech using Vosk
#     if audio_data:
#         audio_data = audio_data.get_raw_data(convert_rate=16000, convert_width=2)
#         recognizer.AcceptWaveform(audio_data)
#         result = json.loads(recognizer.Result())
#         text = result.get("text", "")
#         print("Vosk API pense que vous avez dit : " + text)
#         print(f"Temps de reconnaissance : {end_time - start_time:.2f} secondes")
#     else:
#         print("Aucun audio enregistré.")
# except Exception as e:
#     print(f"Erreur lors de la reconnaissance avec Vosk : {e}")



import time
import speech_recognition as sr
import vosk
import json

# Specify the path to the Vosk model
model_path = "./vosk/vosk-model-small-fr-0.22"  # Adjust this path based on where you placed the model

# Initialize Vosk recognizer with the specified model and sample rate
vosk.SetLogLevel(-1)  # Suppress Vosk log messages (optional)
model = vosk.Model(model_path)
recognizer = vosk.KaldiRecognizer(model, 16000)

# Use SpeechRecognition library for audio file input
r = sr.Recognizer()

audio_file = "./converted_audio.wav"  # Replace with your WAV file path

with sr.AudioFile(audio_file) as source:
    print(f"Transcription de {audio_file}...")
    audio_data = r.record(source)  # Record the entire audio file

try:
    # Recognize speech using Vosk
    if audio_data:
        audio_data = audio_data.get_raw_data(convert_rate=16000, convert_width=2)
        start_time = time.time()  # Start measuring time for recognition
        recognizer.AcceptWaveform(audio_data)
        end_time = time.time()  # Stop measuring time for recognition

        result = json.loads(recognizer.Result())
        text = result.get("text", "")
        print("Vosk API pense que vous avez dit : " + text)
        print(f"Temps de reconnaissance : {end_time - start_time:.2f} secondes")
    else:
        print("Aucun audio enregistré.")
except Exception as e:
    print(f"Erreur lors de la reconnaissance avec Vosk : {e}")
