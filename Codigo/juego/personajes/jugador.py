class Jugador:
    def __init__(self, clase):
        self.clase = clase
        self.nivel = 1
        self.exp = 0
        self.oro = 10
        self.vida_max = 5
        self.vida = 5
        self.cordura_max = 5
        self.cordura = 5
        self.armadura = 0

        if clase == "Arquero":
            self.fuerza = 3
            self.agilidad = 7
            self.inteligencia = 5
        elif clase == "Berserker":
            self.fuerza = 7
            self.agilidad = 4
            self.inteligencia = 3
        elif clase == "Mago":
            self.fuerza = 3
            self.agilidad = 4
            self.inteligencia = 8
        else:
            self.fuerza = 5
            self.agilidad = 5
            self.inteligencia = 5
