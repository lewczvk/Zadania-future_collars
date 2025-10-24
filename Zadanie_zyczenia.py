imie = input("Podaj imie: ")

rok_obecny = 2025
rok_urodzenia = int(input("Podaj rok urodzenia: "))

wiek: int= rok_obecny - rok_urodzenia

spersonalizowana_wiadomosc = "Mocno ściskam!"
imie_nadawcy = "Wika"


print(imie)
print(rok_urodzenia)

print(imie + ", wszystkiego najlepszego z okazji " + (str(wiek) + " urodzin!"))

print(spersonalizowana_wiadomosc)
print(imie_nadawcy)

