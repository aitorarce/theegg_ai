class Vaca():
    def __init__(self, peso=0, litros_dia=0):
        self.peso = peso
        self.litros_dia = litros_dia

    def __repr__(self):
        return "{0}:{1}".format(self.peso, self.litros_dia)

#Funcion recursiva que recorre la lista y en cada nueva llamada por cada elemento va añadiendo al subconjunto anterior
def subconjuntos(lista):
    if len(lista) == 0:
        return [[]]
    else:
        subconjunto_principal = [ ]
        for subconjunto_anterior in subconjuntos(lista[1:]):
            subconjunto_principal += [subconjunto_anterior]
            subconjunto_principal += [[lista[0]] + subconjunto_anterior]
        return subconjunto_principal

tara = int(input("Peso maximo admitido del transporte en Kg?: "))
vacas_disponibles = int(input("numero de vacas disponibles para su transporte?: "))
lista_vacas = [Vaca for vaca in range(vacas_disponibles)]

for i in range(0, vacas_disponibles):
    peso_vaca = int(input("Introduce el peso en Kg de la vaca numero " + str(i + 1) + ": "))
    litros_vaca = int(input("Introduce la produccion diaria en litros para la vaca numero " + str(i + 1) + ": "))
    lista_vacas[i] = Vaca(peso_vaca, litros_vaca)

combinaciones_vacas = subconjuntos(lista_vacas)
maxima_produccion = 0
for conjunto in combinaciones_vacas:
    peso_conjunto = 0
    litros_conjunto = 0
    for vaca in conjunto:
        peso_conjunto += vaca.peso
        litros_conjunto += vaca.litros_dia
        if peso_conjunto <= tara and litros_conjunto >= maxima_produccion:
            vacas_seleccionadas = conjunto
            maxima_produccion = litros_conjunto
print("Las vacas seleccionadas fueron")
for vacas in vacas_seleccionadas:
    print(vacas)
print("Y la producción máxima ha conseguir con las vacas y el camion actuales es de : " + str(maxima_produccion) + "litros")