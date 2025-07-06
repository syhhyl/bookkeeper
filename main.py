import argparse
from ledger import *
import utils

def argParser() -> dict:
	parser = argparse.ArgumentParser()
	parser.add_argument("action", type=str, help="what you do")
	parser.add_argument("--item", type=str, help="thing detail")
	parser.add_argument("--amount", type=int, help="amount")
	parser.add_argument("--date", type=str, help="work date")
	parser.add_argument("--category", type=str, help="category")
	parser.add_argument("--uitem", type=str, help="use with update")
	parser.add_argument("--udate", type=str, help="use with date")

	args = vars(parser.parse_args())
	for pair in args:
		if pair[1] == None:
			args[pair[0]] = ''	
	return args


def main():
	args_dict = argParser()	
	match args_dict['action']:
		case 'add':
			add(args_dict)
		case 'remove':
			remove(args_dict['item'], args_dict['date'])
		case 'list':
			list()
		case 'update':
			update(args_dict['uitem'], args_dict['udate'], args_dict)
		case 'show':
			show()	
		case 'table':
			table()

if __name__ == "__main__":
	main()