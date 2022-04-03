def maximiza_produccion(pesos_vacas, litros_vacas, tara_camion):
    n = len(pesos_vacas)
    ant = [[0, []] for m in range(tara_camion + 1)]
    for i in range(1, n + 1):
        act = [[0, [0 for j in range(i)]]]
        for m in range(1, tara_camion + 1):
            if pesos_vacas[i - 1] <= m and litros_vacas[i - 1] + ant[m - pesos_vacas[i - 1]][0] > ant[m][0]:
                act.append([litros_vacas[i - 1] + ant[m - pesos_vacas[i - 1]][0], ant[m - pesos_vacas[i - 1]][1][:] + [1]])
            else:
                act.append([ant[m][0], ant[m][1][:] + [0]])
        ant = act
    return act[tara_camion]

def borra_valores_lista(lista, valores):
    values_as_set = set(valores)
    return [x for x in lista if x not in values_as_set]


if __name__ == "__main__":
    # variables y entrada de datos  mediante for para poblar la lista de vacas
    tara = int(input("Peso maximo admitido del transporte en Kg?: "))
    vacas_disponibles = int(input("numero de vacas disponibles para su transporte?: "))
    pesos_vacas = [0 for i in range(vacas_disponibles)]
    litros_vacas = [0 for i in range(vacas_disponibles)]

    for i in range(0, vacas_disponibles):
        peso_vaca = int(input("Introduce el peso en Kg de la vaca numero " + str(i + 1) + ": "))
        litros_vaca = int(input("Introduce la produccion diaria en litros para la vaca numero " + str(i + 1) + ": "))
        pesos_vacas[i] = peso_vaca
        litros_vacas[i] = litros_vaca

    lista_vacas_seleccionadas = maximiza_produccion(pesos_vacas, litros_vacas, tara)
    pesos_vacas_seleccionadas = [0 for i in range(len(lista_vacas_seleccionadas[1]))]

    print("La maxima produccion de leche para estas vacas es: ", lista_vacas_seleccionadas[0])
    for i in range(len(lista_vacas_seleccionadas[1])):
        if lista_vacas_seleccionadas[1][i] == 1:
            pesos_vacas_seleccionadas[i] = pesos_vacas[i]
    print("Hay que seleccionar las vacas de pesos : ", borra_valores_lista(pesos_vacas_seleccionadas,[0]))
