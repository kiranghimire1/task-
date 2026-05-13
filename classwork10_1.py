1
# # items=[3,5,7,9,11,13]
# # r_item=items.pop(4)
# # items.insert(2,r_item)
# # items.append(r_item)
# # print(items)

2
# #  first_set = {23, 42, 65, 57, 78, 83, 29}
# # second_set = {57, 83, 29, 67, 73, 43, 48}
# # common = first_set.intersection(second_set)
# # if common == set():
# #     print('no common elements')
# # else:
# #     difference = first_set.symmetric_difference(second_set)
# #     print(difference)

# # 3.
# first_set={27,43,34}
# second_set={34,93,22,27,43,53,48}
# if first_set.issubset(second_set) or first_set.issuperset(second_set):
#  first_set.clear()
#  print(first_set)
# else:
#  print('first set is not subset or superset of second set')

# #  4.
# month={'jan':47, 'feb':52,'march':47,'april':44,'may':53,'june':53,'july':54,'aug':44,'sept':54}
# list=list(set(month.values()))
# print(list)

# # 5.
# sample_list=[87,45,41,65,94,41,99,94]
# tuple=tuple(sample_list)#con=mmon values removes..
# print(max(tuple) and min(tuple))

# 6.
# clubA={'ram',"hari",'shyam'}
# clubB={'ram','sam','hari'}
# common=clubA.intersection(clubB)
# if common==set():
#  print('no common members')
# else:
#  print(common) 

#    7
# required_task={'email','report','meeting'}
# complete_tasks={'email','report'}
# common=required_task.issubset(complete_tasks)
# pending=required_task-complete_tasks
# if common:
#  print(' task has been complited') 
# else:
#   print(f'these tasks has been completed{pending}')

# #   8.
# students={'ram':'ram.@gmail.com','hari':'hari.@gmail.com','sita':'sita.@gmail.com','gita':'gita.@gmail.com'}
# user=input('enter your user name:  ')
# if user in students:
#   required=students.value(user)
#   print(f'Email:{students[user]}' )
# else:
#   print('user not found ')

# #   9.
# shopping_list={'milk','bread','eggs'}
# bought={'bread','eggs'}
# pending=shopping_list-bought
# if pending:
#  print(f'unbought items{pending}') 
# else:
#   print('shopping completed')
  
# # 10
# class_list=['ram','sita','laxman']
# new_student=input('enter your name: ')
# if new_student in class_list:
#   print('you are already enrolled.')
# else:
#   class_list.append(new_student)  
#   print('added successfully')

# print(class_list)  

# # 11
# votes=['blue','red','blue','green','blue']
# if votes.count('blue') >=3:
#   print('blue wins')
# else:
#   print('blue looses')  
  
# # 12.
#   grades={'ram':92,'sita':98}
#   user=input('enter your name:  ')
#   if user in grades:
#     mark=grades[user]
#     print(f'your grade is {mark}')
#   else:
#     print('user not found!!!!')
     
# # 14
# banned_items: {"scissors", "knife", "lighter"}
# baggage_weight=float(input('enter your baggage_weight in kgs:  ')).lower().split()
# carried_items=(input('enter the items you are carrying: '))
# has_banned= any(items in banned_items for items in carried_items)
# if baggage_weight <=7 and  not has_banned :
#   print('bag allowed')
# else:
#   print('bag not allowed!!!!')  

# #   15.
# sample_dict = {
# 'emp1': {'name': 'Jhon', 'salary': 7500},
# 'emp2': {'name': 'Emma', 'salary': 8000},
# 'emp3': {'name': 'Shyam', 'salary': 500}
# }
# change=sample_dict["emp3"]['salary']=8500
# print(sample_dict)


# # 16
# Ram={'blue','red','brown','green'}
# Laxman={'purple','blue','violet'}
# common=any(items in Ram for items in Laxman)
# if common:
#   print('they have some common items')
# else:
#   print('they picked completely different items')  
