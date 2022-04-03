decimal = str(input("Introduce un número entre 0 y 0.9999 con un maximo de 4 digitos decimales: "))
# Esta seccion de codigo hasta el siguiente comentario es una validacion de la entrada para permitir un solo punto en
# la segunda posicion y ningun caracter no numerico
control_solo_numeros_en_decimal = True
control_un_solo_punto = True
for i in range(0, len(decimal) - 1):
    if (decimal[i] != "0" and decimal[i] != "1" and decimal[i] != "2" and decimal[i] != "3"
            and decimal[i] != "4" and decimal[i] != "5" and decimal[i] != "6" and decimal[i] != "7"
            and decimal[i] != "8" and decimal[i] != "9" and decimal[i] != "."):
        control_solo_numeros_en_decimal = False
    if decimal[i] == "." and i != 1:
        control_un_solo_punto = False
while len(decimal) > 6 or decimal[
                          0:2] != "0." or control_un_solo_punto == False or control_solo_numeros_en_decimal == False:
    decimal = str(input("ERROR: Debes Introducir un número entre 0 y 0.9999 con un maximo de 4 digitos decimales (no "
                        "valen letras ni caracteres especiales solo numeros dentro del rango): "))
    control_solo_numeros_en_decimal = True
    control_un_solo_punto = True
    for i in range(0, len(decimal) - 1):
        if (decimal[i] != "0" and decimal[i] != "1" and decimal[i] != "2" and decimal[i] != "3"
                and decimal[i] != "4" and decimal[i] != "5" and decimal[i] != "6" and decimal[i] != "7"
                and decimal[i] != "8" and decimal[i] != "9" and decimal[i] != "."):
            control_solo_numeros_en_decimal = False
        if decimal[i] == "." and i != 1:
            control_un_solo_punto = False

# Este es el algoritmo de reducir a fraccion irreducible propiamente , he optado por buscar el maximo divisor comun
# iterando hacia atras desde numerador hasta 1
numerador = int(float(decimal) * 10000)
denominador = 10000
i = int(numerador)
while i > 1:
    if numerador % i == 0 and denominador % i == 0:
        numerador /= i
        denominador /= i
    i = i - 1
print("La fraccion irreductible del decimal introducido es  ", int(numerador), "/", int(denominador))
