def escena_tienda(jugador):
    print("\n🏪 Llegaste a una tienda misteriosa.")
    print("Puedes comprar UN artículo con tu oro actual.")
    print(f"Tienes {jugador.oro} de oro.")
    
    articulos = {
        "1": ("Espada afilada (+2 fuerza)", "fuerza", 2, 10),
        "2": ("Armadura ligera (+1 armadura)", "armadura", 1, 8),
        "3": ("Botas elásticas (+2 agilidad)", "agilidad", 2, 10),
        "4": ("Amuleto mágico (+2 inteligencia)", "inteligencia", 2, 10),
        "5": ("Poción de salud (+3 vida)", "vida", 3, 5)
    }

    for clave, (nombre, _, _, precio) in articulos.items():
        print(f"{clave}. {nombre} - {precio} oro")

    eleccion = input("Elige el número del artículo >> ")

    if eleccion in articulos:
        nombre, atributo, cantidad, precio = articulos[eleccion]
        if jugador.oro >= precio:
            jugador.oro -= precio
            if atributo == "vida":
                jugador.vida = min(jugador.vida_max, jugador.vida + cantidad)
            else:
                setattr(jugador, atributo, getattr(jugador, atributo) + cantidad)
            print(f"Compraste {nombre}.")
        else:
            print("No tienes suficiente oro.")
    else:
        print("Elección inválida. No compraste nada.")

    print("\nContinuará en la siguiente versión del juego...")
    print("🏁 Fin del demo.")
