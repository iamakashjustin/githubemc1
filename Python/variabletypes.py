class phone():
    chargertype="C-TYPE"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("Brand:",self.brand)
        print("price:",self.price)
        print("Chargertype:",self.chargertype)


phone.chargertype="B-TYPE"
samsung = phone("samsung","10000")
samsung.display()


redmi = phone("Redmi","1200")
redmi.display()


vivo = phone("vivo","13000")
vivo.display()
