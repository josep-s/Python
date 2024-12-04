def main():
    try:
        # Demana a l'usuari que introdueixi un número
        num = int(input("Introdueix un número: "))

        # Comprova si el número és parell o senar
        if num % 2 == 0:
            print(f"{num} és un número parell.")
        else:
            print(f"{num} és un número senar.")
    except ValueError:
        print("Entrada no vàlida. Si us plau, introdueix un enter vàlid.")

if __name__ == "__main__":
    main()
