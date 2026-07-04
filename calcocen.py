liczba_ocen = int(input("Ile masz ocen? "))

while liczba_ocen <= 0:
    print("Liczba ocen musi być większa od 0.")
    liczba_ocen = int(input("Ile masz ocen? "))

suma = 0

for i in range(liczba_ocen):
    ocena = float(input("Podaj ocenę: "))

    while ocena < 1 or ocena > 6:
        print("Nieprawidłowa ocena. Podaj ocenę od 1 do 6.")
        ocena = float(input("Podaj ocenę: "))

    suma += ocena

srednia = suma / liczba_ocen

print("Średnia wynosi:", round(srednia, 2))

if srednia < 1.75:
    print("Ocena końcowa: niedostateczny")
elif srednia < 2.75:
    print("Ocena końcowa: dopuszczający")
elif srednia < 3.75:
    print("Ocena końcowa: dostateczny")
elif srednia < 4.75:
    print("Ocena końcowa: dobry")
elif srednia < 5.5:
    print("Ocena końcowa: bardzo dobry")
elif srednia <= 6:
    print("Ocena końcowa: celujący")
else:
    print("Nieprawidłowa średnia")