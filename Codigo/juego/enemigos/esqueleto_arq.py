import random

def luchar_esqueleto_arquero(jugador):
    vida_enemigo = 10
    ataque_enemigo = 3

    print("\n💀 Combate contra el Esqueleto Arquero.")
    while vida_enemigo > 0 and jugador.vida > 0:
        print(f"\nTu vida: {jugador.vida} | Vida del esqueleto: {vida_enemigo}")
        accion = input("¿Atacar (a) o Cubrirse (c)? >> ").lower()

        if accion == "a":
            dano = jugador.agilidad + random.randint(0, 2)
            print(f"Disparas con rapidez e infliges {dano} de daño.")
            vida_enemigo -= dano
        elif accion == "c":
            print("Te cubres parcialmente, recibiendo menos daño.")
            recibido = max(0, ataque_enemigo - jugador.armadura - 2)
        else:
            print("Acción no válida.")
            continue

        if vida_enemigo > 0:
            if accion != "c":
                recibido = max(1, ataque_enemigo - jugador.armadura)
            jugador.vida -= recibido
            print(f"El esqueleto te dispara una flecha. Recibes {recibido} de daño.")

    return jugador.vida > 0
