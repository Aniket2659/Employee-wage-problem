import random
def check_attendance(attendance):
    if attendance==0:
        return 0
    if attendance==1:
        return 20*8
atd_random=random.randint(0,1)
print(check_attendance(atd_random))