class college:
    def __init__ (self,x,name,rollno,age,random):
        self.name=name
        self.x=x
        self.rollno=rollno
        self.age=age
        self.random=random
    def __str__ (self):
        return f"{self.name} {self.x} {self.rollno} {self.age} {self.random}"
a=college("manish","Roll no",14,20,"gfhgjkghjgfj")
print(a)