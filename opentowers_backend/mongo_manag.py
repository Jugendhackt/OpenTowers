import pprint
import pymongo
import triangulation
from pymongo import MongoClient

client = MongoClient('localhost',27017)


def monge_connecten(json_input):
	"""Take JSON-Input and writes to mongo-database."""
	cellid = json_input["cellid"]
	data_Array = json_input["dataArray"][0]

	if client.OpenTower.post.find_one({"cellid": cellid}) is None:
		post_id = client.OpenTower.post.insert_one(json_input)
		post_id
		print("New cell tower added")
	else:
		client.OpenTower.post.update({"cellid":cellid},{"$push":{ "dataArray":data_Array}})

		#pprint.pprint(client.OpenTower.post.find_one({"cellid": cellid }))

	if client.OpenTower.post.find_one({"cellid":cellid, "dataArray.2":{"$exists":True}}) is None:
		print("Not enought towers for triangulation")
	else:
		print("Triangulating new position")
		calc_location = pars_triangulation(client.OpenTower.post.find_one({"cellid":cellid}))
		client.OpenTower.post.update({"cellid":cellid},{"$set":{"calc_Position":{"long":calc_location[1],"lati":calc_location[0]}}})


def pars_triangulation(array_input):
	"""Transform from JSON to List for triangulation.py."""
	long_g = []
	lati_g = []
	signal_Str = []

	for i in range(len(array_input["dataArray"])):
		long_g.append(array_input["dataArray"][i]["location"]["long"])
		lati_g.append(array_input["dataArray"][i]["location"]["lati"])
		signal_Str.append(array_input["dataArray"][i]["signal_Strength"])

	return triangulation.triangulater(lati_g, long_g, signal_Str)


def gps(gps_location):
    """Search for nearby towers in mongo-database."""
    gps_location = gps_location.split()
    # The 1 is not calibrated, imaginary value!!! Test in real-life :)
    gps_location_lat = [float(gps_location[0])-1, float(gps_location[0])+1]
    gps_location_lng = [float(gps_location[1])-1, float(gps_location[1])+1]
    print(gps_location_lat)
    print(gps_location_lng)
    towers = list(client.OpenTower.post.find({"$and":[{"$and":[{"calc_Position.long":{"$lte":gps_location_lng[1]}},{"calc_Position.long":{"$gte":gps_location_lng[0]}}]},{"$and":[{"calc_Position.lati":{"$lte":gps_location_lat[1]}},{"calc_Position.lati":{"$gte":gps_location_lat[0]}}]}]}))
    for tower in towers:
        tower["_id"] = None
    return towers
