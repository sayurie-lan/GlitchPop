# def my_func(a, b):
# 	return (int(a) * int(b))
# a = input()
# b = input()
# c = my_func(a, b)
# print(f"The sum of a multuple {a}, {b} is ", c)
# import my_module as mmod
# mmod.age()
# print(mmod.a)
# import algorithm as (plus, minus)
# import algorithm as algo
# import string_work as sw
# algo.plus(1, 3)
# algo.minus(4, 3)
# sw.add_str('asd', 'www')
# x = datetime.datetime(2020, 5, 17)
# print(x)
# print(x.strftime("%d.%m.%Y %H:%M"))

# ------WORKING WITH EXCEL

# from openpyxl import load_workbook

# wb = load_workbook('asd.xlsx')

# # print(wb.get_sheet_names())
# sheet = wb.get_sheet_by_name('users')
# # print(sheet['A2'].value)
# # print(sheet['A2'].row)
# # print(sheet['A2'].column)
# # print(sheet['A2'].coordinate)

# for i in range(1, 4):
# 	print(i, sheet.cell(row=i, column=1).value)
# sheet['A2'].value = 'QQQQ'
# wb.save('changed.xlsx')

# --------SALARY
# from openpyxl import load_workbook
# wb = load_workbook('salary.xlsx')

# sheet = wb.get_sheet_by_name('Database')
# sum1 = 0
# for i in range (4, 25):
# 	# print(sheet.cell(row=i, column=11).value)
# 	sum1 += sheet.cell(row=i, column=11).value
# sheet['K26'].value = sum1
# print(sum1)

# wb.save('salary.xlsx')

#------------REQUEST

import requests
import json

# r = requests.get('https://jsonplaceholder.typicode.com/users')
# otvet = r.text
# otvet = json.loads(otvet)

# for i in otvet:
# 	if i['id'] == 4:
# 		print(i['address']['geo']['lng'])

# for i in otvet:
# 	if i['userId'] == 1:
# 		print(i['title'])

# print(type(otvet))
# print(r.text)

# ----post

