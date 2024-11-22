import json
import spacy
import pyaudio
from vosk import Model, KaldiRecognizer
import threading

# Diccionario de traducción de etiquetas al español
etiqueta_traduccion = {
    "NOUN": "Sustantivo",
    "VERB": "Verbo",
    "ADJ": "Adjetivo",
    "ADV": "Adverbio",
    "PRON": "Pronombre",
    "DET": "Determinante",
    "ADP": "Adposición",
    "CONJ": "Conjunción",
    "INTJ": "Interjección",
    "PROPN": "Nombre propio",
    "NUM": "Número",
    "PART": "Partícula",
    "SCONJ": "Conjunción subordinante",
    "CCONJ": "Conjunción coordinante",
    "AUX": "Verbo auxiliar",
    "SYM": "Símbolo",
    "PUNCT": "Puntuación"
}

nlp = spacy.load("es_core_news_lg")

modelo_vosk = "C:\\Users\\iroba\\Downloads\\vosk-model-small-es-0.42\\vosk-model-small-es-0.42"

def obtener_descripcion_espanol(etiqueta):
    return etiqueta_traduccion.get(etiqueta, "Etiqueta desconocida")

def reconocer_audio():
    model = Model(modelo_vosk)
    recognizer = KaldiRecognizer(model, 16000)

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
    stream.start_stream()

    print("Por favor, hable ahora...")

    texto_reconocido = ""
    while True:
        datos = stream.read(4096, exception_on_overflow=False)
        if recognizer.AcceptWaveform(datos):
            resultado = json.loads(recognizer.Result())
            texto_reconocido += resultado.get("text", "")
            break

    stream.stop_stream()
    stream.close()
    p.terminate()

    print(f"Texto reconocido: {texto_reconocido}")
    return texto_reconocido

def analizar_texto(texto):
    doc = nlp(texto)
    resultado = []

    resultado.append("\nAnálisis gramatical:")
    tokens = [(token.text, token.pos_) for token in doc]

    for texto, etiqueta in tokens:
        descripcion = obtener_descripcion_espanol(etiqueta)
        resultado.append(f"Palabra: {texto}, Etiqueta: {etiqueta}, Descripción: {descripcion}")

    with open("resultado_analisis.txt", "w", encoding="utf-8") as archivo:
        archivo.write("\n".join(resultado))
        print("El análisis ha sido guardado en 'resultado_analisis.txt'.")

def iniciar_reconocimiento():
    texto = reconocer_audio()
    if texto:
        threading.Thread(target=analizar_texto, args=(texto,)).start()

if __name__ == "__main__":
    iniciar_reconocimiento()
