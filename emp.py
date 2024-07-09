import random

class Employee:
    PART_TIME_HOURS = 6
    FULL_TIME_HOURS = 8
    WAGE_PER_HOUR = 20
    MAX_HOURS = 200
    MAX_DAYS = 20

    def __init__(self):
        self.wage = 0
        self.total_hours = 0

    @classmethod
    def compute_monthly_wage(cls):
        employee = cls()
        for _ in range(cls.MAX_DAYS):
            if employee.total_hours >= cls.MAX_HOURS:
                break
            attendance = random.randint(0, 1)
            if attendance == 0:
                continue
            job_type = input('Enter a type of job (part/full): ').strip().lower()
            if job_type == 'part':
                employee.add_hours(cls.PART_TIME_HOURS)
            elif job_type == 'full':
                employee.add_hours(cls.FULL_TIME_HOURS)
            else:
                print("Invalid job type.")
        return employee.wage

    def add_hours(self, hours):
        if self.total_hours + hours <= Employee.MAX_HOURS:
            self.wage += hours * Employee.WAGE_PER_HOUR
            self.total_hours += hours
        else:
            print("Exceeded maximum working hours.")


print(f"Total monthly wage: {Employee.compute_monthly_wage()}")
