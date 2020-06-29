import random

def normalize_text(text):
    forbidden = {ord(c): None for c in ("?", "¿", "¡", "!", " ", ",", ".", ";", ":", "ñ")}
    return text.lower().translate(forbidden)

def num_to_string(numlist):
    abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]
    mensaje_en_cadena = []
    i = 0
    while len(mensaje_en_cadena) < len(numlist):
        for j in range(0, 27):
            if numlist[i] == j:
                mensaje_en_cadena += abc[j - 1]
        i += 1
    return mensaje_en_cadena

def string_to_num(stringlist):
    abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]
    mensaje_en_numeros = []
    i = 0
    while len(mensaje_en_numeros) < len(stringlist):
        for j in range(0, len(abc)):
            if stringlist[i] == abc[j]:
                mensaje_en_numeros += [j + 1]
        i += 1
    return mensaje_en_numeros

def create_keystream(text, baraja):
    barajaaux = []
    barajafinalpaso3_1 = []
    barajafinalpaso3_2 = []
    posicion_a = 0
    posicion_b = 0
    keystream = []
    aux = 0
    while len(keystream) < len(text):
        # Paso 1 muevo el comodin A primero siempre
        a_encontrada = False
        for j in range(0, len(baraja)):
            if a_encontrada:
                break
            if str(baraja[j]) == 'A' and a_encontrada == False:
                if j == len(baraja) - 1:
                    barajaaux.append(baraja[0])
                    barajaaux.append('A')
                    posicion_a = 1
                    for k in range(3, len(baraja)):
                        if str(baraja[k - 1]) != 'A':
                            barajaaux.append(baraja[k - 1])
                    baraja = barajaaux
                    a_encontrada = True
                else:
                    aux = baraja[j + 1]
                    baraja[j + 1] = 'A'
                    posicion_a = j + 1
                    baraja[j] = aux
                    a_encontrada = True
        # muevo el comodin B despues de haber movido el A
        b_encontrada = False
        #Paso2 mueve el comodin B
        for j in range(0, len(baraja)):
            if b_encontrada:
                break
            if str(baraja[j]) == 'B' and b_encontrada == False:
                if j == len(baraja) - 1:
                    barajaaux.append(baraja[0])
                    barajaaux.append(baraja[1])
                    barajaaux.append('B')
                    posicion_b = 2
                    for k in range(4, len(baraja)):
                        if str(baraja[k - 1]) != 'B':
                            barajaaux.append(baraja[k - 1])
                    baraja = barajaaux
                    b_encontrada = True
                elif j == len(baraja) - 2:
                    barajaaux.append(baraja[0])
                    barajaaux.append('B')
                    posicion_b = 1
                    for k in range(3, len(baraja)):
                        if str(baraja[k - 1]) != 'B':
                            barajaaux.append(baraja[k - 1])
                    baraja = barajaaux
                    b_encontrada = True
                else:
                    aux2 = baraja[j + 2]
                    aux = baraja[j + 1]
                    baraja[j + 2] = "B"
                    posicion_b = j + 2
                    baraja[j] = aux
                    baraja[j + 1] = aux2
                    b_encontrada = True
        # Paso 3 cortar en 3 mazos he intercambiar el mazo Antes de A con el mazo despues de B
        if posicion_b > posicion_a:
            baraja1 = baraja[:posicion_a]
            baraja2 = baraja[posicion_a:posicion_b + 1]
            baraja3 = baraja[posicion_b + 1:]
        else:
            baraja1 = baraja[:posicion_b]
            baraja2 = baraja[posicion_b:posicion_a + 1]
            baraja3 = baraja[posicion_a + 1:]
        barajafinalpaso3_1 += baraja3
        barajafinalpaso3_1 += baraja2
        barajafinalpaso3_1 += baraja1
        baraja = barajafinalpaso3_1
        #Paso4  Si la ultima carta es distinta de comodin miro el valor d ela ultima carta
        if str(baraja[len(baraja) - 1]) != 'A' and str(baraja[len(baraja) - 1]) != 'B':
            baraja1 = baraja[:baraja[len(baraja) - 1]]
            baraja2 = baraja[baraja[len(baraja) - 1]:len(baraja) - 1]
            baraja3 = baraja[len(baraja) - 1:]
            barajafinalpaso3_2 += baraja2
            barajafinalpaso3_2 += baraja1
            barajafinalpaso3_2 += baraja3
            baraja = barajafinalpaso3_2
        #Paso5 MIro el valor dela primera carta
            #primero compruebo que no sea un comdin la primera carta en cuyo caso tendria que contar 53
            #me iria por el elif, siempre hay que comprobar si la carta que edspues de la que contamos es un comdin
            #si lo es, no apuntamos y seguimos iterando
            if str(baraja[0]) != 'A' and str(baraja[0]) != 'B':
                if str(baraja[baraja[0]]) != 'A' and str(baraja[baraja[0]]) != 'B':
                    if int(baraja[baraja[0]]) > 26:
                        num = int(baraja[baraja[0]]) % 26
                        keystream += [num]
                    else:
                        keystream += [int(baraja[baraja[0]])]
            elif str(baraja[52]) != 'A' and str(baraja[52]) != 'B':
                if int(baraja[52]) > 26:
                    num = int(baraja[52]) % 26
                    keystream += [num]
                else:
                    keystream += [int(baraja[52])]
        barajaaux = []
        barajafinalpaso3_1 = []
        barajafinalpaso3_2 = []
        posicion_a = 0
        posicion_b = 0
        aux = 0
    return keystream

