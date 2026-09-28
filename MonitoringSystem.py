import doctest # Importamos doctest para poder hacer pruebas unitarias directamente en los comentarios (docstrings).

# Definimos la matriz 'datos' como una lista de listas (anidadas). 
# Cada fila representa una muestra y cada columna una variable (Temperatura, Voltaje, Corriente).
datos = [
    [24.8, 3.30, 1.20],
    [25.5, 3.32, 1.22],
    [27.1, 3.38, 1.28],
    [30.2, 3.41, 1.35],
    [28.7, 3.29, 1.19],
    [31.5, 3.45, 1.38],
    [26.4, 3.31, 1.24],
    [29.8, 3.36, 1.29]
]

def extraer_columna(matriz, indice):
    """
    Extrae todos los elementos de una columna específica de una matriz.
    Se hace iterando sobre las filas y tomando el elemento en la posición del 'índice'.
    
    Pruebas doctest:
    >>> m = [[1, 2], [3, 4], [5, 6]]
    >>> extraer_columna(m, 0)
    [1, 3, 5]
    >>> extraer_columna(m, 1)
    [2, 4, 6]
    """
    columna = [] # Inicializamos una lista vacía que guardará los valores extraídos.
    for fila in matriz: # Recorremos la matriz principal, fila por fila.
        columna.append(fila[indice]) # Tomamos el valor en el índice dado y lo agregamos a nuestra lista.
    return columna # Retornamos la nueva lista.

def calcular_resumen(valores):
    """
    Calcula la cantidad, mínimo, máximo y promedio de una lista numérica.
    Utilizamos las funciones integradas de Python (len, min, max, sum) por eficiencia.
    
    Pruebas doctest:
    >>> calcular_resumen([10, 20, 30])
    (3, 10, 30, 20.0)
    """
    cantidad = len(valores) # 'len' cuenta cuántos elementos hay en total.
    minimo = min(valores)   # 'min' encuentra el valor más pequeño.
    maximo = max(valores)   # 'max' encuentra el valor más grande.
    promedio = sum(valores) / cantidad # Sumamos todos los valores y dividimos por el total.
    return cantidad, minimo, maximo, promedio # Se retorna como una tupla (colección inmutable).

def detectar_alertas(matriz):
    """
    Detecta e imprime las medidas que superan los límites establecidos.
    Límites: Temp >= 30.0, Voltaje > 3.40, Corriente > 1.30.
    
    Pruebas doctest (Simulando una fila que rompe los límites):
    >>> matriz_alerta = [[31.5, 3.45, 1.38]]
    >>> detectar_alertas(matriz_alerta)
    Muestra 0: Temperatura alta
    Muestra 0: Voltaje alto
    Muestra 0: Corriente alta
    """
    # Usamos 'enumerate' porque necesitamos tanto el índice 'i' como los datos de la 'fila'.
    for i, fila in enumerate(matriz): 
        temperatura = fila[0]
        voltaje = fila[1]
        corriente = fila[2]

        # NOTA DE DISEÑO: Se utiliza el índice 'i' directamente (comenzando desde 0) 
        # y no 'i + 1' (conteo humano). Esto se hace para coincidir de manera estricta 
        # con el "Ejemplo de salida esperada" de la guía (Muestra 3 y Muestra 5), 
        # reflejando la posición real del dato en la memoria de la matriz.
        if temperatura >= 30.0:
            print(f"Muestra {i}: Temperatura alta")
        if voltaje > 3.40:
            print(f"Muestra {i}: Voltaje alto")
        if corriente > 1.30:
            print(f"Muestra {i}: Corriente alta")

def main():
    """Función principal que orquesta la ejecución del programa."""
    
    # 1. Extracción de columnas usando la función
    temperaturas = extraer_columna(datos, 0)
    voltajes = extraer_columna(datos, 1)
    corrientes = extraer_columna(datos, 2)

    # 2. Cálculo de resúmenes desempaquetando las tuplas
    c_t, min_t, max_t, prom_t = calcular_resumen(temperaturas)
    c_v, min_v, max_v, prom_v = calcular_resumen(voltajes)
    c_c, min_c, max_c, prom_c = calcular_resumen(corrientes)

# 3. Comprensión de listas: Filtrar únicamente los valores críticos
    temperaturas_altas = [t for t in temperaturas if t >= 30.0]
    voltajes_altos = [v for v in voltajes if v > 3.40]
    corrientes_altas = [c for c in corrientes if c > 1.30]

    print("\nVALORES CRÍTICOS DETECTADOS (Comprensión de listas):")
    print(f"Temperaturas >= 30.0 °C: {temperaturas_altas}")
    print(f"Voltajes > 3.40 V: {voltajes_altos}")
    print(f"Corrientes > 1.30 A: {corrientes_altas}")
    print("-" * 40)

    # 4. Impresión del informe. Se formatea con 'f-strings' y limitando los decimales a 2 (.2f).
    print("\nResumen del Sistema\n")
    print("")

    print("Temperatura\n")
    print(f"Cantidad: {c_t}")
    print(f"Mínimo: {min_t}°C")
    print(f"Máximo: {max_t}°C")
    print(f"Promedio: {prom_t:.2f}°C")
    print("")

    print("Voltaje\n")
    print(f"Cantidad: {c_v}")
    print(f"Mínimo: {min_v} V")
    print(f"Máximo: {max_v} V")
    print(f"Promedio: {prom_v:.2f} V")
    print("")

    print("Corriente\n")
    print(f"Cantidad: {c_c}")
    print(f"Mínimo: {min_c} A")
    print(f"Máximo: {max_c} A")
    print(f"Promedio: {prom_c:.2f} A")
    print("")

    print("Alertas")
    print("")
    detectar_alertas(datos)

# Este bloque asegura que las pruebas se ejecuten y luego corra el programa si el archivo es ejecutado directamente.
if __name__ == "__main__":
    # testmod() busca y corre automáticamente todo lo que parezca una prueba en los docstrings.
    doctest.testmod() 
    main()