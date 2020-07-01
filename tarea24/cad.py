def cad(numero):
    binario = ''
    while numero // 2 != 0:
        binario = str(numero % 2) + binario
        numero = numero // 2
    return str(numero) + binario


while True:
    try:
        numero = int(input("Introduce un numero entero para convertir a binario : "))
        break
    except ValueError:
        print("Oops!  No es un numero entero decimal válido.  Intentalo de nuevo...")
print("El numero en decimal es : ", cad(numero))
