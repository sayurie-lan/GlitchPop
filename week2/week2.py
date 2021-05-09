##### TASK 1

# a = 'hello'
# print(sorted(a))
# print(type(a))

##### TASK 2

# from random import randint

# ran = randint(1, 50)
# print(ran)
# for i in range(0, 3):
# 	n = int(input())
# 	if n == ran:
# 		print("My Congratulations")
# 		break
# 	elif n > ran:
# 		print("lower")
# 	elif n < ran:
# 		print("higher")

##### TASK 3

# from random import randint

# rand = randint(1, 1000)
# print(rand)
# str_rand = str(rand)
# sum_plus = 0
# sum_mult = 1
# for i in range(len(str_rand)):
# 	sum_mult = sum_mult * int(str_rand[i])
# 	sum_plus = sum_plus + int(str_rand[i])
# print(sum_plus, " ", sum_mult)

##### TASK 4

# import requests
# import json

# link = ("https://webhook.site/be0569e0-bbbe-4f10-9b6c-3b225e831e29")
# someparams = {"name" : "Ulan", "age" : "24"}
# respG = requests.get(link, params=someparams)
# print("get ok", "Status:", respG.status_code) #status code returns os status of request where 200 is ok
# respP = requests.post(link, params=someparams, json = {"username" : "supersecret"})
# print("post ok", "Status:", respP.status_code)

##### TASK 5

# import requests
# import json

# link = ("https://webhook.site/be0569e0-bbbe-4f10-9b6c-3b225e831e29")
# jason = requests.get(link)
# print(jason.text)

##### TASK 6

import requests
import json

link = ("https://webhook.site/be0569e0-bbbe-4f10-9b6c-3b225e831e29")
jason = requests.get(link)
# jason = dict(jason) # attempt to convert it into the dictionary
jason = jason.text
jason_parsed = json.loads(jason)
summ_balance = 0
# print(jason_parsed)
# print(jason_parsed)
for i in jason_parsed:
	if i["eyeColor"] == "green":
		balance = i['balance'].replace('$','').replace(',','')
		balance = float(balance)
		summ_balance += balance
		f = open(i["name"]["first"] + ".txt", "r", "w") # сука какой нахуй integer
		friends = str(i["friends"])
		f.write(friends)
print(summ_balance)
