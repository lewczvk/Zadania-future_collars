#ZADANIE PROSTY SYSTEM KSIĘGOWY
#Napisz program, który będzie rejestrował operacje na koncie firmy i stan magazynu.
# Program po uruchomieniu wyświetla informację o dostępnych komendach:
#
# saldo
# sprzedaż
# zakup
# konto
# lista
# magazyn
# przegląd
# koniec
#
# Po wprowadzeniu odpowiedniej komendy, aplikacja zachowuje się w unikalny sposób dla każdej z nich:
#
# saldo - Program pobiera kwotę do dodania lub odjęcia z konta.
# sprzedaż - Program pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt musi znajdować się w magazynie. Obliczenia respektuje względem konta i magazynu (np. produkt "rower" o cenie 100 i jednej sztuce spowoduje odjęcie z magazynu produktu "rower" oraz dodanie do konta kwoty 100).
# zakup - Program pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt zostaje dodany do magazynu, jeśli go nie było. Obliczenia są wykonane odwrotnie do komendy "sprzedaz". Saldo konta po zakończeniu operacji „zakup” nie może być ujemne.
# konto - Program wyświetla stan konta.
# lista - Program wyświetla całkowity stan magazynu wraz z cenami produktów i ich ilością.
# magazyn - Program wyświetla stan magazynu dla konkretnego produktu. Należy podać jego nazwę.
# przegląd - Program pobiera dwie zmienne „od” i „do”, na ich podstawie wyświetla wszystkie wprowadzone akcje zapisane pod indeksami od „od” do „do”. Jeżeli użytkownik podał pustą wartość „od” lub „do”, program powinien wypisać przegląd od początku lub/i do końca. Jeżeli użytkownik podał zmienne spoza zakresu, program powinien o tym poinformować i wyświetlić liczbę zapisanych komend (żeby pozwolić użytkownikowi wybrać odpowiedni zakres).
# koniec - Aplikacja kończy działanie.
#
# Dodatkowe wymagania:
#
# Aplikacja od uruchomienia działa tak długo, aż podamy komendę "koniec".
# Komendy saldo, sprzedaż i zakup są zapamiętywane przez program, aby móc użyć komendy "przeglad".
# Po wykonaniu dowolnej komendy (np. "saldo") aplikacja ponownie wyświetla informację o dostępnych komendach, a także prosi o wprowadzenie jednej z nich.
# Zadbaj o błędy, które mogą się pojawić w trakcie wykonywania operacji (np. przy komendzie "zakup" jeśli dla produktu podamy ujemną kwotę, aplikacja powinna wyświetlić informację o niemożności wykonania operacji i jej nie wykonać). Zadbaj też o prawidłowe typy danych.

saldo_firmy = 50000.0

produkty = [
 {"nazwa_produktu": "pralka",
  "cena_produktu": 1999.99,
  "liczba_sztuk": 6},

{"nazwa_produktu": "telewizor",
  "cena_produktu": 4499.99,
  "liczba_sztuk": 5},

 {"nazwa_produktu": "lodowka",
   "cena_produktu": 3599.99,
   "liczba_sztuk": 4},

 {"nazwa_produktu": "piekarnik",
   "cena_produktu": 2999.99,
   "liczba_sztuk": 7},

 {"nazwa_produktu": "zamrazarka",
   "cena_produktu": 1599.99,
   "liczba_sztuk": 6},

 {"nazwa_produktu": "laptop",
   "cena_produktu": 3999.99,
   "liczba_sztuk": 5},

 {"nazwa_produktu": "glosnik",
  "cena_produktu": 599.99,
  "liczba_sztuk": 8},

 {"nazwa_produktu": "zegarek",
  "cena_produktu": 899.99,
  "liczba_sztuk": 10}]

historia = ["Dodano nowy produkt 'pralka'" , "Zakupiono 2 produkty 'telewizor'", "Sprzedano produkt o nazwie 'piekarnik'" ]


while True:
 wprowadzenie_komendy = input("""
      Wybierz jedną komendę:
      1. saldo
      2. sprzedaż
      3. zakup
      4. konto
      5. lista
      6. magazyn
      7. przeglad
      8. koniec
      Podaj numer komendy: """)

 match wprowadzenie_komendy:
    case "1":
        srodki = float(input("Podaj kwotę do dodania lub odjęcia: "))
        if saldo_firmy + srodki < 0:
           print("Saldo nie może być ujemne.")
        else:
           saldo_firmy += srodki
           print(f"Aktualne saldo firmy: {saldo_firmy:.2f} PLN.")

    case "2":
        nazwy_produktow = input("Nazwa produktu do sprzedaży: ")
        cena_produktu = None
        liczba_sztuk = None
        try:
            cena_produktu = float(input("Cena produktu do sprzedaży: "))
            liczba_sztuk = int(input("Liczba sztuk do sprzedaży: "))
            if liczba_sztuk < 0:
                cena_produktu = None
                liczba_sztuk = None
                print("Nie możesz wybrać wartości ujemnej.")
        except:
            print("Znaki muszą być cyframi.")
        if cena_produktu is not None and liczba_sztuk is not None:
            znaleziony_produkt = False
            for produkt in produkty:
                if produkt.get("nazwa_produktu") == nazwy_produktow:
                    znaleziony_produkt = True
                    if liczba_sztuk > produkt["liczba_sztuk"]:
                        print("Nie ma tego produktu do sprzedaży.")
                        break
                    produkt["liczba_sztuk"] -= liczba_sztuk
                    saldo_firmy += cena_produktu * liczba_sztuk

            if not znaleziony_produkt:
                print("Nie ma tego produktu do sprzedaży.")

    case "3":
        nazwa_produktu = input("Podaj nazwę produktu: ")
        cena_produktu = float(input("Podaj cenę produktu: "))
        liczba_sztuk = int(input("Podaj liczbę produktu: "))
        if saldo_firmy - (cena_produktu * liczba_sztuk) < 0:
            print("Nie możesz mieć salda w wartości ujemnej.")
            continue
        else:
            saldo_firmy -= cena_produktu * liczba_sztuk
        produkty.append({
            "nazwa_produktu": nazwa_produktu,
            "cena_produktu": cena_produktu,
            "liczba_sztuk": liczba_sztuk,
        })


    case "4":
        print(f"Aktualne saldo firmy: {saldo_firmy} PLN.")

    case "5":
        print("Całkowity stan magazynu: ")
        print(produkty)

    case "6":
        nazwa_produktu = input("Nazwa produktu w magazynie: ")
        znaleziony_produkt = False
        for produkt in produkty:
                if produkt.get("nazwa_produktu") == nazwa_produktu:
                    znaleziony_produkt = True
                    print(f"Znaleziono produkt w magazynie: {produkt}")
                    break
        if not znaleziony_produkt:
            print("Nie znaleziono takiego produktu w magazynie.")

    case "7":
        od = input("Podaj wartość 'od'(nie musisz nic podawać): ")
        do = input("Podaj wartość'do'(nie musisz nic podawać): ")
        if od:
            od = int(od)
        else:
            od = 0
        if do:
            do = int(do)
        else:
            do = len(historia)
        print(f"Przegląd: {historia[od:do]} ")
    case "8":
        print("Koniec działania programu.")
        break


