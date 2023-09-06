from random import randint

number = randint(1,100)
user_number = 0
print("Wylosowałem liczbe od 1 do 100, zgadnij jaką!")

while True:
    try:
        user_number = int(input("Liczba: "))
    except:
        print("Podaj cyfre lub liczbe całkowitą")
        continue
    if user_number > number:
        print("Podałeś za dużą liczbę")
    elif user_number < number:
        print("Podałeś za małą liczbę")
    else:
        print("Brawo! Zgadłeś, to liczba: " + str(number))
        break




