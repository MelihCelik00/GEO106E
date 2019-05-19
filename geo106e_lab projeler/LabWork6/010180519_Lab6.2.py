num_519 = int(input("Write a integer number to calculate factorial of number: "))
factorial_519 = 1
if (num_519 < 0):
    print("Invalid number")

elif(num_519 == 0):
    print("Factorial of"+str(num_519)+"is 0")

for i_519 in range(1,num_519+1):
    
    factorial_519 *= i_519

print("Factorial of "+str(num_519)+" is "+str(factorial_519))