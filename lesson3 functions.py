def subNumbers(x, y):
    return (x - y)

# main code
a = 90
b = 50

# finding subtraction
result = subNumbers(a, b)

# print statement
print("subtraction of ", a, " and ", b, " is = ", result)

def multNumbers(x, y):
    return (x * y)

a = 12
b = 4

result = multNumbers(a, b)

print("multiplication of ", a, " and ", b, " is =", result)


# outer for loop
#for element in sequence
#  # inner for loop
#  for element in sequence
#     body of inner for loop
#  body of outer for loop

# example: generate a mult table

# outer loop
for i in range(1, 11):
    # nested loop
    # to iterate from 1 to 10
    for j in range(1, 11):
        # print multiplication
        print(i * j, end=' ')
    print()

steelers = input("enter a phrase: ")
def translate(steelers):
    translation=""
    for letter in steelers:
        if letter in "Erstl":
            translation = translation + "z"
        else:
            translation = translation + letter
        return translation

print(translate)

import random


x = "y"

while x == "y":

    no = random.randiant(1, 6)
x = input("press y to roll again and n to exit:")


