'''

Challenge 1: Introduce Yourself
Create three variables: name, age, and city. Assign your own values and print them in a sentence. 

'''

name = 'Kaustav'
age = 25
city = 'Kolkata'

f = f'My name is {name}, I am {age} years old, and I live in {city}'

print(f)

'''

Challenge 2: Swap Two Variables
Create two variables, a = 10 and b = 20. Swap their values so that a becomes 20 and b becomes 10.
Bonus: Can you do it without creating a third variable?

'''

a = 10
b = 20

b, a = a, b

print(a)
print(b)

'''

Challenge 3: Simple Calculator
Create two variables, num1 = 45 and num2 = 15. Perform the following operations:
- Addition
- Subtraction
- Multiplication
- Division

'''

num1 = 45
num2 = 15

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1/num2

print(sum, difference, product, quotient)

'''

Challenge 4: Shopping Bill

You bought:
- 2 notebooks at ₹50 each
- 3 pens at ₹10 each
- 1 bag at ₹750
Store the quantities and prices in variables. Calculate and print the total bill.

'''

notebook_price = 50
notebook_quantity = 2

pen_price = 10
pen_quantity = 3

bag_price = 750
bag_quantity = 1

Total_bill = (notebook_price * notebook_quantity) + (pen_price * pen_quantity) + (bag_price * bag_quantity)

print(Total_bill)


'''

Challenge 5: Temperature Converter
Create a variable called celsius with the value 37. Use another variable to calculate the temperature in Fahrenheit.
Formula: \(F = (C \times 9/5) + 32\)

'''

celsius = 37
Fahrenheit = (celsius * 9/5) + 32
print(f'{celsius}°C = {Fahrenheit}°F')

'''

Challenge 6: Understand Variable Types
Create these variables:
student_name = 'Kaustav'
marks = 87.5
passed = True
rank = 3

Print the value and data type of each variable using type().

'''

student_name = 'Kaustav'
marks = 87.5
passed = True
rank = 3

print(type(student_name))
print(type(marks))
print(type(passed))
print(type(rank))


'''

Challenge 7: Predict the Output

Without running this code, predict the final values of x and y.
x = 5
y = x
x = 10
y = x + y
print(x)
print(y)

Explain why those values appear.

'''

x = 5
y = x
x = 10
y = x + y
print(x)
print(y)

#Explanation: Initially, x is assigned the value 5. Then y is assigned the value of x, which is 5. After that, x is updated to 10. Finally, y is updated to the sum of the new value of x (which is 10) and the old value of y (which was 5), resulting in y being 15. Therefore, the final values are x = 10 and y = 15.


'''

Challenge 8: Fix the Variables

This code contains mistakes. Correct it so that it runs successfully.
name = "Kaustav"
age = 23
city = Kolkata

print("My name is " + name)
print("I am " + age + " years old")
print("I live in " + city)

Goal: Fix the code without changing the intended meaning of the output.

'''

name = "Kaustav"
age = 23
city = 'Kolkata'

print("My name is " + name)
print("I am " + str(age) + " years old")
print("I live in " + city)


'''

Challenge 9: The Bank Balance

Your initial bank balance is ₹5,000. You deposit ₹1,500 and then withdraw ₹800.
1. Store the initial balance in a variable.
2. Update it after the deposit.
3. Update it again after the withdrawal.
4. Print the final balance.

Bonus: Solve it using the += and -= operators.

'''

# Store the initial balance
balance = 5000

# Deposit ₹1,500
balance = balance + 1500

# Withdraw ₹800
balance = balance - 800

# Print the final balance
print("Final Balance:", balance)


'''

Challenge 10: Build Your Own Profile Card
Create variables for your name, age, course, college, and favourite programming language. Print a neatly formatted profile using an f-string.

Example:

===== MY PROFILE =====
Name: Alex
Age: 22
Course: Computer Science
College: ABC College
Favourite language: Python
======================

'''

name = "Kaustav"
age = 25
course = "ETCE"
college = "IIEST, Shibpur"
favourite_language = "Python"

profile = f"""
{'='*7} MY PROFILE {'='*7} 
Name: {name}
Age: {age}
Course: {course}
College: {college}
Favourite language: {favourite_language}
{'='*27}
"""

print(profile)



























