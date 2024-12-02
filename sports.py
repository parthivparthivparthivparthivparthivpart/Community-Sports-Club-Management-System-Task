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
    def add_performance_score(self):
        a = input(f"What score are you adding to {self.name}?")
        (self.peformance_scores).append(int(a))
    def calculate_average_score(self):
        return sum(self.peformance_scores) / len(self.peformance_scores)
    def get_member_summary(self):
        super().get_details()
        av = self.calculate_average_score()
        print(f"""
Member id: {self.membership_id}
Member's sport: {self.sport}
Member's score average: {av}""")

class Coach(Person):
    def __init__(self, name, age, contact_number, coach_id, specialisation, salary):
        super().__init__(name, age, contact_number)
        self.coach_id = coach_id
        self.specialisation = specialisation
        self.salary = salary
        self.mentees = []
    def assign_mentee(self, Member):
        print(f'Coach {self.name} is now mentoring {Member.name} in {Member.sport}')
        (self.mentees).append(Member.name)
    def set_coach_details(self):
        super().set_details()
        self.coach_id = input(f"What is {self.name}'s coach id?: ")
        self.specialisation = input(f"What is {self.name}'s specialisation: ")
        self.salary = input(f"What is {self.name}'s salary?: ")
    def get_mentees(self):
        print(self.mentees)
    def increase_salary(self, percentage):
        percentage = int(input("How much percent to increase their salary by?: "))
        self.salary = int(self.salary) * (1 + (percentage/100))
        print(self.salary)

class Staff(Person):
    def __init__(self, name, age, contact_number, staff_id, position, years_of_service):
        super().__init__(name, age, contact_number)
        self.staff_id = staff_id
        self.position = position
        self.years_of_service = years_of_service
    def set_staff_details(self):
        super().set_details()
        self.staff_id = input(f"What is {self.name}'s staff id?: ")
        self.position = input(f"What is {self.name}'s position?: ")
        self.years_of_service = int(input(f"How many years of service does {self.name} have?: "))
    def increment_service_years(self):
        self.years_of_service += 1
        print(f'1 year of service added!!!!!')
    def assist_member(self, Member):
        print(f"Staff {self.name} assisted {Member.name} in resolving an issue.")
    def get_staff_summary(self):
        super().get_details()
        print(f"""
Staff id: {self.staff_id}
Staff's position: {self.position}
Staff's years of service: {self.years_of_service}""")
        

a = Coach('', '', '', '', '', '')
a.set_coach_details()
a.increase_salary(10)
b = Member('', '', '', '', '', '')
b.set_details()
b.add_performance_score()
b.add_performance_score()
b.add_performance_score()
b.get_member_summary()
d = Member('', '', '', '', '', '')
d.set_details()
d.add_performance_score()
d.add_performance_score()
d.add_performance_score()
d.get_member_summary()
a.assign_mentee(b)
z = Coach('', '', '', '', '', '')
z.set_coach_details()
z.increase_salary(20)
z.assign_mentee(d)
z.get_mentees()
a.get_mentees()
c = Staff('', '', '', '', '', '')
c.set_staff_details()
c.increment_service_years()
c.get_staff_summary()
c.assist_member(d)

        

