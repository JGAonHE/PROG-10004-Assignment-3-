"""PROG 10004: Assignment 3.
Name:Jinfeng he(komi)."""

from shelf import Shelf
from vendingMachine import VendingMachine

class BreakRoom:
    """create a class for breakroom"""
    
    def __init__(self, machine1, machine2):
        self.machine1 = machine1
        self.machine2 = machine2
    
    def simulate(self):
        choice = 0
        print("Welcome to the Break Room!")

        while choice != 4:
            print()
            print("There are two vending machines here:")
            print("1.", self.machine1)
            print("2.", self.machine2)
            print()
            print("What would you like to do?")
            print("1. Enter money")
            print("2. Get change back")
            print("3. Vend an item")
            print("4. Leave the break room")
            print()

            choice = int(input("Your Choice? "))
            if choice == 1:
                machine_choice = int(input("Which machine would you like to use? (1 or 2): "))

                print("Choose a coin type:")
                print("1. Nickel")
                print("2. Dime")
                print("3. Quarter")
                print("4. Loonie")
                print("5. Toonie")

                coinChoice = int(input("Please enter your choice: "))

                amount = 0.0

                if coinChoice == 1:
                    amount = 0.05
                elif coinChoice == 2:
                    amount = 0.10
                elif coinChoice == 3:
                    amount = 0.25
                elif coinChoice == 4:
                    amount = 1.00
                elif coinChoice == 5:
                    amount = 2.00

                if amount == 0.0:
                    print("Invalid coin choice.")
                else:
                    numCoins = int(input("How many coins would you like to enter? "))
                    amount = amount * numCoins
                    if machine_choice == 1:
                        self.machine1.insertCoin(amount)
                        print("Money entered")
                    elif machine_choice == 2:
                        self.machine2.insertCoin(amount)
                        print("Money entered")
                    else:
                        print("Invalid machine choice.")
                
            elif choice == 2:
                machineChoice = int(input("Which machine would you like to use? (1 or 2): "))

                if machineChoice == 1:
                    print("Which items?")
                    for i in range(len(self.machine1.shelves)):
                        print(i + 1,".",self.machine1.shelves[i].name)
                    
                    itemChoice = int(input("Please enter your choice: "))
                    numItems = int(input("How many items would you like to vend? "))
                    
                    for i in range(numItems):
                        result = self.machine1.vend(itemChoice-1)

                        if result == "":\
                            print("*** Vend Failled ***")
                        else:
                            print(result)
                elif machineChoice == 2:
                    print("Which items?")
                    for i in range(len(self.machine2.shelves)):
                        print(i + 1,".",self.machine2.shelves[i].name)
                    
                    itemChoice = int(input("Please enter your choice: "))
                    numItems = int(input("How many items would you like to vend? "))
                    
                    for i in range(numItems):
                        result = self.machine2.vend(itemChoice-1)

                        if result == "":
                            print("*** Vend Failled ***")
                        else:
                            print(result)
                
                
            elif choice == 3:
                machineChoice = int(input("Which machine would you like to use? (1 or 2): "))

                if machineChoice == 1:
                    change = self.machine1.returnChange()
                    print("Change returned: $" + ("%0.2f" % change))
                elif machineChoice == 2:
                    change = self.machine2.returnChange()
                    print("Change returned: $" + ("%0.2f" % change))
                else:
                    print("Invalid machine choice.")
                
            elif choice == 4:
                print("Thanks for coming, Goodbye!")
                
            else:
                print("Invalid choice.")
