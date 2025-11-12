# Objective:
# Students will learn how to compare values using Python’s comparison operators and interpret Boolean results.

# Topics Covered:
# ==, !=, >, <, >=, <=

# Key Notes:

# Comparison operators compare two values and return either True or False.

# Remember: = is assignment, while == is comparison.

a = 3
b = 4
print(a) #output of 3
print(b) #output of 4
print(a == b) #output of false

print(a == b)   # False (checks for equality)
print(a != b)   # True (check if is not equal)
print(a > b)    # False (checks for greater than)
print(a < b)    # True (checks for less than)
print(a >= b)   # False (checks for greater than or equal to)
print(a <= b)   # True (checks for less than or equal to)


#predict the output of the following comparisons:
10 > 5 #output true
7 == 2 * 3 + 1 # output true
8 != 8 #output false
4 <= 2 + 2 #output true

# Write 3 examples that result in True and 3 that result in False.
10 > 5 #output true
7 == 2 * 3 + 1 # output true
4 <= 2 + 2 #output true
10 > 15 #output false
7 == 2 * 4 + 5 #output false
67 >= 41 #output false
# Create a simple grade-checking condition:

#else you failed
# practice problem :
# where a student must check if their score is greater than or equal to 60 to pass a test.# The password must be at least 8 characters long and contain at least one digit.password = "mypassword1"
score = int(input("what is your score"))
if score >= 90 and score <= 100:
    print("you got an a")
#if score is between 80 - 89 -- you got an b
elif score >= 80 and score <= 89:
    print("you got a b")
#if score is between 70 - 79 -- you got an c
elif score >= 70 and score <= 79:
    print("you got a c")
#if score is between 60 - 69 -- you got an d
elif score >= 60 and score <= 69:
    print("you got a d")
else:
    print("you failed")