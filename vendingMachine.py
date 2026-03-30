"""PROG 10004: Assignment 3.
Name:Jinfeng he(komi)."""

from shelf import shelf

class vendingMachine:
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
            return self.shelves[shelfNum].dispense()
    
    def __returnChange(self):
        change = self.credit
        self.credit = 0.0
        return change
    
    def __str__(self):
        report = "VendingMachine."

        for shelf in self.shelves:
            report = report +str(shelf.quantity) + " " + shelf.name + " for $" + format(shelf.price, ".2f") + " . "
        
        report = report + "$" + format(self.credit,".2f")+ " credit."

        return report
    



        
        



