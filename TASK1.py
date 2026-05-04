#1.Write a program to check whether the given number is in between 1 and 100 or not.
# num = int(input("Enter a number: "))

# if num >= 1 and num <= 100:
#     print("The number is between 1 and 100.")
# else:
#     print("The number is NOT between 1 and 100.")


#2. Check whether the user input number is even or odd and   display it to user
# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("The number is Even.")
# else:
#     print("The number is Odd.")
#

#  #3. Write a program that asks the user for a number in the range of 1 to 12. The program should display the corresponding month, where 
# # 1=january, 2=february,3=march,4=april,5=may,6=june,7=july,8=august,9=september,10=october,11=november,12=december. The program should display an error 
# #  message if the user enters a number that is outside the range of 1 to 12.
# num = int(input("Enter a number (1-12): "))

# if num == 1:
#     print("January")
# elif num == 2:
#     print("February")
# elif num == 3:
#     print("March")
# elif num == 4:
#     print("April")
# elif num == 5:
#     print("May")
# elif num == 6:
#     print("June")
# elif num == 7:
#     print("July")
# elif num == 8:
#     print("August")
# elif num == 9:
#     print("September")
# elif num == 10:
#     print("October")
# elif num == 11:
#     print("November")
# elif num == 12:
#     print("December")
# else:
#     print("Error: Number must be between 1 and 12.")

#4. A school has following rules for grading system:
# a. Below 25 - F 
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

# marks = float(input("Enter your marks: "))

# if marks < 25:
#     print("Grade: F")
# elif marks < 45:
#     print("Grade: E")
# elif marks < 50:
#     print("Grade: D")
# elif marks < 60:
#     print("Grade: C")
# elif marks < 80:
#     print("Grade: B")
# else:
#     print("Grade: A")


#5.Write a program to check whether a number is divisible by 7 or not
# num = int(input("Enter a number: "))

# if num % 7 == 0:
#     print("The number is divisible by 7.")
# else:
#     print("The number is NOT divisible by 7.")

#6.Write a program to accept two numbers and mathematical operators and perform operation accordingly. Like: Enter First Number: 7 Enter Second Number : 9 Enter operator : + Your Answer is : 16
# num1 = float(input("Enter First Number: "))
# num2 = float(input("Enter Second Number: "))
# op = input("Enter operator (+, -, *, /): ")

# if op == "+":
#     result = num1 + num2
# elif op == "-":
#     result = num1 - num2
# elif op == "*":
#     result = num1 * num2
# elif op == "/":
#     if num2 != 0:
#         result = num1 / num2
#     else:
#         result = "Error: Division by zero"
# else:
#     result = "Error: Invalid operator"

# print("Your Answer is:", result)

#7.Write a Python program to check car loan eligibility:Salary >= 50,000 and Credit Score >= 700: "Eligible"
# Otherwise: "Not Eligible"

# salary = float(input("Enter your salary: "))
# credit_score = int(input("Enter your credit score: "))

# if salary >= 50000 and credit_score >= 700:
#     print("Eligible")
# else:
#     print("Not Eligible")

#8. Write a Python program that takes an integer input n n. From given number, check if it is divisible by both 3 and 5, and print "FizzBuzz" 
#if true. If the number is divisible only by 5, print "Buzz." If it is divisible only by 3, print "Fizz." Finally, if the number is not divisible by either 3 or 5,
#print the number itself.
# n = int(input("Enter a number: "))

# if n % 3 == 0 and n % 5 == 0:
#     print("FizzBuzz")
# elif n % 5 == 0:
#     print("Buzz")
# elif n % 3 == 0:
#     print("Fizz")
# else:
#     print(n)


#9.Write a Python program that takes a character input and checks whether it is a vowel or consonant.
# ch = input("Enter a character: ").lower()

# if ch.isalpha() and len(ch) == 1:
#     if ch in ['a', 'e', 'i', 'o', 'u']:
#         print("It is a vowel.")
#     else:
#         print("It is a consonant.")
# else:
#     print("Invalid input. Please enter a single alphabet character.")

#10. Write a Python program to input marks and determine the grade based on the following conditions:
# 90-100: A
#80-89: B
#70-79: C
#Below 70: Fail
# marks = float(input("Enter your marks: "))

