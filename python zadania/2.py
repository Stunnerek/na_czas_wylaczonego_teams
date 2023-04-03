from datetime import datetime

imie = input("Podaj swoje imię ")
rok_urodzenia_wprowadzony = input("Podaj swój rok urodzenia ")
currentYear = int(datetime.now().year) - int(rok_urodzenia_wprowadzony)

print("Masz na imię "+imie+" i masz " +str(currentYear) +" lat")