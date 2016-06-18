import requests;
from Src.MyParser import MyParser
from Src.config.configParser import readConfig
from pymongo import MongoClient

protocol = readConfig("main","protocol")
domain = readConfig("main", "domain")
mongoHost = readConfig("DataBase", "host")
mongoPort = readConfig("DataBase", "port")

parser = MyParser()
if mongoHost != None:
  conn = MongoClient("mongodb://" + mongoHost + ":" + mongoPort)
else:
  conn = MongoClient()

db = conn.evescrape
dbdata = db.data

url = protocol + "://" + domain + "/"
res = requests.get(url);

parser.feed(res.text)

print(parser.links)
print()
print(parser.metaData)
print()
print(parser.pageTitle)

'''
TODO and other notes to self
  the documents produces by the crawler can be stored in collections by Domain
  urls should be built out of protocol - subdomain - domain -topleveldomain - path - fragment

'''