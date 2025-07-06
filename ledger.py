import json
import storage

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
import utils

filepath = 'data.json'

def add(args_dict: dict):
	del args_dict['action'], args_dict['uitem'], args_dict['udate']
	if not utils.check_date(args_dict['date']):
		print("date invaild")
		return
	# if os.path.exists(filepath):
	# if utils.isExistFile(filepath):
	# 	with open(filepath, 'r') as f:
	# 		try:
	# 			data = json.load(f)
	# 			data.append(args_dict)
	# 		except json.JSONDecodeError:
	# 			print("data.json is null")
	# 			data.append(args_dict)
	data = storage.readJson(filepath)
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
	# if os.path.exists(filepath):
	if not utils.check_date(date):
		print("date invaild")
		return
	# if utils.isExistFile(filepath):
	# 	with open(filepath, 'r+') as f:
	# 		try:
	# 			data = json.load(f)	
	# 			# print(data)
	# 			data = [each for each in data if not \
	# 					(each.get('item') == it and each.get('date') == date)]
	# 			# for index in range(len(data)): 
	# 			# 	if data[index]['item'] == it and data[index]['date'] == date:
	# 			# 		del data[index]
	# 		except json.JSONDecodeError:
	# 			print("data.json is null")
	# with open(filepath, 'w') as f:
	# 	json.dump(data, f, indent=2)
	data = storage.readJson(filepath)
	data = [each for each in data if not \
		 	(each.get('item') == it and each.get('date') == date)]
	
	storage.writeJson(filepath, data)

def list():
	# if os.path.exists(filepath):
	# if utils.isExistFile(filepath):
		# with open(filepath, 'r') as f:
		# 	try:
		# 		data = json.load(f)
		# 		for each in data:
		# 			print(f"[date]:{each['date']}\n[item]:{each['item']}\
		#    				  \n[amount]:{each['amount']}\n[category]:{each['category']}")
		# 	except json.JSONDecodeError:
		# 		print("data.json is null")
	data = storage.readJson(filepath)
	for each in data:
		print(f"[date]:{each['date']}\n[item]:{each['item']}\
			  \n[amount]:{each['amount']}\n[category]:{each['category']}")
				
	
def update(it: str, date: str, args_dict: dict):
	data = []	
	if not utils.check_date(date):
		print("date invaild")
		return
	
	# if utils.isExistFile(filepath):
	# 	with open(filepath, 'r') as f:
	# 		try:
	# 			data = json.load(f)
	# 			# print(data)	
	# 			for i in range(len(data)):
	# 				if data[i]['item'] == it and data[i]['date'] == date:
	# 					data[i] = args_dict		
	# 		except json.JSONDecodeError:
	# 			print("data.json is null")	
	# with open(filepath, 'w') as f:
	# 	json.dump(data, f, indent=2)
	
	data = storage.readJson(filepath)
	if data:
		for i in range(len(data)):
			if data[i]['item'] == it and data[i]['date'] == date:
				data[i] = args_dict		
	storage.writeJson(filepath, data)
		
def show():
	#get max/min amount
	data = storage.readJson(filepath)
	min, max = utils.getMaxMin(data)
	# print(min, max)
	for each in data:
		curr_a = each['amount'] 
		print(f"{each['date'][5:]:<5}: ¥{each['amount']:<6} ", end='',)
		utils.calc_show(curr_a, min, max)
	