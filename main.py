import argparse
from ledger import add, remove, list

# parser = argparse.ArgumentParser()
# parser.add_argument("filename", type=str, help="a filepath")
# parser.add_argument("date", help="the day of work", type=int)
# args = parser.parse_args()
# print(args.filename, args.date)

def argParser() -> dict:
	parser = argparse.ArgumentParser()
	parser.add_argument("action", type=str, help="what you do")
	parser.add_argument("--item", type=str, help="thing detail")
	parser.add_argument("--amount", type=int, help="amount")
	parser.add_argument("--date", type=str, help="work date")
	parser.add_argument("--category", type=str, help="category")
	# parser.add_argument("--by", type=str, help="use for stats")
	# parser.add_argument("--to", type=str, help="use for export")

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
			
		

if __name__ == "__main__":
	main()