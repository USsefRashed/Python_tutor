class Pizza:
    def __init__(self,ingredients,radius):
        self.components=ingredients
        self.radius=radius
    def area(self):
        return Pizza.circleArea(self.radius)
    def __str__(self):
        return f"pizza ingraedients is {self.components} And its size is {self.area()} squared cm"
    @staticmethod
    def circleArea(r):
        return (r**2)*3.14
pz1=Pizza(["Tomatoes","onion"],15)
print(pz1)
#I can use static method dirctly without creating objects
print("Circle area",Pizza.circleArea(4))
    
    