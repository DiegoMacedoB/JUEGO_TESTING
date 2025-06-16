from escenas.escena_muerte import escena_muerte
from escenas.escena_bosque import escena_bosque
from escenas.escena_cloacas import escena_cloacas
from escenas.escena_techo import escena_techo
from enemigos.rey_goblin import luchar_rey_goblin

def escena_cabania(jugador):
    print("\n🛖 Estás en una cabaña abandonada.")
    print("Tienes tres posibles salidas:")
    print("1. Romper la puerta de piedra (requiere fuerza >= 6)")
    print("2. Buscar un escape debajo de la cama (requiere inteligencia >= 6)")
    print("3. Escalar por el techo (requiere agilidad >= 6)")
    eleccion = input(">> ")

    if eleccion == "1":
        if jugador.fuerza >= 6:
            print("¡Rompiste la puerta y escapaste al bosque!")
            escena_bosque(jugador)
        else:
            print("No pudiste romper la puerta... ¡y el Rey Goblin te ataca!")
            if not luchar_rey_goblin(jugador):
                escena_muerte(jugador)
    elif eleccion == "2":
        if jugador.inteligencia >= 6:
            print("Encontraste una trampilla y escapaste a las cloacas.")
            escena_cloacas(jugador)
        else:
            print("No hallaste nada... ¡y el Rey Goblin aparece!")
            if not luchar_rey_goblin(jugador):
                escena_muerte(jugador)
    elif eleccion == "3":
        if jugador.agilidad >= 6:
            print("Escalaste exitosamente el techo.")
            escena_techo(jugador)
        else:
            print("Te resbalas... ¡y el Rey Goblin te enfrenta!")
            if not luchar_rey_goblin(jugador):
                escena_muerte(jugador)
    else:
        print("Opción inválida. Intenta de nuevo.")
        escena_cabania(jugador)
