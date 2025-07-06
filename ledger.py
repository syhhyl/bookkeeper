import json
import storage
import utils

filepath = 'data.json'

def add(args_dict: dict):
	del args_dict['action'], args_dict['uitem'], args_dict['udate']
	if not utils.check_date(args_dict['date']):
		print("date invaild")
		return
	data = storage.readJson(filepath)
	data.append(args_dict)
	with open(filepath, 'w') as f:
		json.dump(data, f, indent=2)
	

def remove(it: str, date: str):
	if not utils.check_date(date):
		print("date invaild")
		return
	data = storage.readJson(filepath)
	data = [each for each in data if not \
		 	(each.get('item') == it and each.get('date') == date)]
	
	storage.writeJson(filepath, data)
				
	
def update(it: str, date: str, args_dict: dict):
	data = []	
	if not utils.check_date(date):
		print("date invaild")
		return
	
	data = storage.readJson(filepath)
	if data:
		for i in range(len(data)):
			if data[i]['item'] == it and data[i]['date'] == date:
				data[i] = args_dict		
	storage.writeJson(filepath, data)
		
def show():
	data = storage.readJson(filepath)
	min, max = utils.getMaxMin(data)
	for each in data:
		curr_a = each['amount'] 
		print(f"{each['date'][5:]:<5}: ¥{each['amount']:<6} ", end='',)
		utils.calc_show(curr_a, min, max)
	

def table():
	data = storage.readJson(filepath)
	utils.creTable(data)
	

def clean():
	storage.writeJson(filepath, [])