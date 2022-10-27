import numpy as np

class Complex :
    def __init__(self, real, img):
        self.__real = real;
        self.__img = img;
        self.__mag = ((self.__real)**2 + (self.__img)**2)**(0.5)
        self.__angle = (np.arctan(self.__img/self.__real))*360/(2*3.14)
    
    def __str__(self):
        return "{}+{}j".format(self.__real, self.__img)
    
    def get_real(self):
        return self.__real;
    
    def set_real(self, real):
        if(type(real) == int or type(real)==float):
            self.__real = real
        else:
            print("Wrong Input")
            
    def get_img(self):
        return self.__img;
    
    def set_img(self, img):
        if(type(img) == int or type(img)==float):
            self.__img = img
        else:
            print("Wrong Input")
            
    def __add__(self, other):
        temp_real = self.__real + other.__real
        temp_img = self.__img + other.__img
        if temp_img <0 :
            return "{}{}j".format(temp_real, temp_img)    
        else:
            return "{}+{}j".format(temp_real, temp_img)
        
        
    def __sub__(self, other):
        temp_real = self.__real + other.__real
        temp_img = self.__img + other.__img
        if temp_img <0 :
            return "{}{}j".format(temp_real, temp_img)    
        else:
            return "{}+{}j".format(temp_real, temp_img)
        
        
    def __mul__(self, other):
        temp_real = (self.__real * other.__real) - (self.__img * other.__img)
        temp_img = (self.__real * other.__img) + (self.__img * other.__real)
        temp_real = round(temp_real, 3)
        temp_img = round(temp_img, 3)
        if temp_img <0 :
            return "{}{}j".format(temp_real, temp_img)    
        else:
            return "{}+{}j".format(temp_real, temp_img)
                
    
    def __truediv__(self, other):
        a = self.__real
        b = self.__img
        c = other.__real
        d = other.__img
        temp_real = ((a*c)+(b*d))/(c*c + d*d)
        temp_img = ((b*c) -(a*d))/(c*c + d*d)
        temp_real = round(temp_real, 3)
        temp_img = round(temp_img, 3)
        if (temp_img <0) :
            return "{}{}j".format(temp_real, temp_img)    
        else:
            return "{}+{}j".format(temp_real, temp_img)
        
    def mag(self):
        temp_ans = ((self.__real)**2 + (self.__img)**2)**(0.5)  
        return round(temp_ans, 3)
    
    def phase(self):
        return self.__angle
    
    def dist(self, other):
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
            
    
n = Complex(5,6)
print(n)
# print(n.get_real())
# n.real = 4
# print(n.get_real())
# n.set_real(4.0)
# print(n.get_real())
# n.set_img(45.67)
# print(n.get_img())
n1 = Complex(-5,-6)
print(n*n1)
n2 = ((n/n1))
print(type(n2))
print(n.dist(n1))
print(n1.mag())
print(n1.topolar())
print(n1.conjugate())
print(n1.phase())
