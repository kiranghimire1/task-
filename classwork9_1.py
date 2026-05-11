# #4. Design a program for a 'Student Resource Portal.' The program should
# ask for a username and a password.
#  If the username is admin and password is ad123, print
# Access Granted: Faculty Dashboard.
#  If the username is student and password is st2026, print
# Access Granted: Notes and Practice Questions.
#  For any other combination, print Invalid Credentials.
# Please try again
# print('STUDENT PORTAL')
# username=input('enter username:  ')
# password=input('enter password:  ')
# if username=='admin' and password=='ad123':
#     print("Access Granted: Faculty Dashboard.")
# elif username=='student' and password=='st2026': 
#     print('Access Granted: Notes and Practice Questions')  
# else:
#     print("Invalid Credentials.Please try again")

#  # 6. Create a Python program for a text-based adventure game called
# Magic Forest based on the given flowchart. The program should follow
# the exact logic shown in the flowchart.

# print("WELCOME TO THE MAGIC FOREST")
# stage1=input('choose NORTH or SOUTH: ').lower()
# if stage1=='south':
#     stage2=input('CROSS THE RIVER or FOLLOW THE PATH: ').lower()
#     if stage2=='follow the path':
#         stage3=input('choose FAIRY,OGRE,or ELF?:').lower()
#         if stage3=='elf':
#             print("PLAYER WON THE GAME")
#         else:
#             print("PLAYER LOOSE THE GAME")   
#     else:
#          print("PLAYER LOOSE THE GAME") 
# else:
#     print("PLAYER LOOSE THE GAME")      
# 
# # 
# #     5. Write a Python program that calculates a customer's final bill based
# on their spending and membership status. The program should follow
# the exact logic shown in the flowchart.
#  purchase_amount=int(input('enter your total purchase amount: '))
# if purchase_amount>5000:
#     membership=input('do you have a membership (yes/no): ')
#     if membership=='yes':
#         discount= 0.3*purchase_amount
#         final_price=purchase_amount-discount
#         print(f"final price is {final_price}")
#         print(f"discount amount is {discount}")
#     else:
#         print(f'final price is {purchase_amount}')
# else: 
#     print(f'final price is {purchase_amount}')  
#   
# # 10. Write a Python program that calculates a person’s Body Mass
# Index and determines their weight category based on the following
# rules:  
# weight=float(input('enter your weight in kgs: '))
# height=float(input('enter your height in m: '))
# bmi=weight/(height**2)
# print(f"your BMI is {bmi:.2f}")
# if bmi<18.5:
#     print ('!!!you are under weight!!!!')
# elif 18.5 < bmi and bmi<25:
#     print("you have normal weight")
# elif 25 < bmi and bmi < 30:
#     print('you are over weight')
# else:
#     print('you are obese')  

#  16. A utility company charges different rates based on electricity
# usage:
# If usage < 100 units then cost Rs 5 per unit
# If usage is between 100 to 300 units:
# First 100 units: Rs 5
# Next units: Rs 8
# If usage is > 300 units: First 100: Rs 5 Next 200: Rs 8 Remaining: Rs 10

# unit=float(input("enter your electricity consumed unit:  "))
# if unit<=100:
#     cost= unit*5
#     print(f"electricity bill is Rs.{cost} ")
# elif unit<=300:
#     cost=100*5 + (unit-100)*8
#     print(f'electriciy bill is {cost}')
# else:
#     cost=100*5+200*8+(unit-300)*10
#     print(f"electricity bill is {cost} ")
# 
  
# # 18. Write a Python program that takes a number as input, first
# checks if it is positive if yes then check whether it is even or odd.
  
# num=int(input('enter the number'))
# if num>0:
#     if num%2=="0":
#         print('Given number is even')
#     else:
#         print('Given number is odd')

# #19. A store gives a 20% discount if the total purchase is above RS
# 1000 AND the customer is a member, or a 10% discount if the
# purchase is above RS 1000 but the customer is not a member. Write a
# program that takes total_amount and is_member (True/False) as
# input and prints the final amount after applying the correct discount
# or no discount

# total_purchase=int(input("enter your total purchase:  "))
# member=input('are you a member of our shop(yes/no): ')
# if total_purchase>=1000 and member=='yes':
#     discount=0.2*total_purchase
#     final_price=total_purchase-discount
#     print(f'your total amount is{final_price}')
#     print(f'your discount amount is{discount}')
# elif total_purchase>=1000 and member=='no':
#          discount=0.1*total_purchase
#          final_price=total_purchase-discount
#          print(f'your total amount is{final_price}')
#          print(f'your discount amount is{discount}')

# else:
#        print(f"your total amount is {total_purchase} ")    
# 
# 
# # 20. Create a weight conversion program that:
# Asks the user what their Earth weight is as a float. Asks
# the user for a planet number as an int.
# Then, use an if/elif/else statement to calculate the user's weight on
# the destination planet.
# To calculate the user's weight: destination weight=Earth weight ×
# relative gravity     

# weight=float(input('enter your weoght on earth: '))
# planet=input('enter the planet number(1-7) you want for weight conversion: ')
# if planet=='1':
#     destination_weight=weight*0.38
#     print(f'your destination weight onMercury is {destination_weight} ')
# elif planet=='2':
#      destination_weight=weight*0.91
#      print(f'your destination weight on Venus is {destination_weight} ')
# elif planet=='3':
#      destination_weight=weight*0.38
#      print(f'your destination weight on Mars is {destination_weight} ')
# elif planet=='4':
#      destination_weight=weight*2.53
#      print(f'your destination weight on Jupiter is {destination_weight} ')
# elif planet=='5':
#      destination_weight=weight*1.07
#      print(f'your destination weight on Saturn is {destination_weight} ')
# elif planet=='6':
#      destination_weight=weight*0.89
#      print(f'your destination weight on uranus is {destination_weight} ')
# elif planet=='7':
#      destination_weight=weight*1.14
#      print(f'your destination weight on Neptune is {destination_weight} ')

# 21. WAP which accepts marks of four subjects and display total
# marks, percentage and grade. Hint: more than 70 –> distinction, more
# than 60 –> first, more than 40 –> pass, less than 40 –> fail



# m1, m2, m3, m4 = map(int, input("enter marks of 4 subjects: ").split())

# total_marks=m1+m2+m3+m4
# percentage=(total_marks/400)*100
# grade=total_marks/4
# print(f'total marks is {total_marks}\n percentage is{percentage}%\n grade is{grade}')
# if percentage>=70:
#     print('distinction')
# elif percentage>=60:
#     print('first')
# elif percentage>=40 :
#     print('second ')
# else:
#     print('fail')     
# 
# 
# #   23. Write a program that simulates the elevator's internal logic. The
# program should accept user inputs for the desired floor, the current weight
# load, and the door status, then determine if the elevator is cleared to move.

# floor=int(input('enter floor number: '))
# if floor<0 or floor>10:
#     print("invalid floor")
# else:    
#     weight=int(input('enter the total weight: '))
#     if weight>500:
#         print('OVERWEIGHT: LIFT CANNOT MOVE ')
#     else:    
#         door=input ( "is the door closed(yes/no: )")
#         if door=='yes':
#          print("activate elivator motion")
#         else: 
#            print("WARNING: CLOSE THE DOOR")