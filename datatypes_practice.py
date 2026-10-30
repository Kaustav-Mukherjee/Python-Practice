'''
Challenge 1: Identify the Data Types

Create the following variables:
a = 100
b = 45.67
c = "Python"
d = True
e = None
f = 3 + 5j
g = [10, 20, 30]
h = (10, 20, 30)
i = {10, 20, 30}
j = {"name": "Kaustav", "age": 25}

Requirements:
1. Print each variable's value.
2. Print its data type using type().
3. Identify which ones are mutable and immutable.

'''


a = 100
b = 45.67
c = "Python"
d = True
e = None
f = 3 + 5j
g = [10, 20, 30]
h = (10, 20, 30)
i = {10, 20, 30}
j = {"name": "Kaustav", "age": 25}

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))

'''
Challenge 2: Integer vs Float
Create two variables:
a = 25
b = 4

Perform the following operations:
- Normal division
- Floor division
- Modulus
- Exponentiation
Print the results along with their data types.

Bonus: Why does 25 / 4 return a float while 25 // 4 returns an integer?

'''

a = 25
b = 4
normal_div = a/b
floor_div = a//b
modulus = a%b
exponentiation = a**b

print(normal_div, floor_div, modulus, exponentiation)


'''
Challenge 3: String or Number?
Predict the output of the following code before executing it.
a = "100"
b = 20

print(a * 2)
print(int(a) + b)
print(float(a) / 4)
print(a + str(b))

Explain why Python produces different results for each operation.

'''

a = "100"
b = 20

print(a * 2)
print(int(a) + b)
print(float(a) / 4)
print(a + str(b))


'''

Challenge 4: Build a Unit Converter

Create a program that converts:
- Kilometres into metres.
- Metres into centimetres.
- Kilograms into grams.
- Hours into minutes.
Use variables and appropriate data types.

'''

# Distance_km = float(input('Enter the distance in kilometers: '))
# distance_m = Distance_km * 1000
# distance_cm = distance_m * 100

# weight_kg = float(input('Enter the weight in kilograms: '))
# weight_g = weight_kg * 1000

# time_hr = float(input('Enter the time in hours: '))
# time_min = time_hr * 60

# print(f"{Distance_km} km is equal to {distance_m} m and {distance_cm} cm.")
# print(f"{weight_kg} kg is equal to {weight_g} g.")
# print(f"{time_hr} hours is equal to {time_min} minutes.")

'''

Challenge 5: The Input Conversion Trap

Study this code:
age = input("Enter your age: ")
next_year = age + 1

print(next_year)

1. Identify the error.
2. Fix it using type conversion.
3. Print the user's age and next year's age.
4. Print the data type of both variables.
Bonus: What happens if someone enters twenty-five instead of 25?

'''

# age = int(input("Enter your age: "))
# next_year = age + 1
# print('Your age is:', age)
# print('Next year, you will be:', next_year)
# print(type(age))
# print(type(next_year))


'''

Challenge 6: Boolean Detective

Predict the output:
a = bool(0)
b = bool(1)
c = bool("")
d = bool("False")
e = bool([])
f = bool([0])

print(a, b, c, d, e, f)
Explain why "False" evaluates to True, even though it contains the word False.

'''

a = bool(0)        # Output: False, because 0 is considered as False in Python.
b = bool(1)        # Output: True, because 1 is considered as True in Python.
c = bool("")       # Output: False, because empty string is considered as False in Python.
d = bool("False")  # Output: True, because non-empty string is considered as True in Python.
e = bool([])       # Output: False, because empty list is considered as False in Python.
f = bool([0])      # Output: True, because non-empty list is considered as True in Python.

print(a, b, c, d, e, f)


'''

Challenge 7: String Manipulation

Given:
name = "  kaustav mukherjee  "

Remove leading and trailing spaces.
Convert the name into uppercase.
Convert it into lowercase.
Capitalize the first letter of each word.
Count the total characters.
Replace the space between the names with an underscore.
Check whether the cleaned name contains "kaustav".

'''

name = "  kaustav mukherjee  "

cleaned_name = name.strip()
uppercase_name = cleaned_name.upper()
lowercase_name = cleaned_name.lower()
capitalized_name = cleaned_name.title()
character_count = len(cleaned_name)
underscore_name = cleaned_name.replace(" ", "_")
contains_kaustav = "kaustav" in lowercase_name

