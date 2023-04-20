from beverages import *
import random

class CoffeeMachine:
    def __init__(self):
        self.remain_cups = 10
        pass

    class EmptyCup(HotBeverages):
        name = "empty cup"
        price = 0.90
        
        def description(self):
            return ("An empty cup?! Gimme my money back!")
        
    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def repair(self):
        self.remain_cups = 10

    def serve(self, drink):
        if (self.remain_cups == 0):
            raise self.BrokenMachineException
        self.remain_cups -= 1
        if (random.randrange(1,7) == 6):
            print(self.EmptyCup())
        print(drink())

if __name__ == '__main__':
    machine = CoffeeMachine()
    drink_list = [HotBeverages, Coffee, Tea, Chocolate, Cappuccino]
    for i in range(11):
        try:
            machine.serve(random.choice(drink_list))
        except machine.BrokenMachineException as error:
            print(error)
    machine.repair()
    for i in range(11):
        try:
            machine.serve(random.choice(drink_list))
        except machine.BrokenMachineException as error:
            print(error)


