# ZADANIE PROGRAM DO BAZY SZKOLNEJ
from unittest import case


# Utwórz program do zarządzania bazą szkolną. Istnieje możliwość tworzenia trzech typów użytkowników (uczeń, nauczyciel, wychowawca) a także zarządzania nimi.
#
# Po uruchomieniu programu można wpisać jedną z następujących komend: utwórz, zarządzaj, koniec.
#
# Polecenie "utwórz" - Przechodzi do procesu tworzenia użytkowników.
# Polecenie "zarządzaj" - Przechodzi do procesu zarządzania użytkownikami.
# Polecenie "koniec" - Kończy działanie aplikacji.
#
# Proces tworzenia użytkowników:
#
# Należy wpisać opcję, którą chcemy wybrać: uczeń, nauczyciel, wychowawca, koniec. Po wykonaniu każdej z opcji (oprócz "koniec") wyświetla to menu ponownie.
# Polecenie "uczeń" - Należy pobrać imię i nazwisko ucznia (jako jedna zmienna, można pobrać je jako dwie zmienne, jeżeli zostanie to poprawnie obsłużone) oraz nazwę klasy (np. "3C")
# Polecenie "nauczyciel" - Należy pobrać imię i nazwisko nauczyciela (jako jedna zmienna, labo dwie, jeżeli zostanie to poprawnie obsłużone), nazwę przedmiotu prowadzonego, a następnie w nowych liniach nazwy klas, które prowadzi nauczyciel, aż do otrzymania pustej linii.
# Polecenie "wychowawca" - Należy pobrać imię i nazwisko wychowawcy (jako jedna zmienna, albo dwie, jeżeli zostanie to poprawnie obsłużone), a także nazwę prowadzonej klasy.
# Polecenie "koniec" - Wraca do pierwszego menu.
#
# Proces zarządzania użytkownikami:
#
# Należy wpisać opcję, którą chcemy wybrać: klasa, uczen, nauczyciel, wychowawca, koniec. Po wykonaniu każdej z opcji (oprócz "koniec") wyświetla to menu ponownie.
# Polecenie "klasa" - Należy pobrać klasę, którą chcemy wyświetlić (np. "3C") program ma wypisać wszystkich uczniów, którzy należą do tej klasy, a także wychowawcę tejże klasy.
# Polecenie "uczeń" - Należy pobrać imię i nazwisko uczenia, program ma wypisać wszystkie lekcje, które ma uczeń a także nauczycieli, którzy je prowadzą.
# Polecenie "nauczyciel" - Należy pobrać imię i nazwisko nauczyciela, program ma wypisać wszystkie klasy, które prowadzi nauczyciel.
# Polecenie "wychowawca" - Należy pobrać imię i nazwisko wychowawcy, a program ma wypisać wszystkich uczniów, których prowadzi wychowawca.
# Polecenie "koniec" - Wraca do pierwszego menu.


class Uczen:
    def __init__(self, imie, nazwisko, nazwa_klasy):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nazwa_klasy = nazwa_klasy

    def __repr__(self):
        return f"Uczeń {self.imie} {self.nazwisko} z klasy {self.nazwa_klasy}."

class Nauczyciel:
    def __init__(self, imie, nazwisko, nazwa_przedmiotu, nazwy_klas_prowadzonych):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nazwa_przedmiotu = nazwa_przedmiotu
        self.nazwy_klas_prowadzonych = nazwy_klas_prowadzonych

    def __repr__(self):
        return f"Nauczyciel {self.imie} {self.nazwisko} uczący {self.nazwa_przedmiotu} i prowadzący klasy {self.nazwy_klas_prowadzonych}."

class Wychowawca:
    def __init__(self, imie, nazwisko, nazwa_prowadzonej_klasy):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nazwa_prowadzonej_klasy = nazwa_prowadzonej_klasy

    def __repr__(self):
        return f"Wychowawca {self.imie} {self.nazwisko} prowadzący klasy {self.nazwa_prowadzonej_klasy}."

szkoła = {
    "uczniowie": [
        Uczen("Adam", "Adamczyk", "4c"),
        Uczen("Bartosz", "Bóbr", "5a"),
        Uczen("Cezary", "Czub", "6b"),
    ],
    "nauczyciele": [
        Nauczyciel("Dariusz", "Dąbrowski", "matematyka", ["3c", "4a", "5b"]),
        Nauczyciel("Ewa", "Ejsmont", "język polski", ["2c", "5a", "4c", "2b"]),
        Nauczyciel("Fabian", "Franciszkiewicz", "wychowanie fizyczne", ["5c", "1a", "6b"] ),
    ],
    "wychowawcy": [
        Wychowawca("Grażyna", "Gołąb", "4c"),
        Wychowawca("Henryk", "Hofman", "5a"),
        Wychowawca("Irena", "Irmanowicz", "6b")
    ],
}

def wyszukaj_uczniów(szkoła, nazwa_klasy):
    uczniowie = []
    for uczen in szkoła:
        if uczen.nazwa_klasy == nazwa_klasy:
            uczniowie.append(uczen)
    return uczniowie

