# def my_func(a, b):
# 	return (int(a) * int(b))
# a = input()
# b = input()
# c = my_func(a, b)
# print(f"The sum of a multuple {a}, {b} is ", c)

def age_acces(a):
	try:
		if int(a) >= 18:
			print('ote ber')
		else:
			print('kait uine')
	except Exception as e:
		print('San jaz')
age = input()
age_acces(age)