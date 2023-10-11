lista_personas = [
    ("11111111", "Pedro", "Paez", 24),
    ("22222222", "Fito", "Garcia", 23),
    ("33333333", "Leo", "Peralta", 26),
    ("44444444", "Bruno", "Mac", 25),
    ("55555555", "Nico", "Zaoral", 27),
    ("44444444", "Bruno", "Mac", 25),
]


def ordenar(lista_personas):
    """El metodo debe devolver una lista con las edades ordenadas de menor a mayor"""
    # Completar
    lista_ordenada_edad = []
    edades_ordenadas = []
    lista_ordenada_edad = sorted(lista_personas, key=lambda edad: edad[3])

    for i in range(len(lista_ordenada_edad)):
        edades_ordenadas.append(lista_ordenada_edad[i][3])

    return edades_ordenadas


def convertir_a_diccionario(lista_personas):
    """Hacer un diccionario que tenga como claves los “dni” y como valores tuplas con nombre, apellido y edad"""
    # Completar
    dicc = {}

    for i in range(len(lista_personas)):
        llave = lista_personas[i][0]
        valor = (lista_personas[i][1], lista_personas[i][2], lista_personas[i][3])
        dicc[llave] = valor

    return dicc


def devolver_edad(lista_personas, dni):
    """Para la 'lista_personas' devuelve la edad de la persona que tenga el dni definido.
    Tip: intentar usar el método convertir_a_diccionario"""
    # Completar
    edad = 0
    dicc = convertir_a_diccionario(lista_personas)

    for llave in dicc:
        if llave == dni:
            edad = dicc[llave][2]  # Dic = "llave(dni)" : "(nombre, apellido, edad)"

    return edad


def eliminar_repetidos(lista_personas):
    """El metodo debe devolver los elementos unicos"""
    # Completar
    lista_a_set = set(lista_personas)
    lista_unicos = list(lista_a_set)

    return lista_unicos


def separar_por_edad(lista_personas):
    """Devolver dos listas
    * lista 1: mayores de 25 (incluido)
    * lista 2: menores de 25
    """
    # Completar
    mayores = []
    menores = []

    for i in range(len(lista_personas)):
        if lista_personas[i][3] >= 25:
            mayores.append(lista_personas[i])
        else:
            menores.append(lista_personas[i])

    return mayores, menores


def obtener_promedio(lista):
    """Implementar obtener el promedio de la lista de números que se recibe.
    Capturar con un try/except la excepción de dividir por cero"""
    # Completar
    promedio = 0.0
    suma_edades = 0

    for i in range(len(lista)):
        suma_edades += lista[i]
    try:
        promedio = suma_edades / len(lista)
    except:
        len(lista) == 0

    return promedio


def main():
    # """ Este metodo no debe modificarse y es solo a fines de probar el codigo """
    print("Resultados:\n")
    print(" * Edades ordenadas: %s\n" % ordenar(lista_personas))
    print(
        " * Elementos como diccionario: %s\n" % convertir_a_diccionario(lista_personas)
    )
    print(
        " * La edad para dni 55555555 es: %s\n"
        % devolver_edad(lista_personas, "55555555")
    )
    print(" * Elementos únicos: %s\n" % eliminar_repetidos(lista_personas))
    print(" * Los mayores de 25 son: %s\n" % separar_por_edad(lista_personas)[0])
    print(" * Los menores de 25 son: %s\n" % separar_por_edad(lista_personas)[1])
    print(
        " * El promedio de las edades es: %s\n"
        % obtener_promedio(ordenar(lista_personas))
    )
    print(" * El promedio de una lista vacía es: %s\n" % obtener_promedio([]))

main()