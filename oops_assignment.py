# defining the parent class A
# let Class A correspond to college

class A :  
# init of class  A
    def __init__(self, college):
        print("init of A")
        self.college = college
        
    # methods of class A
    def methodA1(self):   
        print("inside method A1")
        print("College Name :", self.college)
    
        
# defining class B which is a child-class of class A
# Let class B correspond to the year the student studies in        

class B(A):
    # init of class B
    def __init__(self, year):
        print("init of Class B is called")
        self.year = year
        
    # methods of class B
    def methodB1(self):
        print("inside method B1")
        print("College Name :", self.college)
        print("        Year :", self.year)
            
        
# defining class C which itself a child-class of Class B
# Let class A correspond to the branch of the student

class C(B):
    # init of class C
    def __init__(self, branch):
        self.branch = branch 
    
    # methods of class C 
    # with an example of calling parent function as well
    def methodC1(self):
        print("inside method C1")
        self.methodB1()         
        print("College Name :", self.college)
        print("        Year :", self.year)
        print("      Branch :", self.branch)
        

# defining Class D which itself is a child-class of Class B
# Let Class D correspond to the society the student has joined 

class D(B):
    # init of class  D
    def __init__(self, society):
        self.society = society
        
    # methods of class D
    def methodD1(self):
        print("inside methode D1")
        print("College Name :", self.college)
        print("        Year :", self.year)
        print("     Society :", self.society)
        
        
# defining class E which is a child of class C & D and grand-child of class B
# and grand-grand-child of class A
# let class E correspond to the Personal Details of the Student

class E(C,D):
    
    # init of class E
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill
        
    # methods of Class E
    def methodE1(self):
        print("College Name :", self.college)
        print("        Year :", self.year)
        print("      Branch :", self.branch)
        print("     Society :", self.society)
        print("        Name :", self.name)
        print("      Skills :", self.skill)
        
        
# Creating Objects and testing everything out

student = E("Dhruv", "C++ and Python")
student.college = "AKGEC"
student.year = "2nd"
student.branch = "CSE(AIML)"
student.society = "BRL"
student.methodE1()
student.methodC1()