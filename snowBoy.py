import snowboydecoder

# Détecteur de mots-clés
detector = snowboydecoder.HotwordDetector("path/to/your/hotword/model.pmdl", sensitivity=0.5)

# Fonction callback appelée lors de la détection
def detected():
    print("Mot-clé détecté")

print("En attente du mot-clé...")
detector.start(detected_callback=detected)
