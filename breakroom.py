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

        while choice != 4:
            print("Welcome to the breakroom!")
            print("There are two vending machines to choose from.")
            print("1.", self.machine1)
            print("2.", self.machine2)
            print("Your options are:")
            print("1, Enter money")
            print("2, Vend an item")
            print("3, Get your change back")
            print("4, Exit the breakroom")

            choice=int(input("Please enter your choice: "))

            if choice == 1:
                machine_choice = int(input("Which machine would you like to use? (1 or 2): "))

                print("Choose a coin type:")
                print("1. Nickel")
                print("2. Dime")
                print("3. Quarter")
                print("4. Loonie")
                print("5. Toonie")

                coinChoice= int(input("Please enter your choice: "))

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

                if machine_choice == 1:
                    self.machine1.insertCoin(amount)
                    print("Money entered")
                elif machine_choice == 2:
                    self.machine2.insertCoin(amount)
                    print("Money entered")
                else:
                    print("Invalid machine choice.")
                
            elif choice == 2:
                machineChoice =int(input("Which machine would you like to use? (1 or 2): "))

                if machineChoice == 1:
                    print("Which item?")
                    for i in range(len(self.machine1.shelves)):
                        print(i + 1, ".", self.machine1.shelves[i].name)
                    
                    itemChoice = int(input("Your choice: "))
                    result = self.machine1.vend(itemChoice - 1)
                    print(result)

                    if result == "":
                        print("*** Vend Failed ***")
                    else:
                        print(result)
                    
                elif machineChoice == 2:
                    print("Which item?")
                    for i in range(len(self.machine2.shelves)):
                        print(i + 1, ".", self.machine2.shelves[i].name)
                    itemChoice = int(input("Your choice: "))
                    result = self.machine2.vend(itemChoice - 1)
                    print(result)

                    if result == "":
                        print("*** Vend Failed ***")
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
