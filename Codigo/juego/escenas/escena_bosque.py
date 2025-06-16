from enemigos.cuadrilla import luchar_cuadrilla
from escenas.escena_tienda import escena_tienda
from escenas.escena_muerte import escena_muerte

def escena_bosque(jugador):
    print("\n🌲 Has llegado al bosque.")
    print("Una cuadrilla de goblins te embosca.")

    if luchar_cuadrilla(jugador):
        print("¡Has vencido a la cuadrilla de goblins!")
        jugador.exp += 5
        jugador.oro += 10
        escena_tienda(jugador)
    else:
        escena_muerte(jugador)