def cifrar(mensaje, clave_emisor):
    mensaje = normalize_text(mensaje)
    # imprimo el mensaje en letras y el array de numeros necesario para cifrar
    print("Mensaje : ", mensaje)
    mensaje_en_numeros = string_to_num(mensaje)
    print("Mensaje en numeros", mensaje_en_numeros)

    # calculo el keystream a partir de la baraja clave que es un barajeo random
    mykeystream_numeros_cifrar = create_keystream(mensaje_en_numeros, clave_emisor)
    print("El Keystream obtenido en el cifrado en numeros es : ", mykeystream_numeros_cifrar)
    keystream = num_to_string(mykeystream_numeros_cifrar)
    print("El Keystream obtenido en el cifrado en letras es : ", keystream)
    mensaje_cifrado_numeros = []

    for i in range(0, len(mensaje_en_numeros)):
        if mensaje_en_numeros[i] + mykeystream_numeros_cifrar[i] > 26:
            mensaje_cifrado_numeros.append((mensaje_en_numeros[i] + mykeystream_numeros_cifrar[i]) % 26)
        else:
            mensaje_cifrado_numeros.append(mensaje_en_numeros[i] + mykeystream_numeros_cifrar[i])
    mensaje_cifrado_cadena = num_to_string(mensaje_cifrado_numeros)
    return mensaje_cifrado_cadena

def descifrar(mensaje_cifrado, clave_receptor):

    mensaje_cifrado_numeros = string_to_num(mensaje_cifrado)
    # calculo el keystream a partir de la baraja clave que es un barajeo random
    mykeystream_numeros_descifrar = create_keystream(mensaje_cifrado_numeros, clave_receptor)
    print("El Keystream obtenido durante el descifrado en numeros es : ", mykeystream_numeros_descifrar)
    keystream = num_to_string(mykeystream_numeros_descifrar)
    print("El Keystream obtenido durante el descifrado en letras es : ", keystream)

    mensaje_descifrado_numeros = []
    for i in range(0, len(mensaje_cifrado_numeros)):
        if mensaje_cifrado_numeros[i] < mykeystream_numeros_descifrar[i]:
            mensaje_descifrado_numeros.append(mensaje_cifrado_numeros[i] + 26 - mykeystream_numeros_descifrar[i])
        else:
            mensaje_descifrado_numeros.append(mensaje_cifrado_numeros[i] - mykeystream_numeros_descifrar[i])
    mensaje_descifrado_cadena = num_to_string(mensaje_descifrado_numeros)
    return mensaje_descifrado_cadena

def num_to_cards(lista_numeros):
    cartas = sum(list(
        map(lambda n: [str(n) + 'A', str(n) + '2', str(n) + '3', str(n) + '4', str(n) + '5', str(n) + '6', str(n) + '7',
                       str(n) + '8', str(n) + '9', str(n) + '10', str(n) + 'J', str(n) + 'Q', str(n) + 'K'],
            ['♣', '♦', '♥', '♠'])), [])
    cartas.append("Joker A")
    cartas.append("Joker B")
    lista_cartas=[]
    i = 0
    while len(lista_cartas) < len(lista_numeros):
        for j in range(0, len(cartas)):
            if i < 54:
                if lista_numeros[i] == 'A':
                    lista_cartas.append(cartas[52])
                    i += 1
                elif lista_numeros[i] == 'B':
                    lista_cartas.append(cartas[53])
                    i += 1
                elif lista_numeros[i] == j:
                    lista_cartas.append(cartas[j-1])
                    i += 1
    return lista_cartas



if __name__ == "__main__":
    baraja = list(range(1, 53))
    baraja.append("A")
    baraja.append("B")
    # hago un shuffle de la baraja que va a ser mi clave para calcular el keystream
    random.shuffle(baraja)
    clave = num_to_cards(baraja)
    print("La clave a utilizar es :")
    print(clave)

    # hago 2 copias una para el emisor (cifrar), otra para el receptor (descifrar)
    clave_emisor = baraja.copy()
    clave_receptor = baraja.copy()

    mensaje = str(input("Introduce el mensaje secreto se le quitaran espacios y simbolos de escritura: "))

    print("Es importante verificar que el calculo del keystream tanto en el cifrado como en el descifrado es el mismo, es decir es determinista para una mismo input")

    # cifro el mensaje con la funcion cifrar que me devuelve un array de numeros cifrados y luego en el main los convierto a letras
    mensaje_cifrado = cifrar(mensaje, clave_emisor)

    print("El mensaje cifrado en cadena es: ", mensaje_cifrado)

    # Ahora descifro con la funcion descifrar a apartir del mensaje cifrado en numeros y el keystream generado para que devuelva
    # el array de numeros mensaje_descifrado_numeros, luego lo convierto a testo en el main
    mensaje_descifrado = descifrar(mensaje_cifrado, clave_receptor)
    mensaje_descifrado_cadena = "El mensaje descifrado en una cadena es : "
    for i in range(0, len(mensaje_descifrado)):
        mensaje_descifrado_cadena += mensaje_descifrado[i]
    print(mensaje_descifrado_cadena)