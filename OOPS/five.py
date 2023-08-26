class Rectangle():
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth


    def Area(self):
        return self.length * self.breadth
    
    def show(self):
        print(f"Lenght of Rectangle is {self.length}")
        print(f"Breadth of Rectangle is {self.breadth}")

    def show_area(self):
        print(f"Area of Rectangle is {self.Area()}")


r = Rectangle(10,20)
r.show()
r.show_area()
