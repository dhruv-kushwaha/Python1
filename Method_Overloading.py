def area(side1, side2 = None):
    if(side2 == None):
        # Calculating Area of Circle
        print("Area of Circle is : ", 3.14*side1*side1)
        return 
    
    elif(side1 == side2):
        #Cacluating Area of Square
        print("Area of Square is : ", side1*side1)
        return
        
    else:
        #Calculating Area of Rectangle
        print("Area of Rectangle is : ", side1*side2)
        return
    
def perimeter(side1, side2 = None):
    if(side2 == None):
        # Calculating Area of Circle
        print("Perimeter of Circle is : ", 2*3.14*side1)
        return 
    
    elif(side1 == side2):
        #Cacluating Area of Square
        print("Perimeter of Square is : ", 4*side1)
        return
        
    else:
        #Calculating Area of Rectangle
        print("Perimeter of Rectangle is : ", 2*(side1+side2))
        return
    
a = 7
area(a,a)
perimeter(a,a)