print("Cleaned name:", cleaned_name)
print("Uppercase:", uppercase_name)
print("Lowercase:", lowercase_name)
print("Capitalized:", capitalized_name)
print("Character count:", character_count)
print("With underscore:", underscore_name)
print('Contains "kaustav":', contains_kaustav)


'''

Challenge 8: The Mixed Data Type Puzzle

Without executing the code, predict the output and data type of every expression.

a = 10
b = 3.5
c = "5"
d = True

result1 = a + b
result2 = a * d
result3 = c * 3
result4 = str(a) + c
result5 = float(c) + b
result6 = a / 2

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)

Bonus: Explain why True behaves like 1 in arithmetic operations.

'''

a = 10
b = 3.5
c = "5"
d = True

result1 = a + b
result2 = a * d
result3 = c * 3
result4 = str(a) + c
result5 = float(c) + b
result6 = a / 2

print(result1) # Output: 13.5, Data Type: float
print(result2) # Output: 10, Data Type: int , TRUE behaves like 1 in arithmetic operations because in Python, the boolean value True is treated as 1 and False is treated as 0 when used in arithmetic contexts.
print(result3) # Output: "555", Data Type: str
print(result4) # Output: "105", Data Type: str
print(result5) # Output: 8.5, Data Type: float
print(result6) # Output: 5.0, Data Type: float

'''

Challenge 9: Mutable vs Immutable

Study the following code:
a = [1, 2, 3]
b = a

a.append(4)

print(a)
print(b)

Now compare it with:
x = "Python"
y = x

x = x + " Programming"

print(x)
print(y)

Answer these questions:
1. Why do a and b both show the updated list?
2. Why does y retain its original string?
3. Which data type is mutable and which is immutable?

'''
# Why do a and b both show the updated list?
# Answer: In the first code snippet, both a and b refer to the same list object in memory. When we append 4 to a, it modifies the list in place, and since b is referencing the same list, it also reflects the change.

# Why does y retain its original string?
# Answer: In the second code snippet, strings are immutable in Python. When we concatenate " Programming" to x, it creates a new string object and assigns it to x. The original string that y references remains unchanged.

# Which data type is mutable and which is immutable?
# Answer: Lists are mutable, meaning they can be changed after creation. Strings are immutable, meaning they cannot be changed after creation.

a = [1, 2, 3]
b = a

a.append(4)

print(a)
print(b)

x = "Python"
y = x

x = x + " Programming"

print(x)
print(y)


'''

Challenge 10: Mini Project — Student Data Analyzer
Build a student information and result analyzer.

Start with these values:
name = "Kaustav Mukherjee"
age = 25
course = "ETCE"
maths = 87
physics = 92
programming = 96
attendance = 85.5
passed = True

Your program should:
1. Display all student information.
2. Calculate total marks.
3. Calculate average marks.
4. Convert the average into a string for display.
5. Display attendance as a percentage.
6. Print the data type of every variable.
7. Create a formatted student report using f-strings.
8. Use a Boolean variable to display whether the student has passed.
Bonus: Create a list containing all three subject marks and calculate its total using sum().

'''

name = "Kaustav Mukherjee"
age = 25
course = "ETCE"
maths = 87
physics = 92
programming = 96
attendance = 85.5
passed = True

Total_marks = maths + physics + programming
Average_marks = Total_marks / 3
Subject_marks = [maths, physics, programming]
Total_subject_marks = sum(Subject_marks)

print(f"Student Name: {name}")
print(f"Age: {age}")
print(f"Course: {course}")
print(f"Maths: {maths}")
print(f"Physics: {physics}")
print(f"Programming: {programming}")
print(f"Total Marks: {Total_marks}")
print(f"Average Marks: {Average_marks}")
print(f"Subject Marks List: {Subject_marks}")
print(f"Total Subject Marks: {Total_subject_marks}")
print(f"Attendance: {attendance}%")
print(f"Passed: {passed}")

print("\nData Types:")
for var in [name, age, course, maths, physics, programming, attendance, passed]:
    print(f"{var}: {type(var).__name__}")








