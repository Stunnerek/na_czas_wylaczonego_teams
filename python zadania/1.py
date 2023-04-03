wybrane_pole = input("wybierz czego chcesz pole")
print (wybrane_pole)
if wybrane_pole == "kwadrat":
    podstawa = input("podaj podstawę")
   
    pole = int(podstawa) * int(podstawa)
    print ("oto pole kwadrata" + str(pole))
elif wybrane_pole == "trojkat":
    podstawa = input("podaj podstawę")
    wysokosc = input("podaj wysokosc")
    pole = int(podstawa) * int(wysokosc) /2
    print ("oto pole trojkata" + str(pole))
elif wybrane_pole == "trapez":
    podstawa = input("podaj podstawę pierwsza")
    podstawa_gorna = input("podaj podstawe drugą")
    wysokosc = input("podaj wysokosc")
    pole_1 = int(podstawa) * int(podstawa_gorna)
    pole_2 = (int(wysokosc)* pole_1 /2)
    print ("oto pole trapeza" + str(pole_2))
elif wybrane_pole == "trapez":
    podstawa = input("podaj podstawę pierwsza")
    podstawa_gorna = input("podaj podstawe drugą")
    wysokosc = input("podaj wysokosc")
    pole_1 = int(podstawa) * int(podstawa_gorna)
    pole_2 = (int(wysokosc)* pole_1 /2)
    print ("oto pole trapeza" + str(pole_2))

