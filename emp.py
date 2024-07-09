import random
def check_attendance(attendance):
    if attendance==0:
        return 0
    if attendance==1:
        time=input('enter a type of job :')
        if time=='part':
            return 20*6
        elif time=='full':
            return 20*8

atd_random=random.randint(0,1)
print(check_attendance(atd_random))