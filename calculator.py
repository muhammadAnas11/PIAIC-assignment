
print("-♦-♦-♦-♦-♦-♦-♦-♦-CALCULATOR-♦-♦-♦-♦-♦-♦-♦-♦-")
print("Choice:1 ADDITION")
print("Choice:2 SUBTRACTION")
print("Choice:3 MULTIPLICATION")
print("Choice:4 DIVISION")
print("Choice:5 MODE")
#if choice <=5  :
choice = int( input ("Enter your choice = " )) 
num1   = int( input ("Enter first number = " ))
num2   = int( input ("Enter second number = " ))
if choice == 1 :
            print("-----------ADDITION-----------")
            result = num1 + num2 
            print(" Addition of number is",result )
elif choice == 2 :
            print("-----------SUBTRACTION-----------")
            result = num1 - num2 
            print(" Subtraction of number is",result  ) 
elif choice == 3 :
            print("-----------MULTIPLICATION-----------")
            result = num1 * num2 
            print(" Multiplication of number is",result  )
elif choice == 4 :
            print("-----------DIVISION-----------")
            result = num1 / num2 
            print(" Division of number is",result  ) 
elif choice == 5 :
            print("-----------MODE-----------")
            result = num1 % num2 
            print(" Mode of number is",result  ) 
else:
            print("Oops! INVALID CHOICE ")