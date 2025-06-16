import tkinter as tk
from PIL import Image, ImageTk
import os
from juego.escenas import escena_bosque, escena_cloacas, escena_techo

def mostrar_intro(jugador):
    def ir_bosque():
        intro.destroy()
        escena_bosque.iniciar_bosque(jugador)

    def ir_cloacas():
        intro.destroy()
        escena_cloacas.iniciar_cloacas(jugador)

    def ir_techo():
        intro.destroy()
        escena_techo.iniciar_techo(jugador)

    intro = tk.Tk()
    intro.title("Inicio de la Aventura")
    intro.geometry("800x600")

    # Cargar imagen
    imagen_path = os.path.join("assets", "cabania.png")
    imagen = Image.open(imagen_path)
    imagen = imagen.resize((300, 200))  # Ajusta tamaño
    imagen_tk = ImageTk.PhotoImage(imagen)

    # Mostrar imagen
    imagen_label = tk.Label(intro, image=imagen_tk)
    imagen_label.image = imagen_tk  # Mantener referencia
    imagen_label.pack(pady=10)

    # Mensaje de introducción
    mensaje = f"""Has elegido ser un {jugador.clase}.\n
Estás en una cabaña con tres salidas:\n
1. Romper la puerta de piedra (Bosque).\n
2. Escapar por una trampilla bajo la cama (Cloacas).\n
3. Subir por el techo (Techo)."""
    label = tk.Label(intro, text=mensaje, font=("Arial", 14), wraplength=600, justify="left")
    label.pack(pady=20)

    # Botones de decisión
    tk.Button(intro, text="Ir al bosque", command=ir_bosque).pack(pady=5)
    tk.Button(intro, text="Ir a las cloacas", command=ir_cloacas).pack(pady=5)
    tk.Button(intro, text="Subir al techo", command=ir_techo).pack(pady=5)

    intro.mainloop()
