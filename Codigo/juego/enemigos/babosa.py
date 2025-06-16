import random

def luchar_babosa(jugador):
    vida_enemigo = 6
    ataque_enemigo = 1

    print("\n🟢 Combate contra la babosa gigante.")
    while vida_enemigo > 0 and jugador.vida > 0:
        print(f"\nTu vida: {jugador.vida} | Vida babosa: {vida_enemigo}")
        accion = input("¿Atacar (a) o Huir (h)? >> ").lower()

        if accion == "a":
            dano = jugador.inteligencia + random.randint(0, 2)
            print(f"Atacas con astucia y haces {dano} de daño.")
            vida_enemigo -= dano
        elif accion == "h":
            print("Intentas huir... pero la baba te atrapa.")
        else:
            print("Acción inválida.")
            continue

        if vida_enemigo > 0:
            recibido = ataque_enemigo - jugador.armadura
            recibido = max(1, recibido)
            jugador.vida -= recibido
            print(f"La babosa te golpea con baba ácida. Recibes {recibido} de daño.")

    return jugador.vida > 0
