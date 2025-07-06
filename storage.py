import json
import utils 

def readJson(filepath: str) -> list:
	data = []
	if utils.isExistFile(filepath):
		with open(filepath, 'r') as f:
			try:
				data = json.load(f)
			except json.JSONDecodeError:
				# print("")
				pass
	return data	
		

def writeJson(filepath: str, data: list):
	if utils.isExistFile(filepath):
		with open(filepath, 'w') as f:
			json.dump(data, f, indent=2)