import pprint
import pymongo
from pymongo import MongoClient

def monge_connecten(json_input)
	client = MongoClient('localhost',27017);

	cellid = json_input["cellid"]
	data_Array = json_input["dataArray"][0]

	if client.OpenTower.post.find_one({"cellid": cellid}) is None:
		post_id = client.OpenTower.post.insert_one(test_syntax) 
		post_id
		print("New cell tower added")

	else:
		client.OpenTower.post.update({"cellid":cellid},{"$push":{ "dataArray":data_Array}})
		pprint.pprint(client.OpenTower.post.find_one({"cellid": cellid }))

	print(test_syntax["dataArray"][0])
	


