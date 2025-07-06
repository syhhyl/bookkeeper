import json
import utils 

def readJson(filepath: str) -> list:
	data = []
	if utils.isExistFile(filepath):
		with open(filepath, 'r') as f:
			try:
				data = json.load(f)
				# print("load config success")
			except json.JSONDecodeError:
				print("")
	return data	
		

def writeJson(filepath: str, data: list):
	if utils.isExistFile(filepath):
		with open(filepath, 'w') as f:
			json.dump(data, f, indent=2)