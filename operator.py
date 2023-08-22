
#Python Script that accepts user input for a mathematical operation (Assignment)

#Get the mathematical operation from the user
operator = input("Enter the mathematical operation (+, -): ")

#Get the number from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter thr second number: "))

#Perform the operation on user input
if operator == "+":
    result = num1 + num2
if operator == "-":
    result = num1 - num2

#Display the result 
print("result:",result)