# if 90 <= marks <= 100:
#     print("Grade: A")
# elif 80 <= marks <= 89:
#     print("Grade: B")
# elif 70 <= marks <= 79:
#     print("Grade: C")
# elif marks < 70:
#     print("Fail")
# else:
#     print("Invalid marks")

#11. Write a Python program to categorize a person’s age:
# Age < 13: Child
# 13 <= Age <= 19: Teenager
# Age > 19: Adult
# age = int(input("Enter your age: "))

# if age < 13:
#     print("Child")
# elif 13 <= age <= 19:
#     print("Teenager")
# else:
#     print("Adult")


#12.Write a Python program to check if a given character is uppercase, lowercase, or a digit.
# ch = input("Enter a character: ")

# if len(ch) == 1:
#     if ch.isupper():
#         print("Uppercase letter")
#     elif ch.islower():
#         print("Lowercase letter")
#     elif ch.isdigit():
#         print("Digit")
#     else:
#         print("Special character")
# else:
#     print("Please enter only a single character.")

#13. Write a Python program that takes a color as input ("Red", "Yellow", "Green") and outputs the corresponding action ("Stop", "Get Ready", "Go").
# color = input("Enter color (Red, Yellow, Green): ").strip().lower()

# if color == "red":
#     print("Stop")
# elif color == "yellow":
#     print("Get Ready")
# elif color == "green":
#     print("Go")
# else:
#     print("Invalid color input")

#14.Write a Python program to check eligibility for a job based on age and experience:
#Age > 18 and Experience >= 2 years: Eligible
#Otherwise: Not Eligible
# age = int(input("Enter your age: "))
# experience = float(input("Enter your experience in years: "))

# if age > 18 and experience >= 2:
#     print("Eligible")
# else:
#     print("Not Eligible")

#15. Write a Python program to give advice based on the temperature:
# Temperature > 30°C: "It's hot, stay hydrated!"
# Temperature between 15-30°C: "Enjoy the weather!"
# Temperature < 15°C: "It's cold, wear warm clothes!"
# temp = float(input("Enter the temperature in °C: "))

# if temp > 30:
#     print("It's hot, stay hydrated!")
# elif 15 <= temp <= 30:
#     print("Enjoy the weather!")
# else:
#     print("It's cold, wear warm clothes!")

#16.. Write a Python program that takes a menu option ("Pizza", "Burger", "Pasta") and prints its price:
# Pizza: $10
# Burger: $7
# Pasta: $8
# item = input("Enter your choice (Pizza, Burger, Pasta): ").strip().lower()

# if item == "pizza":
#     print("Price: $10")
# elif item == "burger":
#     print("Price: $7")
# elif item == "pasta":
#     print("Price: $8")
# else:
#     print("Invalid menu option")


#17. Write a Python program to select players based on height:
# Height >= 6 feet: Selected
# Height < 6 feet: Not Selected

# height = float(input("Enter your height in feet: "))

# if height >= 6:
#     print("Selected")
# else:
#     print("Not Selected")
 

#18.Write a Python program to check if a person is eligible to watch a movie based on their age:
# Age >= 18: Allowed
# Age < 18: Not Allowed
# age = int(input("Enter your age: "))

# if age >= 18:
#     print("Allowed")
# else:
#     print("Not Allowed")

#19.Write a Python program to check login credentials:
# Username: "admin", Password: "password123"
# If correct, print "Access Granted"; otherwise, print "Access Denied."
# username = input("Enter username: ")
# password = input("Enter password: ")

# if username == "admin" and password == "password123":
#     print("Access Granted")
# else:
    # print("Access Denied")
#20.Write a Python program that takes a month number (1–12) and outputs the corresponding season:
# 12, 1, 2: "Winter"
# 3, 4, 5: "Spring"
# 6, 7, 8: "Summer"
# 9, 10, 11: "Autumn"
# month = int(input("Enter month number (1-12): "))

# if month in [12, 1, 2]:
#     print("Winter")
# elif month in [3, 4, 5]:
#     print("Spring")
# elif month in [6, 7, 8]:
#     print("Summer")
# elif month in [9, 10, 11]:
#     print("Autumn")
# else:
#     print("Invalid month number")