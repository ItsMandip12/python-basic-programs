#class which has two methods for area and perimeter

class rect:
    def __init__ (self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return (self.l*self.b)
    def per(self):
        return (2*(self.l+self.b))
    
obj1=rect(5,10)
print(f"Area is : {obj1.area()}")
print(f"Perimeter is : {obj1.per()}")