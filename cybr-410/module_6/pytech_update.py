
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

# update student_id 1007 last_name
result = collection.update_one({"student_id": "1007"}, {"$set": {"last_name": "Mac-Dad III"}})

# find document by student_id
chris = collection.find_one({"student_id": "1007"})

# output the results 
print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 AFTER UPDATING LAST NAME --")
print("  Student ID: " + chris["student_id"] + "\n  First Name: " + chris["first_name"] + "\n  Last Name: " + chris["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to exit... ")