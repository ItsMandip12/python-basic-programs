class veichele:
    def __init__ (self,brand):
        self.brand=brand
    def show_info(self):
        print(f"Brand: {self.brand}")
class car(veichele):
    def __init__ (self,brand,model="299"):
        self.model=model
        super().__init__(brand)
    def show_info(self):
        super().show_info()
        print(f"Model: {self.model}")
obj1=car("Toyota")
obj1.show_info()