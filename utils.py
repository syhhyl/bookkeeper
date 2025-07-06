'''
check_date()
date:YYYY-MM-DD
'''
from datetime import datetime
import os
from rich.table import Table
from rich.console import Console
def check_date(date: str) -> bool:
	try:
		if not date: date = ''
		input_date = datetime.strptime(date, '%Y-%m-%d')
	except ValueError:
		return False
	return input_date <= datetime.now()

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
	base = (max - min) * 10
	if base == 0:
		per = 1
	else:
		per = curr / base
	bar_len = 60
	filled_len = int(per * bar_len)
	# print(f"filled_len:{filled_len}")
	if filled_len < 1: filled_len = 1
	bar = '█' * filled_len
	print(bar)



def creTable(data: list):
	console = Console()
	table = Table(show_header=True, header_style="bold magenta")
	table.add_column("date", style="dim")
	table.add_column("item", style="dim")
	table.add_column("amount", style="dim")
	table.add_column("category", style="dim")

	for each in data:
		table.add_row(
			each['date'],
			each['item'],
			str(each['amount']),
			each['category']
		)
	console.print(table)
	
	
		
