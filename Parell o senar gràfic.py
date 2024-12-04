import tkinter as tk
from tkinter import simpledialog

def main():
    # Crea la finestra principal
    root = tk.Tk()
    root.iconify()  # Minimitza la finestra principal

    try:
        # Demana a l'usuari un número
        num = simpledialog.askinteger("Introdueix un Número", "Si us plau, introdueix un enter:")

        if num is not None:
            # Crea una nova finestra per mostrar el resultat
            result_window = tk.Toplevel(root)
            result_window.title("Resultat")

            # Comprova si el número és parell o senar
            if num % 2 == 0:
                message = f"{num} és un número parell."
            else:
                message = f"{num} és un número senar."

            # Mostra el missatge en un quadre de text
            label = tk.Label(result_window, text=message)
            label.pack(padx=20, pady=20)
        else:
            # Mostra un missatge d'error si no s'ha proporcionat una entrada vàlida
            error_window = tk.Toplevel(root)
            error_window.title("Error")
            label = tk.Label(error_window, text="No s'ha proporcionat una entrada vàlida.")
            label.pack(padx=20, pady=20)
    except ValueError:
        # Mostra un missatge d'error si l'entrada no és vàlida
        error_window = tk.Toplevel(root)
        error_window.title("Error")
        label = tk.Label(error_window, text="Entrada no vàlida. Si us plau, introdueix un enter vàlid.")
        label.pack(padx=20, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
