class Rectangle:
    """This class is a rectangle"""
    #attributes
    def __init__(self):
        self.length=0.0
        self.breadth=0.0
    #functions
    def getlength(self):
        return self.length
    def getbreadth(self):
        return self.breadth
    def setlength(self,newlength):
        self.length=newlength
    def setbreadth(self,newbreadth):
        self.breadth=newbreadth
    def areaRectangle(self):
        area=self.length*self.breadth
        return area

RedRectangle=Rectangle()
RedRectangle.setlength(20)
RedRectangle.setbreadth(25.2)
print("the area of the rectangle is", RedRectangle.areaRectangle())

BlueRectangle=Rectangle()
BlueRectangle.setlength(22)
BlueRectangle.setbreadth(21.2)
print("the area of the rectangle is", BlueRectangle.areaRectangle())
print(BlueRectangle.getlength())
print(BlueRectangle.getbreadth())

print(RedRectangle.getlength())
print(RedRectangle.getbreadth())



