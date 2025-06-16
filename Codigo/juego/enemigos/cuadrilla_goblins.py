import random

def luchar_cuadrilla(jugador):
    vida_enemigo = 10
    ataque_enemigo = 2

    print("\n⚔️ Combate contra la cuadrilla de goblins.")
    while vida_enemigo > 0 and jugador.vida > 0:
        print(f"\nTu vida: {jugador.vida} | Vida goblins: {vida_enemigo}")
        accion = input("¿Atacar (a) o Huir (h)? >> ").lower()

        if accion == "a":
            dano = jugador.fuerza + random.randint(0, 2)
            print(f"Atacas e infliges {dano} de daño.")
            vida_enemigo -= dano
        elif accion == "h":
            print("Intentas huir... ¡pero no puedes!")
        else:
            print("Acción inválida.")
            continue

        if vida_enemigo > 0:
            recibido = ataque_enemigo - jugador.armadura
            recibido = max(1, recibido)
            jugador.vida -= recibido
            print(f"Los goblins te atacan y recibes {recibido} de daño.")

    return jugador.vida > 0
