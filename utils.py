'''
check_date()
date:YYYY-MM-DD
'''
from datetime import datetime
def check_date(date: str) -> bool:
	year, month, day = date.split('-') 
	# print(datetime.now().year)
	# print(datetime.now().month)
	# print(datetime.now().day)
	now = datetime.now()
	if int(year) > now.year:
		return False 
	elif int(month) > now.month:
		return False
	elif int(day) > now.day:
		return False	
	return True
check_date('2005-09-26')
