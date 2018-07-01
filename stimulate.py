import random


answer = input("Ready to roll Dice? Yes or No ")
while (answer == "Yes" or answer == "yes"):
    print(random.randint(1,6))
    answer = input("Ready to roll Dice? Yes or No")


