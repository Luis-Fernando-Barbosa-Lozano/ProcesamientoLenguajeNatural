from collections import Counter
oraciones_ingles = [
    "the dog barks",
    "a bird flies",
    "the fish swims",
    "the world is your",
    "the sun shines",
    "a flower grows",
    "the tree stands"
]

oraciones_espanol = [
    "el perro ladra",
    "el pajaro vuela",
    "el pez nada",
    "el aguila vuela",
    "el sol brilla",
    "una flor crece",
    "el arbol permanece"
]

correspondencias = {
    "the": "el",
    "dog": "perro",
    "fish": "pez",
    "swims": "nada",
    "sun": "sol",
    "flower": "flor",
    "flies": "vuela",
    "grows": "crece",
    "tree": "arbol",
    "stands": "permanece",
    "a": "una",
    "shines": "brilla",
}

def contar_frecuencia_por_palabra(oraciones):
    frecuencias = Counter()
    for oracion in oraciones:
        palabras = oracion.lower().split()
        for palabra in palabras:
            frecuencias[palabra] += 1
    return frecuencias

frecuencias_ingles = contar_frecuencia_por_palabra(oraciones_ingles)

total_palabras_por_oracion = [len(oracion.split()) for oracion in oraciones_ingles]

def mostrar_frecuencia_y_operaciones(frecuencias, oraciones_ingles, oraciones_espanol, correspondencias, total_palabras_por_oracion):
    for palabra, frecuencia in frecuencias.items():
        print(f"\nPalabra: '{palabra}'")

        # Traducir la palabra de inglés a español usando el diccionario
        palabra_en_espanol = correspondencias.get(palabra, palabra)

        # Listar las oraciones en español donde aparece la palabra
        frases_con_palabra = []
        for oracion_ingles, oracion_espanol in zip(oraciones_ingles, oraciones_espanol):
            if palabra in oracion_ingles.lower().split():
                frases_con_palabra.append(oracion_espanol)

        print("Frases donde aparece en español:")
        for frase in frases_con_palabra:
            print(" ", frase)

        total_palabras = 0
        for frase in frases_con_palabra:
            total_palabras += len(frase.split())

        print(f">>> Frecuencia de '{palabra}': {frecuencia} (frecuencia)")
        print(f">>> Total de palabras en frases con '{palabra}': {total_palabras} (total de palabras)")
        print(f">>> Frecuencia de '{palabra}' = {frecuencia} / {total_palabras} = {frecuencia / total_palabras:.2f}")

mostrar_frecuencia_y_operaciones(frecuencias_ingles, oraciones_ingles, oraciones_espanol, correspondencias,
                                 total_palabras_por_oracion)