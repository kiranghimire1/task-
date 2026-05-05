# #1. A theme park has these rules: You can ride the roller coaster if you are at least 12 years old AND at least 140 cm tall. 
# # Write the if-else code for this.

# age = int(input("Enter your age: "))
# height = int(input("Enter your height in cm: "))

# if age >= 12 and height >= 140:
#     print("You can ride the roller coaster!")
# else:
#     print("You cannot ride the roller coaster.")


# #2.    Design a Traffic Light System. Given a variable light that can be "red", "yellow", or "green", print the correct instruction.
# #  Also handle an invalid color with an error message.

# light = input("Enter the traffic light color (red/yellow/green): ").lower().strip()

# if light == "red":
#     print("STOP! Do not proceed.")
# elif light == "yellow":
#     print("CAUTION! Prepare to stop.")
# elif light == "green":
#     print("GO! You can proceed.")
# else:
#     print("ERROR: Invalid color! Please enter 'red', 'yellow', or 'green'.")

# #3. Write a match statement that takes a number 1–4 and prints the corresponding season:
# # 1 = spring, 2 = summer, 3 = autumn, 4 = winter.
# # Default: "unknown".
# season_num = int(input("Enter a number (1-4): "))

# match season_num:
#     case 1:
#         print("spring")
#     case 2:
#         print("summer")
#     case 3:
#         print("autumn")
#     case 4:
#         print("winter")
#     case _:
#         print("unknown")

# #4. Write a login system using nested if. Check:
# # If username equals "admin"
# # Inside that, if password equals "pass123"
# # Print appropriate messages for: valid login, wrong password, wrong username.    
# username = input("Enter username: ")
# password = input("Enter password: ")

# if username == "admin":
#     if password == "pass123":
#         print("Login successful! Welcome admin.")
#     else:
#         print("Wrong password!")
# else:
#     print("Wrong username!")  

# #    5. Design a Bank Loan Approval System. Approve a loan only if ALL three conditions are met:
# # Age is between 21 and 60 (inclusive)
# # Monthly income is at least 30,000
# # Credit score is at least 700
# # If not approved, print which condition failed. 
# # If multiple fail, pick the most important one to report
# age = int(input("Enter your age: "))
# income = int(input("Enter monthly income: "))
# credit_score = int(input("Enter credit score: "))

# if 21 <= age <= 60:
#     if income >= 30000:
#         if credit_score >= 700:
#             print("Loan APPROVED!")
#         else:
#             print("Loan DENIED: Credit score too low (need 700+)")
#     else:
#         print("Loan DENIED: Monthly income too low (need 30,000+)")
# else:
#     print("Loan DENIED: Age not eligible (must be 21-60)")

# #6. You are developing a simple ticket booking system for a movie theatre. The ticket price depends on the age of the person and whether they have a membership card:
# # If under 12: ticket is free
# # If age is between 12 and 60:
# # With membership: Rs. 150
# # Without membership: Rs. 200
# # If above 60: ticket costs Rs.
# # 100 (senior citizen discount)
# # Write a Python program using nested if-else to 
# # calculate and print the ticket price based on age and membership status.    
# age = int(input("Enter your age: "))
# has_membership = input("Do you have membership? (yes/no): ").lower().strip() == "yes"

# if age < 12:
#     price = 0
#     print(f"Ticket price: Rs. {price} (Free for children)")
# elif age <= 60:
#     if has_membership:
#         price = 150
#         print(f"Ticket price: Rs. {price} (Member discount)")
#     else:
#         price = 200
#         print(f"Ticket price: Rs. {price} (Regular price)")
# else:
#     price = 100
#     print(f"Ticket price: Rs. {price} (Senior citizen discount)")


#  #   7. A company gives a bonus of 5% to an employee if their years of service is more than 5 years. 
#  # Ask the user for their salary and years of service, and print the net bonus amount.
# salary = float(input("Enter your salary: "))
# years_of_service = int(input("Enter years of service: "))

# if years_of_service > 5:
#     bonus = salary * 0.05
#     print(f"Congratulations! Your bonus is: Rs. {bonus:.2f}")
# else:
#     print("No bonus eligible (requires more than 5 years of service)")


# #8. Write a Python program that accepts the radius of a circle from the user and computes the area.    
# import math

# radius = float(input("Enter the radius of the circle: "))
# area = math.pi * radius ** 2
# print(f"Area of the circle: {area:.2f}")

# #9. Accept the age, gender ('M', 'F'), and number of days, and display the wages accordingly based on the following criteria:
# # If age is ≥ 18 and < 30:
# # Male (M): 700 per day
# # Female (F): 750 per day
# # If age is ≥ 30 and < 40:
# # Male (M): 800 per day
# # Female (F): 850 per day
 
# age = int(input("Enter age: "))
# gender = input("Enter gender (M/F): ").upper().strip()
# days = int(input("Enter number of days: "))

# if 18 <= age < 30:
#     if gender == 'M':
#         rate = 700
#     else:  
#         rate = 750
# elif 30 <= age < 40:
#     if gender == 'M':
#         rate = 800
#     else:  
#         rate = 850
# else:
#     rate = 0
#     print("No wage rate defined for this age group")

# if rate > 0:
#     wages = rate * days
#     print(f"Wages: Rs. {wages}")
# else:
#     print("Invalid age or gender!!!!")

# #    10. Accept a number from the user and print the output based on the following conditions:
# # If the number is a multiple of both 3 and 5, print "Fizz Buzz" instead of the number.
# # If the number is a multiple of 3 but not 5, print "Fizz" instead of the number.
# # If the number is a multiple of 5 but not 3, print "Buzz" instead of the number.
# # If the number is not a multiple of 3 or 5, print the number as it is.
  
# number = int(input("Enter a number: "))

# if number % 3 == 0 and number % 5 == 0:
#     print("Fizz Buzz")
# elif number % 3 == 0:
#     print("Fizz")
# elif number % 5 == 0:
#     print("Buzz")
# else:
#     print(number)