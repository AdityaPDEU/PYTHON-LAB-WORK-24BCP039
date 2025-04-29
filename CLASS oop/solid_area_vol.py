import math
class solid:
    def __inint__(self):
        self.shape=None
    def get_data(self):
        print("choose your solid form")
        print("1. cube")
        print("2. cuboid")
        print("3. cylinder")
        print("4. sphere")
        choice=int(input("enter choice for 1-4:"))
        self.shape=choice

        if choice==1:
            self.side=float(input("enter the side of cube:"))
        elif choice==2:
            self.lenght=float(input("enter the length  cuboid:"))
            self.bredth=float(input("enter the bredth cuboid:"))
            self.height=float(input("enter the height of cuboid:"))
        elif choice==3:
            self.radius=float(input(" enter thr radius of cylinder:"))
        elif choice==4:
            self.radius=float(input("enter  radius of the sphere:"))
            self.height=float(input("enter   height of the sphere:"))
        else:
            print("invaid choice000")
    
    def calculate_data(self):
        if self.shape==1:
            area=6*(self.side**2)
            volume= self.side**3
            print (f"surface area of cube:{area}")
            print(f"volume of cube:{ volume}")
        elif self.shape==2:
            area=2*(self.lenght*self.bredth + self.bredth*self.height + self.height*self.lenght)
            volume= self.lenght*self.bredth*self.height
            print (f"surface area of cuboid:{area}")
            print(f"volume of cuboid:{ volume}")
        elif self.shape==3:
            area = 4 * math.pi * (self.radius ** 2)
            volume = (4/3) * math.pi * (self.radius ** 3)
            print(f"Surface Area of Sphere: {area:.2f}")
            print(f"Volume of Sphere: {volume:.2f}")

        elif self.shape == 4:
            area = 2 * math.pi * self.radius * (self.radius + self.height)
            volume = math.pi * (self.radius ** 2) * self.height
            print(f"Surface Area of Cylinder: {area:.2f}")
            print(f"Volume of Cylinder: {volume:.2f}")

        else:
            print("No valid shape selected to calculate.")

s=solid()
s.get_data()
s.calculate_data()