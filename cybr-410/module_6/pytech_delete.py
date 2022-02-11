
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

# new student document
test_doc = {
    "student_id": "1010",
    "first_name": "John",
    "last_name": "Doe"
}

# insert the test document into MongoDB atlas 
test_doc_id = collection.insert_one(test_doc).inserted_id

# insert statements with output 
print("\n  -- INSERT STATEMENTS --")
print("  Inserted student record into the students collection with document_id " + str(test_doc_id))

# call the find_one() method by student_id 1010
student_test_doc = collection.find_one({"student_id": "1010"})

# display the results 
print("\n  -- DISPLAYING STUDENT TEST DOC -- ")
print("  Student ID: " + student_test_doc["student_id"] + "\n  First Name: " + student_test_doc["first_name"] + "\n  Last Name: " + student_test_doc["last_name"] + "\n")

# call the delete_one method to remove the student_test_doc
deleted_student_test_doc = collection.delete_one({"student_id": "1010"})

# find all students in the collection 
new_student_list = collection.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY AFTER DELETING STUDENT TEST DOC --")

# loop over the collection and output the results 
for doc in new_student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")
