##Lab Two

'''
1. Write a program that asks the user for the current temperature in degrees Farenheit.
Print “Wear a coat” if the temperature is below 60 degrees.
'''

userTemp = int(input("Please enter the current temporature in your area: "))

if (userTemp < 60):

    print("Wear a coat.");



'''
2. Write a program that prints “Number is within range” when a number is in between -10 and 10 inclusive.
'''

import random

tester = random.randint(-100, 100)

print(tester)

if (-10 <= tester <= 10):

    print("Number is within range")



'''
3. Write a program that asks the user to input a grade between 0 and 100. The program must output a letter grade.
Use the ranges defined in the class syllabus to define the letters. Use the if-else statement. (Use the ELIF statement,
Section 3.9)
'''

grade = int(input("Please enter a grade: "))

if (grade >= 90):
    print("A")

elif (90 >= grade > 80):
    print("B")

elif (80 >= grade > 70):
    print("C")

elif (70 >= grade > 60):
    print("D")

else:
    print("F")



'''
4. Write a program that asks the user to input 4 numbers. The program must output the greatest of those numbers.
DO NOT use the max() function.
'''

print("Please enter four numbers in the following prompt.\n\n")

userInput = [int(input("Please enter a number: ")) for i in range(4)]

maxValue = userInput[0]

for i in range(1, 4):
    if (userInput[i] > maxValue):
        maxValue = userInput[i]

print("The greatest value is:", maxValue)
