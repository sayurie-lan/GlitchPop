############ TASK 1

# print('Kol-vo liudei')
# k = int(input())
# print('Kol-vo yablok')
# n = int(input())
# c = n / k
# print(int(c))
# print(n % k)

############ TASK 2

# a = int(input())
# b = int(input())
# c = int(input())

# if a % 2 == 1:
# 	a += 1
# if b % 2 == 1:
# 	b += 1
# if c % 2 == 1:
# 	c += 1

# summ = a + b + c

# print(f'we need {int(summ / 2)} desks')

############ TASK 3

# a = int(input())
# b = int(input())
# c = int(input())
# if a == b and a == c:
# 	print('3')
# elif a == b or a == c: # Здесь я поставил elif в место if и он заработал я хз почему
# 	print('2')
# else:
# 	print('0')

############ TASK 4

# a = []
# n = int(input())
# counter = 0
# for i in range(n):  
#     new_element = int(input())
#     a.append(new_element)
#     if new_element == 0:
#     	counter += 1
# print(counter)

############ TASK 5

# f = open('hello.txt', 'w')
# for i in range(0, 100):
# 	f.write('I am a programmer\n')

############ TASK 6

# with open('test.txt', 'r') as f:
# 	f = f.read()
# 	f = f.split()
# 	print(f)

f = open('teamname.txt', 'r', encoding = 'utf-8')
f = f.read()
f = f.split()
counter1 = 0
counter2 = 0
for i in range(0, len(f)):
	if f[i] == 'ElonMars':
		counter1 = int(counter1) + 1
		counter2 = int(counter2) + 1
	elif f[i].upper() == 'ELONMARS':
		counter2 = int(counter2) + 1
print(counter1, " ",counter2)