import re

condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

user_email=input("Enter your email ")

if re.search(condition,user_email):
   print(f'this is your email {user_email}')
else:
   print(f'{user_email} is woring')