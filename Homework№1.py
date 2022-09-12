class Employee:
    def __init__(self, name: str, salary_per_day: int):
        self.name = name
        self.salary_per_day = salary_per_day

    def work(self):
        return "I come to the office"

    def check_salary(self, days: int):
        return self.salary_per_day * days


class Recruiter(Employee):

    def __init__(self, name: str, salary_per_day: int):
        super().__init__(name, salary_per_day)

    def work(self):
        return "I come to the office and start hiring"

    def __str__(self):
        return f'{__class__.__name__}:{self.name}'


class Developer(Employee):

    def __init__(self, name: str, salary_per_day: int, tech_stack: list = ()):
        super().__init__(name, salary_per_day)
        self.tech_stack = tech_stack

    def work(self):
        return "I come to the office and start coding"

    def __str__(self):
        return f'{__class__.__name__}:{self.name}'

    def addition(self, another_one):
        return Developer(name=f'{self.name} {object.name}',
                         salary_per_day=max(self.salary_per_day, another_one),
                         tech_stack=list(set(self.tech_stack + another_one.tech_stack)))


if __name__ == '__main__':
    print(Employee.work(Employee))

    print(Recruiter.work(Recruiter))
    recrut = Recruiter('Mark', 15000)
    print(recrut)
    print(recrut.check_salary(10))

    print(Developer.work(Developer))
    develop1 = Developer('John', 30000, ['python', 'java', 'ruby'])
    develop2 = Developer('Joe', 20000, ['python', 'java', 'php'])
    print(develop1)
    print(develop1.check_salary(5))

    print(f'Salary of the employee {recrut.name} is higher than the salary of employee {develop1.name}'
          if recrut.salary_per_day > develop1.salary_per_day and recrut != develop1
          else f'Salary of the employee {recrut.name} is lower than the salary of employee {develop1.name}')

