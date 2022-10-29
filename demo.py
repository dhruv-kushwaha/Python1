import numpy as np

class Complex :
    
    # Declaring the Constructor of the class
    def __init__(self, real, img):
        if((type(real)== int) or type(real) == float):
            self.__real = real;
        else:
            print("Wrong Input!!")
            return
        
        if((type(img)== int) or type(img) == float):
            self.__img = img;
        else:
            print("Wrong Input")
            return
        
        self.__mag = ((self.__real)**2 + (self.__img)**2)**(0.5)
        self.__angle = (np.arctan(self.__img/self.__real))*360/(2*3.14)
    
    
    
    # Declaring the Format of the the Object
    def __str__(self):
        if self.__img <0 :
            return "{}{}j".format(self.__real, self.__img)    
        else:
            return "{}+{}j".format(self.__real, self.__img)
        
        
        
    # Getters : 
    def get_real(self):
        return self.__real;
    
    def get_img(self):
        return self.__img;
    
    
    
    # Setters : 
    def set_real(self, real):
        if(type(real) == int or type(real)==float):
            self.__real = real
        else:
            print("Wrong Input")
            
    def set_img(self, img):
        if(type(img) == int or type(img)==float):
            self.__img = img
        else:
            print("Wrong Input")
    
    
    
    # Operator Overloading :        
    def __add__(self, other):
        temp_real = self.__real + other.__real
        temp_img = self.__img + other.__img
        
        new = Complex(temp_real, temp_img)
        return new
    
    def __sub__(self, other):
        temp_real = self.__real + other.__real
        temp_img = self.__img + other.__img
        new = Complex(temp_real, temp_img)
        return new
    
    def __mul__(self, other):
        temp_real = (self.__real * other.__real) - (self.__img * other.__img)
        temp_img = (self.__real * other.__img) + (self.__img * other.__real)
        temp_real = round(temp_real, 3)
        temp_img = round(temp_img, 3)
        new = Complex(temp_real, temp_img)
        return new
                   
    def __truediv__(self, other):
        a = self.__real
        b = self.__img
        c = other.__real
        d = other.__img
        temp_real = ((a*c)+(b*d))/(c*c + d*d)
        temp_img = ((b*c) -(a*d))/(c*c + d*d)
        temp_real = round(temp_real, 3)
        temp_img = round(temp_img, 3)
        new = Complex(temp_real, temp_img)
        return new
    
    
    
    # Some Methods important for class Complex
    def mag(self):
        temp_ans = ((self.__real)**2 + (self.__img)**2)**(0.5)  
        return round(temp_ans, 3)
    
    def phase(self):
        return self.__angle
    
    def distance(self, other):
        temp_ans = ((self.__real - other.__real)**2 + (self.__img - other.__img)**2)**(0.5)
        return round(temp_ans, 3)
    
    def topolar(self):
        angle = (np.arctan(self.__img/self.__real))*360/(2*3.14)
        mag = self.mag()
        return "mag= {}, angle= {}°".format(mag, angle)
    
    def conjugate(self):
        if (self.__img)<0:
            return "{}+{}j".format(self.__real, (-1)*self.__img)
        else:
            return "{}{}j".format(self.__real, (-1)*self.__img)
        
        
    
        
        
c1 = Complex(4,5)
print(c1)
c2 = Complex(3,-6)
print(c2)
i = c2.get_img()
print(i)
print(c1+c2)
c3 = c1+c2
r = (c3.get_real())
print(r)
print(c1*c2)
print(c1/c2)
print(c1.conjugate())
print(c1.topolar())
print(c1.distance(c2))
print(type(c3))