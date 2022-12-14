import numpy as np

x=2
print(x)

x = x + 5
print(x)

x = 2
x += 5
print(x)

y = 3
x = y**3
print (x)

pi = np.pi
print(pi)
z = y**2 + (5+x) + 1 - pi
print(z)

i = 1
while i<11:
    print(i)
    i =i+1

del i
i = 1
while i<11:
    print(i * '*')
    i = i+1

names = ["steelers" , "ravens" , "browns" , "bengals"]
print(names)
print(names[0])
print(names[-1])
print(names[-2])
print(names[-3])

numbers = [1,2,3,4,5]

for item in numbers:
    print(item)

i=0
while i< len(numbers)
    print(numbers[i])
    i = i+1
