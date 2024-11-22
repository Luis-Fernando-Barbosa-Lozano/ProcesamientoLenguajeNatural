import PyPDF2

def leer_pdf(ruta_pdf):
    try:
        texto = ""
        with open(ruta_pdf, "rb") as archivo:
            lector_pdf = PyPDF2.PdfReader(archivo)
            for pagina in range(len(lector_pdf.pages)):
                texto += lector_pdf.pages[pagina].extract_text() or ""
        return texto
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta_pdf}'.")
        return ""

def contar_frecuencias_colocaciones(texto, colocaciones):
    """Cuenta cuántas veces aparece cada colocación en el texto."""
    frecuencias = {}
    texto = texto.lower()  # Normalizar el texto a minúsculas

    for colocacion in colocaciones:
        colocacion_lower = colocacion.lower()
        frecuencias[colocacion] = texto.count(colocacion_lower)

    return frecuencias

def calcular_probabilidad_condicional(texto, colocaciones):

    probabilidades = {}
    texto = texto.lower()

    for colocacion in colocaciones:
        colocacion_lower = colocacion.lower()
        primera_palabra, segunda_palabra = colocacion_lower.split()
        frecuencia_bigrama = texto.count(colocacion_lower)
        frecuencia_primera = texto.count(primera_palabra)

        print(f"La oracion {colocacion_lower} aparece: {frecuencia_bigrama} veces")
        print(f"La palabra {primera_palabra} {frecuencia_primera} veces")

        # Calcular la probabilidad condicional evitando división por cero
        if frecuencia_primera > 0:
            probabilidad = frecuencia_bigrama / frecuencia_primera
        else:
            probabilidad = 0

        probabilidades[(primera_palabra, segunda_palabra)] = probabilidad

    return probabilidades

# Definición de ruta y colocaciones
ruta_pdf = "redesneuronales.pdf"
colocaciones = [
    "inteligencia artificial"
]

# Leer el contenido del PDF
texto_pdf = leer_pdf(ruta_pdf)
if not texto_pdf:
    print("El archivo PDF no contiene texto o no se pudo leer.")
    exit()

# Contar las frecuencias de las colocaciones
frecuencias_colocaciones = contar_frecuencias_colocaciones(texto_pdf, colocaciones)

print("Frecuencias de colocaciones:")
for colocacion, frecuencia in frecuencias_colocaciones.items():
    print(f"'{colocacion}': {frecuencia} apariciones")

# Encontrar la colocación con mayor frecuencia
colocacion_mas_frecuente = max(frecuencias_colocaciones, key=frecuencias_colocaciones.get)
print(f"\nLa colocación con más frecuencia es: '{colocacion_mas_frecuente}' "
      f"con {frecuencias_colocaciones[colocacion_mas_frecuente]} apariciones.")

# Calcular las probabilidades condicionales
probabilidades_colocaciones = calcular_probabilidad_condicional(texto_pdf, colocaciones)

print("\nProbabilidades condicionales de colocaciones:")
for (primera_palabra, segunda_palabra), probabilidad in probabilidades_colocaciones.items():
    print(f"La palabra '{segunda_palabra}' tiene una probabilidad del {probabilidad :.2f} "
          f"de aparecer después de '{primera_palabra}'.")