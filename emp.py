import random
def monthly_wage():
    wage=0
    total_spent=0
    for i in range(20):
        if total_spent<=200:
            attendance=random.randint(0,1)
            if attendance==0:
                continue
            if attendance==1:
                time=input('enter a type of job :').strip().lower()
                if time=='part':
                    wage=wage+(20*6)
                    total_spent=total_spent+6
                elif time=='full':
                    wage=wage+(20*8)
                    total_spent=total_spent+8
                else:
                    print("Invalid job type.")
    return wage

print(f"Total monthly wage: {monthly_wage()}")
