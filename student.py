class student:
    def __init__(self,name,enrol,marks):
        self.name=name
        self.enrol_ment=enrol
        self.marks_no=marks
    
    def print_data(self):
        return {
            'name of student':self.name,
            'enrolment no':self.enrol_ment,
            'marks obtain':self.marks_no
        }
s1=input("student name")
e1=input("enter enrolment number")
m1=int(input("enter marks"))
s=student(s1,e1,m1)
print(s.print_data())

