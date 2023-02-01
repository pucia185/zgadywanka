import random


def main():
    print("""  ___________          _____  _   _ _____     _      _      _____ _____ __________  ______ 
 |___  / ____|   /\   |  __ \| \ | |_   _|   | |    | |    |_   _/ ____|___  /  _ \|  ____|
    / / |  __   /  \  | |  | |  \| | | |     | |    | |      | || |       / /| |_) | |__   
   / /| | |_ | / /\ \ | |  | | . ` | | | _   | |    | |      | || |      / / |  _ <|  __|  
  / /_| |__| |/ ____ \| |__| | |\  |_| || |__| |    | |____ _| || |____ / /__| |_) | |____ 
 /_____\_____/_/    \_\_____/|_| \_|_____\____/     |______|_____\_____/_____|____/|______|

 """)

    print("""
          Wybieram liczbe calkowita od 1 do 100"

          """)
    losowy_numer = random.randint(1, 100)
    proba = None
    while proba != losowy_numer:
        try:
            proba = int(input("Jaka jest moja liczba? : "))
            if proba < 1 or proba > 100:
                print('Wpisz liczbe calkowita od 1 do 100')
                continue
        except ValueError:
            print('Wpisz liczbe calkowita od 1 do 100')
            continue
        if proba < losowy_numer:
            print("Za niska.")
        elif proba > losowy_numer:
            print("Za wysoka.")
    print("Brawo, to jest wybrany numer!", losowy_numer)


if __name__ == '__main__':
    main()
