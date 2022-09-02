import math

############################### Point Class #############################
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    def distanceTo(self, other):
        distance = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        # return "The distance between the two points is: " + str(distance)
        return distance


print("---------------------------Class Point---------------------------")
a = Point(3, 2)
b = Point(-1, 5)
print("I have two point objects: " + str(a) + " and " + str(b))
# I have two point objects: (3, 2) and (-1, 5)
howFar = a.distanceTo(b)
print("Distance from ", a, " to ", b, " is: ", howFar)

############################### Line Class #############################
class Line(Point):
    def __init__(self, p1, p2):
        # super().__init__(p1, p2)
        #NOTE: keep running into errors here... don't know what to do
        self.p1 = p1
        self.p2 = p2
    def __str__(self):
        return "(" + str(self.p1) + ", " + str(self.p2) + ")"
    def length(self):
        # dx = abs(self.p2.x - self.p1.x)
        # dy = abs(self.p2.y - self.p1.y)
        a = self.p2.distanceTo(self.p1)
        # lineLength = math.sqrt(dx**2 + dy**2)
        #return "The length of the line is: " + a
        return a

print("---------------------------Class Line---------------------------")
a = Point(3, 2)
b = Point(-1, 7) 
c = Line(a,b)
distance = c.length()
print("Length of Line ", c, " is: ", distance)

############################### Triangle Class #############################

class Triangle(Line):
    def __init__(self, p1, p2, p3):
        self.l1 = Line(p1,p2)
        self.l2 = Line(p2,p3)
        self.l3 = Line(p3,p1)
    def __str__(self):
        return "Triangle {" + str(self.l1.p1) + ", " + str(self.l2.p1) + ", " + str(self.l3.p1) + "}"
    def area(self):
        x = (self.l1.length() + self.l2.length() + self.l3.length())/2
        a = math.sqrt(x*(x - self.l1.length())*(x - self.l2.length())*(x - self.l3.length()))
        return a
    
print("---------------------------Class Triangle---------------------------")
a = Point(4,5)
b = Point(2,2)
c = Point(5,1)
tri = Triangle(a,b,c)
A = tri.area()
print("Area of ", tri, " is: ", A)

############################### LinkedList Class #############################

class LinkedList:
    def __init__(self, num, next):
        self.num = num
        self.next = next
        # self.head = None
    def show(self):
        temp = self
        result = ""
        while (temp):
            # print(temp.num)
            result = result + "|" + temp.num + "|"
            temp = temp.next
        print(result)

# NOTE: how to test this?
print("---------------------------Class LinkedList---------------------------")
a = LinkedList("Christa", None)
a = LinkedList("Ahmed", a) 
a.show()

############################### BinaryTree Class #############################

class BinaryTree:
    def __init__(self, value, left, right):
        (self.value, self.left, self.right) = (value, left, right)
    def show(self):
        if self.left == None:
            left = " . "
        else: 
            left = self.left.show()    

        if self.right == None:
            right = " . "
        else: 
            right = self.right.show() 

        return "(" + left + " " + str(self.value) + " " + right + ")"


print("---------------------------Class BinaryTree---------------------------")
a = BinaryTree(5, None, None)
print(a.show())

a = BinaryTree(1, a, None)
print(a.show())

a = BinaryTree(2, BinaryTree(4, None, a), None)
print(a.show())



