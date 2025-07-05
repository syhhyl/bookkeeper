import json

# a = json.dumps([1, 2, 3, {'4':5, '6':7}], sort_keys=True, indent=2)
# b = json.dumps([{'action': 'eat', 'date': '2004'}, {'amount': '100', 'by': 'a'}], sort_keys=True, indent=0)
# c = json.dumps([{'who': 1, 'you': 'yes'}, [{'best': 'no', 'check': 200}]])
# log = json.dumps({'action': 'eat', 'data': '2004'})

# def test():
# 	print(a)
# 	print(type(b))
# 	print(b)
# 	print(type(json.loads(b)))
# 	print(c)
# 	print(json.loads(c))
# 	print(log)
# 	decodelog = json.loads(log)
# 	print(decodelog['action'])

# test()

import os

filepath = 'data.json'
def add(args_dict: dict):
	del args_dict['action']
	data = []
	if os.path.exists(filepath):
		with open(filepath, 'r') as f:
			try:
				data = json.load(f)
				data.append(args_dict)
			except json.JSONDecodeError:
				print("data.json is null")
				data.append(args_dict)
	with open(filepath, 'w') as f:
		json.dump(data, f, indent=2)
	
# data ={
# 	'action': 'eat',
# 	'data': '2004',
# 	'amount': '100'
# }
# data1 ={
# 	'action': 'drink',
# 	'data': '2002',
# 	'amount': '200'
# }

# add('data.json', data)

def remove(it: str, date: str):
	data = []
	if os.path.exists(filepath):
		with open(filepath, 'r+') as f:
			try:
				data = json.load(f)	
				# print(data)
				data = [each for each in data if not \
						(each.get('item') == it and each.get('date') == date)]
				# for index in range(len(data)): 
				# 	if data[index]['item'] == it and data[index]['date'] == date:
				# 		del data[index]
			except json.JSONDecodeError:
				print("data.json is null")
	with open(filepath, 'w') as f:
		json.dump(data, f, indent=2)

def list():
	data = []
	if os.path.exists(filepath):
		with open(filepath, 'r') as f:
			try:
				data = json.load(f)
				for each in data:
					print(f"[date]:{each['date']}\n[item]:{each['item']}\
		   				  \n[amount]:{each['amount']}\n[category]:{each['category']}\n")
			except json.JSONDecodeError:
				print("data.json is null")
				
	