liczba_elementow = int(input("Podaj liczbę elementów: "))

liczba_paczek = 1

waga_paczki = 0

waga_ogólna = 0

waga_najlzejszej_paczki = 20

numer_najlzejszej_paczki = 1

for i in range(liczba_elementow):
    waga_elementu = int(input("Podaj liczbę wysłanej paczki w kilogramach: "))
    if waga_elementu > 10 or waga_elementu < 1:
        break
    waga_ogólna += waga_elementu
    waga_paczki += waga_elementu

    if waga_paczki > 20:
        if waga_najlzejszej_paczki > waga_paczki - waga_elementu:
            waga_najlzejszej_paczki = waga_paczki - waga_elementu
            numer_najlzejszej_paczki = liczba_paczek

        liczba_paczek += 1
        waga_paczki = waga_elementu

if waga_najlzejszej_paczki > waga_paczki:
    waga_najlzejszej_paczki = waga_paczki
    numer_najlzejszej_paczki = liczba_paczek

suma_pustych_kilogramów = liczba_paczek * 20 - waga_ogólna
print(suma_pustych_kilogramów)
print(numer_najlzejszej_paczki)
print(waga_najlzejszej_paczki)








print(waga_ogólna)
print(liczba_paczek)












