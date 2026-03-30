"""PROG 10004: Assignment 3.
Name:Jinfeng he(komi)."""

from shelf import Shelf

class VendingMachine:
    """Create a class for vendingMachine"""

    def __init__(self, shelves): 
        self.shelves = shelves
        self.credit = 0.0
    
    def insertCoin(self, amount):
        self.credit = self.credit + amount
    
    def vend(self, shelfNum):
        if self.shelves[shelfNum].quantity <= 0:
            return""
        
        elif self.credit < self.shelves[shelfNum].price:
            return""
        else:
            self.credit = self.credit - self.shelves[shelfNum].price
            item = self.shelves[shelfNum].dispense()
            return item
    
    def returnChange(self):
        change = self.credit
        self.credit = 0.0
        return change
    
    def __str__(self):
        report = "VendingMachine- "

        for shelf in self.shelves:
            report = report + "" + shelf.name + ": " + str(shelf.quantity) + " for $" + format(shelf.price,".2f") + " "
        
        report = report + "$" + format(self.credit,".2f")+ " credit."

        return report
    
if __name__ == "__main__":
    #This is a test code ,I use if __name__ == "__main__": "ensures that certain code blocks only run when a script is executed directly, not when imported as a module".
    s1 = Shelf("cookies", 1.50, 2)
    s2 = Shelf("chips", 1.00, 3)

    vm = VendingMachine([s1, s2])

    print(vm)
    vm.insertCoin(2.00)
    print(vm)
    print(vm.vend(1))
    print(vm)
    print(vm.returnChange())
    print(vm)


        
        



