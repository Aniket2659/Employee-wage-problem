import random

def check_attendance(attendance):
    match attendance:
        case 0:
            return 0
        case 1:
            time = input('Enter a type of job (part/full) :')
            match time:
                case 'part':
                    return 20 * 6
                case 'full':
                    return 20 * 8
                case _:
                    return "Invalid job type"

atd_random = random.randint(0, 1)
print(check_attendance(atd_random))
