"""PROG 10004: Assignment 3.
Name:Jinfeng he(komi)."""

from shelf import Shelf
from vendingMachine import VendingMachine
from breakroom import BreakRoom

#Create shelves for vending mahine 1
s1 = Shelf("cookies", 1.50, 5)
s2 = Shelf("chips", 1.00, 3)


#Create shelves for vending mahine 2
s3 = Shelf("candy", 1.00, 5)
s4 = Shelf("gum", 0.50, 2)
s5 = Shelf("soda", 2.00, 4)

#Create vending machines
machine1 = VendingMachine(s1, s2)
machine2 = VendingMachine(s3, s4, s5)

#Create breakroom
breakroom = BreakRoom(machine1, machine2)

#start simulation
breakroom.simulate()









