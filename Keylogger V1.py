import tkinter as tk

def tecla_presionada(event):
    print("Tecla:", event.keysym)

ventana = tk.Tk()
ventana.title("Keylogger v.1")
ventana.geometry("500x300")

titulo = tk.Label(
    ventana,
    text="Keylogger - Ciberseguridad",
    font=("Arial", 18, "bold")
)
titulo.pack(pady=(30, 5))

autor = tk.Label(
    ventana,
    text="Autor: J. Andrés Chavarría",
    font=("Arial", 11)
)
autor.pack()

texto = tk.Label(
    ventana,
    text="Haz clic aquí y presiona algunas teclas",
    font=("Arial", 14)
)
texto.pack(pady=80)

ventana.bind("<KeyPress>", tecla_presionada)

ventana.mainloop()