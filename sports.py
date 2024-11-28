class Person:
    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.number = phone_number
    def set_details(self):
        self.name = input("What is their name?: \n")
        self.age = input("How old are they?: \n")
        self.number = input("What is their number?: \n")
    def get_details(self):
        print(f"""
name: {self.name}
age: {self.age}
phone number: {self.number}""")

class Member(Person):
    def __init__(self, name, age, phone_number, membersip_id, sport, peformance_scores):
        super().__init__(name, age, phone_number)
        self.membership_id = membersip_id
        self.sport = sport
        self.peformance_scores = []
    def set_details(self):
        super().set_details()
        self.membership_id = input(f"What is {self.name}'s id?: \n")
        self.sport = input(f"What sport is {self.name} doing? \n")
    def add_performance_score(self, score):
        a = input(f"What score are you adding to {self.name}?")
        (self.peformance_scores).append(int(a))
    def calculate_average_score(self):
        return sum(self.peformace_scores) / len(self.peformace_scores)
    def get_member_summary(self):
        super().get_details()
        av = self.calculate_average_score()
        print(f"""
Member id: {self.membership_id}
Member's sport: {self.sport}
Member's score average: {av}""")

class Coach(Person):