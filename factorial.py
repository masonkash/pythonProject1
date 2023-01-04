num = input("What number?")
factorial = 1
print(num + " is the number")
if int(num) <0:
    print( "factorial does not exist")
elif int(num) ==0:
    print("factorial is 1")
elif int(num) >0:
    for i in range(1, int(num)+1):
        factorial = factorial * i
    print("the factorial of", num, "is", factorial)







