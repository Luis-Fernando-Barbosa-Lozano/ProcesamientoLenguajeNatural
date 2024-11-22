import spacy

# Cargar el modelo para español
nlp = spacy.load("es_core_news_sm")

# Función para analizar la frase y mostrar la categoría de cada palabra
def analizar_frase(frase):
    doc = nlp(frase)  # Procesar la frase con spaCy

    print("Análisis de la frase:")
    for token in doc:
        # Mostrar la palabra, su categoría gramatical y su significado (opcional)
        print(f'"{token.text}" → {token.pos_} ({token.pos_.lower()})')

# Solicitar la frase del usuario
frase = input("Ingresa una frase: ")

# Analizar la frase
analizar_frase(frase)