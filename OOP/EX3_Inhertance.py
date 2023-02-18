class Date():
    def __init__(self):
        self.date = "17-03-2023 "
        print(f"Date of today is: {self.date}")

class Time(Date):
    def get_Time(self):
        self.time = "5:30:00 "
        print(f"Time  is: {self.time}")


c1= Date()
c1.date
c2=Time()
c2.get_Time()
