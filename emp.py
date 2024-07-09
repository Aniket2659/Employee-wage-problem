import random

def check_attendance(attendance):
    if attendance==0:
        print('employee is absent')
    if attendance==1:
        print('employee is present')
atd_check=random.randint(0,1)
check_attendance(atd_check)
