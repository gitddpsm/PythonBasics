"""

булевые bool
""" 
a = 5
print("divine_moment_of_" + str(a < 17 == 17))
user_age = 21

def ageComparsion(user_age):
    if user_age >= 18:
        print("Full acsess granted")
    elif user_age >= 16:
        print("Only history books")
    else:
        print("acsess denied! try later")

ageComparsion(14)