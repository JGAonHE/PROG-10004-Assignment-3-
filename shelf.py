"""PROG 10004: Assignment 3.
Name:Jinfeng he(komi)."""

class shelf:
    """Create a class for shelf to store one product type in a vending machine shelf."""
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def dispense(self):
        """Dispense an item if any products are available (quantity > 0)."""
        if self.quantity > 0:
            self.quantity = self.quantity - 1
            return self.name
        else:
            return ""

if __name__ == "__main__":
    #This is a test code ,I use if __name__ == "__main__": "ensures that certain code blocks only run when a script is executed directly, not when imported as a module".
    s1 = shelf("cookies", 1.50, 2)
    print(s1.dispense())

    s2 = shelf("chips", 1.00, 3)
    print(s2.dispense())

    

    




