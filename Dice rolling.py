from random import randint


def dice_roll():
    dice = randint(1,6)
    return dice


numOfRolls = int(input("Podaj ilośc losowań: "))
i = 1
while i <= numOfRolls:
    print("Losowanie " + str(i) + ": " + str(dice_roll()))
    i += 1