class complex:
    # def __init__(self,real=0,image=0):
    def __init__(self,real,image):
        self.real=real
        self.image=image
    def add(self, other):
        self.x=self.real + other.real
        self.y=self.image + other.image
        return complex(self.x, self.y)
    #     new=complex()
    #     new.real=self.real+ob.real
    #     new.image=self.image+ob.image
    #     return new
    def __sub__(self,other):
        self.real=self.real-other.real
        self.image=self.image-other.image
        return complex(self.real, self.image)
    def print_data(self):
        print(f'{self.real} + {self.image}j')
    def new_print_data(self):
        print(f"{self.real} - {self.image}j")
s1=complex(5,10)
s1.print_data()
s2=complex(2,4)
s2.print_data()
s=s1.add(s2)
s.print_data()
s4=s1 - (s2)
s4.new_print_data()
