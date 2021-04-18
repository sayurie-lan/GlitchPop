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
# gen = input("Choose your gender\n")
# age = input("What is your age\n")
# if int(age) <= 0:
# 	print("Write the correct age")
# 	age = input("What is your age\n")

# gen = str(gen).upper()
# if (gen == "W" and int(age) >= 18) or (gen == "M" and int(age) >= 21):
# 	print("Ote ber")
# else:
# 	print("Kait uine")

# d = {
# 	'name' : 'Egor',
# 	'surname': 'EgorUlyKotiBar',
# 	'pas': 123123,
# 	'WW': True,
# 	'array': [12,2,3,24,3],
# 	'dd': {
# 	'2level': 'Egor2',
# 	'2pas': 21312
#   }
# }

# a = input('vvedite a')
# b = input('vvedite b')

# print(int(a), int(b))

# c = a
# a = b
# b = c

# print(a, b)

# a = input("vvedite a")
# b = input("vvedite b")

# print(a, b)
# a = int(a)
# b = int(b)
# a = a + b
# b = a - b
# a = a - b
# print(a, b)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])
# # ['apple', 'banana', 'cherry', 'orange']

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[4:])
# # ["kiwi", "melon", "mango"]

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# thislist[2] = 'KKKKK'
# fruit = thislist[3]
# print(thislist)
# print(fruit)

# a = [1,4,2,4,6,7,6,5,7]
# a = sorted(a)
# print(a)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# for i in thislist:
# 	print(i)

a = '''asd awd awd awD awd banana BanAna bananA apple asd asdw ad da BananA asd awd awd awD awd banana BanAna bananA apple asd asdw ad da BananA asd awd awd awD awd banana BanAna bananA apple asd asdw ad da BananA'''
b = a.upper()
# print(a)
# print(b)
b = b.split()
a = a.split()
for x in range(0, len(a)):
	if b[x] == "BANANA":
		a[x] = "BANANA"
a = ' '.join(a)
print(a)

# for x in range(0, len(b)):
# 	if b[x] == "BANANA":
# 		a[x] == "BANANA"
# print(a)