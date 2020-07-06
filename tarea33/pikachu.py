class pokemon:
    vida = 100
    def __init__(self, nombre, ataque):
        self.nombre = nombre
        self.ataque = ataque


    def win(self):
        print("Ha ganado : ", self.nombre)


if __name__ == "__main__":
    turno = 1
    pikachu = pokemon("pikachu",55)
    jigglypuff = pokemon("jigglypuff",45)
    while jigglypuff.vida > 0 and pokemon.vida > 0:
        if turno == 1:
            jigglypuff.vida -= pikachu.ataque
            turno = 0
        else:
            pokemon.vida -= jigglypuff.ataque
            turno = 1
    if pikachu.vida <= 0:
        jigglypuff.win()
    else:
        pikachu.win()
