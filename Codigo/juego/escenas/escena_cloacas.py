from enemigos.babosa import luchar_babosa
from escenas.escena_tapiota import escena_tapiota
from escenas.escena_muerte import escena_muerte

def escena_cloacas(jugador):
    print("\n🕳️ Te metes por un agujero bajo la cama y caes en unas cloacas húmedas.")
    print("Una babosa gigante aparece frente a ti.")

    if luchar_babosa(jugador):
        print("¡Has vencido a la babosa!")
        jugador.exp += 3
        jugador.oro += 5
        escena_tapiota(jugador)
    else:
        escena_muerte(jugador)
