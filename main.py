# -*- coding: utf-8 -*-
# print("hello world")
# print("ALibi chort")

# data types

# string
# a = 'asdasd'
# b = "asdasdasd"
# c = '''asdasdasd'''

# int
# a = 1123

# # float
# a = 23.123

# a1 = [1,2,3, '223']

# d = {
#   'asd': 123,
#   '23': 233
# }

# # boolean
# a = True
# a = False

# print(type(d))

# a = '123'      ПРЕОБРАЗОВАТЬ ПЕРЕМЕННЫЕ ТИПЫ
# a = str(a)
# print(a)
# print(type(a))

# x = range(5, 6)
# print(x)

# a = 1
# b = "1"
# c = 1.14

# d = a + float(b) + c

# print(round(d, 3))

# a = input("Input the Radius\n")
# S = float(a)**2*3.14
# print(float(S))

# print(a)
# a = print(type(a))

# name = input("Your Name ")
# a = f"Hello {name}"
# print(a)
# password1 = '2222'#Jack
# password2 = '3333'#Nick

# user_input = input("Введи пароль")

# if user_input == password1:
#   print('Hello Jack')
# elif user_input == password2:
#   print('hello Nick')
# else:
#   print('wrong password!')

# a = input("Value 1 is: ")
# b = input("Value 2 is: ")

# oper = input("Input the operant(*, /, +, -)")
# a = int(a)
# b = int(b)
# if oper == "+":
# 	print(int(a) + int(b))
# elif oper == "-":
# 	print(int(a) - int(b))
# elif oper == "*":
# 	print(int(a) * int(b))
# elif oper == "/":
# 	if b == 0:
# 		print("you cannot divide to 0")
# 	else:
# 		print(int(a) / int(b))
gen = input("Choose your gender\n")
age = input("What is your age\n")
if int(age) <= 0:
	print("Write the correct age")
	age = input("What is your age\n")

gen = str(gen).upper()
if (gen == "W" and int(age) >= 18) or (gen == "M" and int(age) >= 21):
	print("Ote ber")
else:
	print("Kait uine")