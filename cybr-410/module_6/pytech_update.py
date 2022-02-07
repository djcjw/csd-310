from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.1dvfw.mongodb.net/pytech"

client = MongoClient(url)

db = client.pytech

print ("-- pytech collection list --")

print(db.list_collection_names())

# Created or Switched to "students" collection 
collection = db["students"]
  
# find all students in the collection 
student_list = collection.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# find document by student_id
deb = collection.find_one({"student_id": "1008"})

# output the results 
print("\n  -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("  Student ID: " + deb["student_id"] + "\n  First Name: " + deb["first_name"] + "\n  Last Name: " + deb["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to exit... ")

# find method below works

# Creating Dictionary of 3 student records to be inserted
records = [
        {"first_name":"Chris", "last_name":"Ward", "student_id":"1007"},
        {"first_name":"Deb", "last_name":"Lynne", "student_id":"1008"},
        {"first_name":"Harrison", "last_name":"Garrett", "student_id":"1008"},
    ]

# Inserting multiple records in the collection by using collection.insert_many()
collection.insert_many(records)

#for x in collection.find():
  
    #print(x)

for x in collection.find({}, {"_id":1, "first_name": 1, "last_name": 1, "student_id": 1 }):
    print(x)

# insert statements with output 
print("\n  -- INSERT STATEMENTS --")
for id1 in collection.find({}, {" _id":1}):
    print(id1)




print ("\nThis is the end of program suckatash, press any key to exit.. ")
input("\n\n  End of program, press any key to exit... ")


