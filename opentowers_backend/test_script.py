import pprint
import  pymongo
import random
from pymongo import MongoClient
import mongo_manag


for i in range(200):
	long_g = random.uniform(-180,180.0)
	lati_g = random.uniform(-90,90.0)
	cellid_g = random.randint(0,300)
	for j in range(4):
		long_g_in= random.uniform((long_g-0.01),(long_g+0.01))
		lati_g_in = random.uniform((lati_g-0.01),(lati_g+0.01))
		signal_Str = random.randint(-120,0)
		pars_json = {"cellid":cellid_g, "dataArray":[{"signal_Strength":signal_Str, "location":{"long":long_g_in,"lati":lati_g_in}}]}
	#print(pars_json)
		mongo_manag.monge_connecten(pars_json)

