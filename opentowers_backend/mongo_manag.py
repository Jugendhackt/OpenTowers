import pprint
import pymongo
import triangulation 
from pymongo import MongoClient

def monge_connecten(json_input):
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
	client = MongoClient('localhost',27017);

	cellid = json_input["cellid"]
	data_Array = json_input["dataArray"][0]

	if client.OpenTower.post.find_one({"cellid": cellid}) is None:
		post_id = client.OpenTower.post.insert_one(json_input)
		post_id
		print("New cell tower added")
	else:
		client.OpenTower.post.update({"cellid":cellid},{"$push":{ "dataArray":data_Array}})
<<<<<<< Updated upstream
		pprint.pprint(client.OpenTower.post.find_one({"cellid": cellid }))
		print("JSON: ", json_input)
	print(json_input["dataArray"][0])
=======
		#pprint.pprint(client.OpenTower.post.find_one({"cellid": cellid }))

	if client.OpenTower.post.find_one({"cellid":cellid, "dataArray.2":{"$exists":True}}) is None:
		print("Not enought towers for triangulation")
	else:
		print("Triangulating new position")	
		calc_location = pars_triangulation(client.OpenTower.post.find_one({"cellid":cellid}))
		client.OpenTower.post.update({"cellid":cellid},{"$set":{"calc_Position":{"long":calc_location[1],"lati":calc_location[0]}}})	
		

def pars_triangulation(array_input):

	long_g = []
	lati_g = []
	signal_Str = []

	for i in range(len(array_input["dataArray"])):
		long_g.append(array_input["dataArray"][i]["location"]["long"])
		lati_g.append(array_input["dataArray"][i]["location"]["lati"])
		signal_Str.append(array_input["dataArray"][i]["signal_Strength"])

	return triangulation.triangulater(lati_g, long_g, signal_Str)
	
>>>>>>> Stashed changes
