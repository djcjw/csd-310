from pymongo import MongoClient

## Either of the links below work

url = "mongodb+srv://admin:admin@cluster0.1dvfw.mongodb.net/pytech"

##url = "mongodb+srv://admin:admin@cluster0.1dvfw.mongodb.net/pytech?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

print ("-- pytech collection list --")

print(db.list_collection_names())

print ("\nThis is the end of program sucka, press any key to exit.. ")
