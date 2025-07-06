'''
check_date()
date:YYYY-MM-DD
'''
from datetime import datetime
import os
import json
def check_date(date: str) -> bool:
	# year, month, day = date.split('-') 
	# # print(datetime.now().year)
	# # print(datetime.now().month)
	# # print(datetime.now().day)
	# print(year, month, day)
	# now = datetime.now()
	# if int(year) > now.year:
	# 	return False 
	# elif int(month) > now.month:
	# 	return False
	# elif int(day) > now.day:
	# 	return False	
	# return True
	
	try:
		input_date = datetime.strptime(date, '%Y-%m-%d')
	except ValueError:
		return False
	return input_date <= datetime.now()
# check_date('2005-09-26')

def isExistFile(filepath: str):
	return os.path.exists(filepath)

def getMaxMin(data: list) -> tuple:
	max = 0
	min = 0
	for each in data:
		if min == 0: min = each['amount']
		if max == 0: max = each['amount']
		if each['amount'] > max:
			max = each['amount']
		if each['amount'] < min:
			min = each['amount']

	return min, max
				
def calc_show(curr: float, min: float, max: float):
	base = max - min
	if base == 0:
		per = 1
	else:
		per = curr / (base * 2)
	bar_len = 100
	filled_len = int(per * bar_len)
	if filled_len < 1: filled_len = 1
	bar = '█' * filled_len
	print(bar)

	

	
# calc_show(290, 780)
# calc_show(340, 780)

