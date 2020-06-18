#Clase con la que construyo una lista de objetos Vaca
class Vaca():
    def __init__(self, peso=0, litros_dia=0):
        self.peso = peso
        self.litros_dia = litros_dia

    def __repr__(self):
        return "{0}:{1}".format(self.peso, self.litros_dia)

# Funcion recursiva que recorre la lista pasada y en cada nueva llamada recursiva dentro del for que recorre los elementos
# de las listas le voy pasando un elemento menos del principio de la lista actual para esa iteracion
# hasta que me quedo sin elementos en la lista original y devuele de la lista actva un array vacio (condicion para empezar a salir de la recursividad),
# segun van volviendo las llamadas de la recursividad va añadiendo el elemento [0] de cada iteracion recursiva
# que no se ha enviado a la recursividad posterior a cada uno de los elementos de la lista a devolver de la llamada recursiva anterior
# Es decir, al volver de la recursividad va construyendo el array final desde el ultimo elemento hacia atras. en la primera
# salida de la recursividad obtendre el ultimo elemento y el conjunto vacio o array vacio[], en la anterior a esta llamada
# recursiva el anteultimo item de la lista se añadira a cada uno de los elementos de la lista ("subconjunto_anterior") , previamente he
# añadido al "subconjunto_principal" el anterior para no perderlo, y con esta logica hasta salir completamente de todas
# las llamadas recursivas va construyendo el array final añadiendo a la lista que toque  todos los elementos de las listas previas
# de este modo se obtiene una lista con todos los subconjuntos posibles de un conjunto cuyo cardinal de elementos se corresponde con la formula 2^n
# siendo n el numero de elementos en el conjunto.
#PD: la lista es generica se le puede pasar un array de numeros o de cadenasw o lo que quieras para poder debugar y ver como va construyendo el array final
# por ejemplo ejecutando: print(subconjuntos([0,1,2,3,4])
def subconjuntos(lista):
    if len(lista) == 0:
        return [[]]
    else:
        subconjunto_principal = [ ]
        for subconjunto_anterior in subconjuntos(lista[1:]):
            subconjunto_principal += [subconjunto_anterior]
            subconjunto_principal += [[lista[0]] + subconjunto_anterior]
        return subconjunto_principal

if __name__ == "__main__":
    #variables y entrada de datos  mediante for para poblar la lista de vacas
    tara = int(input("Peso maximo admitido del transporte en Kg?: "))
    vacas_disponibles = int(input("numero de vacas disponibles para su transporte?: "))
    lista_vacas = [Vaca for vaca in range(vacas_disponibles)]
    maxima_produccion = 0

    for i in range(0, vacas_disponibles):
        peso_vaca = int(input("Introduce el peso en Kg de la vaca numero " + str(i + 1) + ": "))
        litros_vaca = int(input("Introduce la produccion diaria en litros para la vaca numero " + str(i + 1) + ": "))
        lista_vacas[i] = Vaca(peso_vaca, litros_vaca)

    #llamada a la funcion recursiva para obtener todos los posibles subconjuntos de unconjunto
    combinaciones_vacas = subconjuntos(lista_vacas)

    #En este bucle for recorro todos los subconjunto posibles para las vacas introducidas y compralculo su peso maximo
    # y litros producidos totales para ese comjunto de vacas, mediante la condición me que quedo con el mas alto
    for conjunto in combinaciones_vacas:
        peso_conjunto = 0
        litros_conjunto = 0
        for vaca in conjunto:
            peso_conjunto += vaca.peso
            litros_conjunto += vaca.litros_dia
            if peso_conjunto <= tara and litros_conjunto >= maxima_produccion:
                vacas_seleccionadas = conjunto
                maxima_produccion = litros_conjunto
    #Presentación de los resultados
    print("Las vacas seleccionadas fueron")
    for vacas in vacas_seleccionadas:
        print(vacas)
    print("Y la producción máxima ha conseguir con las vacas y el camion actuales es de : " + str(maxima_produccion) + " litros")