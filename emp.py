import random

class Employee:
    PART_TIME_HOURS = 6
    FULL_TIME_HOURS = 8

    def __init__(self, wage_per_hour, max_hours, max_days):
        self.wage_per_hour = wage_per_hour
        self.max_hours = max_hours
        self.max_days = max_days
        self.wage = 0
        self.total_hours = 0

    @classmethod
    def compute_monthly_wage(cls, company_name, wage_per_hour, max_days, max_hours):
        employee = cls(wage_per_hour, max_hours, max_days)
        for _ in range(max_days):
            if employee.total_hours >= max_hours:
                break
            attendance = random.randint(0, 1)
            if attendance == 0:
                continue
            job_type = input(f'Enter a type of job for {company_name} (part/full): ').strip().lower()
            if job_type == 'part':
                employee.add_hours(cls.PART_TIME_HOURS)
            elif job_type == 'full':
                employee.add_hours(cls.FULL_TIME_HOURS)
            else:
                print("Invalid job type.")
        print(f"Total monthly wage for {company_name}: {employee.wage}")
        return employee.wage

    def add_hours(self, hours):
        if self.total_hours + hours <= self.max_hours:
            self.wage += hours * self.wage_per_hour
            self.total_hours += hours
        else:
            print("Exceeded maximum working hours.")

# Example usage for multiple companies
Employee.compute_monthly_wage("CompanyA", 20, 20, 160)
Employee.compute_monthly_wage("CompanyB", 15, 25, 200)
Employee.compute_monthly_wage("CompanyC", 22, 18, 150)
