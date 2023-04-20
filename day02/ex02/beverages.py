class HotBeverages:
    name = 'hot beverage'
    price = 0.3


    def description(self):
        return ("Just some hot water in a cup.")


    def  __str__(self):
        string = "name : " + self.name + "\n"
        string += "price : " + str(self.price) + "\n"
        string += "description : " + self.description()
        return(string)

class Coffee(HotBeverages):
    name = 'coffee'
    price = 0.40


    def description(self):
        return ("A coffee, to stay awake.")

class Tea(HotBeverages):
    name = 'tea'
    price = 0.30


    def description(self):
        return ("Just some hot water in a cup.")

class Chocolate(HotBeverages):
    name = 'chocolate'
    price = 0.50


    def description(self):
        return ("Chocolate, sweet chocolate...")

class Cappuccino(HotBeverages):
    name = 'capuccino'
    price = 0.45


    def description(self):
        return ("Un po’ di Italia nella sua tazza!")



    
if __name__ == '__main__':
    HotBeverage = HotBeverages()
    Coffee = Coffee()
    Tea = Tea()
    Chocolate = Chocolate()
    Cappuccino = Cappuccino()
    print(HotBeverage)
    print(Coffee)
    print(Tea)
    print(Chocolate)
    print(Cappuccino)
    