def wyszukaj_lekcje_ucznia(imie_ucznia, nazwisko_ucznia, szkoła):
    nazwa_klasy = None
    lista_przedmiotow = []
    for uczen in szkoła.get("uczniowie"):
        if uczen.imie == imie_ucznia and uczen.nazwisko == nazwisko_ucznia:
            nazwa_klasy = uczen.nazwa_klasy
    for nauczyciel in szkoła.get("nauczyciele"):
        if nazwa_klasy in nauczyciel.nazwy_klas_prowadzonych:
            lista_przedmiotow.append(nauczyciel.nazwa_przedmiotu)
    return lista_przedmiotow

def wyszukaj_wszystkie_klasy_nauczyciela(imie_nauczyciela, nazwisko_nauczyciela):
    lista_klas_nauczyciela = []
    for nauczyciel in szkoła.get("nauczyciele"):
        if nauczyciel.imie == imie_nauczyciela and nazwisko_nauczyciela == nazwisko_nauczyciela:
            lista_klas_nauczyciela.append(nauczyciel.nazwy_klas_prowadzonych)
    return lista_klas_nauczyciela

def wyszukaj_wszystkich_uczniow_wychowawcy(imie_wychowawcy, nazwisko_wychowawcy):
    lista_uczniow_wychowawcy = []
    for wychowawca in szkoła.get("wychowawcy"):
        if wychowawca.imie == imie_wychowawcy and nazwisko_wychowawcy == nazwisko_wychowawcy:
            nazwa_prowadzonej_klasy = wychowawca.nazwa_prowadzonej_klasy
    for uczen in szkoła.get("uczniowie"):
        if nazwa_prowadzonej_klasy == uczen.nazwa_klasy:
            lista_uczniow_wychowawcy.append(uczen)
    return lista_uczniow_wychowawcy






while True:
    wybor_uzytkownika = input("Wybierz opcję:\n1. Dodaj\n2. Zarządzaj\n3. Zakończ\n")
    if wybor_uzytkownika == "1":
        obiekt_do_dodania =input("Co chcesz dodać?\n1. Uczen\n2. Nauczyciel\n3. Wychowawca")
        match obiekt_do_dodania:
            case "1":
                imie_ucznia = input("Podaj imię ucznia: ")
                nazwisko_ucznia = input("Podaj nazwisko ucznia: ")
                nazwa_klasy = input("Podaj nazwę klasy ucznia: ")
                uczen = Uczen(imie_ucznia, nazwisko_ucznia, nazwa_klasy)
                szkoła["uczniowie"].append(uczen)
            case "2":
                lista_klas = []
                while True:
                    klasy = input("Podaj klasy: ")
                    if not klasy:
                        break
                    else:
                        lista_klas.append(klasy)
                imie = input("Podaj imie: ")
                nazwisko = input("Podaj nazwisko: ")
                nazwa_przedmiotu = input("Podaj nazwę przedmiotu: ")
                klasa = Nauczyciel(imie=imie, nazwisko=nazwisko, nazwa_przedmiotu=nazwa_przedmiotu, nazwy_klas_prowadzonych=lista_klas)
                szkoła["nauczyciele"].append(klasa)


            case "3":
                imie_wychowawcy = input("Podaj imię wychowawcy: ")
                nazwisko_wychowawcy = input("Podaj nazwisko wychowawcy: ")
                nazwa_prowadzonej_klasy = input("Podaj nazwę klasy prowadzonej przez wychowawcę: ")
                wychowawca = Wychowawca(imie_wychowawcy, nazwisko_wychowawcy, nazwa_prowadzonej_klasy)
                szkoła["wychowawcy"].append(wychowawca)


    elif wybor_uzytkownika == "2":
        opcja_do_edycji = input("Czym chcesz zarządzać?\n1. Klasa\n2. Uczen\n3. Nauczyciel\n4. Wychowawca\n")

        match opcja_do_edycji:
            case "1":
                nazwa_klasy = input("Podaj nazwę klasy: ")
                uczniowie = wyszukaj_uczniów(szkoła.get("uczniowie"), nazwa_klasy=nazwa_klasy)
                print(f"Uczniowie danej klasy to: {uczniowie}")
            case "2":
                imie_ucznia = input("Podaj imie ucznia: ")
                nazwisko_ucznia = input("Podaj nazwisko ucznia: ")
                lista_przedmiotów = wyszukaj_lekcje_ucznia(imie_ucznia, nazwisko_ucznia, szkoła)
                print(f"Wszystkie przedmioty ucznia to: {lista_przedmiotów}.")
            case "3":
                imie_nauczyciela = input("Podaj imie nauczyciela: ")
                nazwisko_nauczyciela = input("Podaj nazwisko nauczyciela: ")
                lista_klas_nauczyciela = wyszukaj_wszystkie_klasy_nauczyciela(imie_nauczyciela, nazwisko_nauczyciela)
                print(f"Klasy prowadzone przez danego nauczyciela to: {lista_klas_nauczyciela}.")
            case "4":
                imie_wychowawcy = input("Podaj imie wychowawcy: ")
                nazwisko_wychowawcy = input("Podaj nazwisko wychowawcy: ")
                lista_uczniow_wychowawcy = wyszukaj_wszystkich_uczniow_wychowawcy(imie_wychowawcy=imie_wychowawcy, nazwisko_wychowawcy=nazwisko_wychowawcy)
                print(f"Lista uczniów danego wychowawcy: {lista_uczniow_wychowawcy}.")

    elif wybor_uzytkownika == "3":
        break









