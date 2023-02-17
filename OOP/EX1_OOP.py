#Student Example in OOP to get student name and marks and get average 
class student: 
    def __init__(self, name ):
        self.name= name
        self.marks=[]
        print (f'welcome {name} to this school')


    def add_marks(self, mark):
        self.marks.append(mark)

    def avg(self):
        return (sum(self.marks))/(len(self.marks))
    
s=student("moahmmed")
s.add_marks(10)
s.add_marks(20)
s.add_marks(30)
s.add_marks(40)
s.add_marks(50)
print (f'the List you make it {s.marks}')
print (f"The average of this numbers is equal: {int(s.avg())}")

