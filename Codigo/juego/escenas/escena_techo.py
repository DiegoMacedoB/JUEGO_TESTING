from enemigos.esqueleto_arquero import luchar_esqueleto_arquero
from escenas.escena_muerte import escena_muerte
from escenas.escena_fin import escena_fin

def escena_techo(jugador):
    print("\n⬆️ Escalas por una rendija hacia el techo de la cabaña.")
    print("Desde las alturas, un esqueleto con arco te apunta en silencio...")

    if luchar_esqueleto_arquero(jugador):
        print("¡El esqueleto cae hecho polvo tras tu ataque!")
        jugador.exp += 4
        jugador.oro += 8
        escena_fin(jugador)
    else:
        escena_muerte(jugador)
