from pymongo import MongoClient

## Either of the links below work

url = "mongodb+srv://admin:admin@cluster0.1dvfw.mongodb.net/pytech"

##url = "mongodb+srv://admin:admin@cluster0.1dvfw.mongodb.net/pytech?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

# Creating Dictionary of student records to be inserted
rec1 = { 
          "first_name": "Chris",
          "last_name": "Ward",
          "student_id": "1007"}

rec2 = { 
          "first_name": "Deb",
          "last_name": "Lynne",
          "student_id": "1008"}

rec3 = {
          "first_name": "Harrison",
          "last_name": "Garrett",
          "student_id": "1009"}

# Created or Switched to "students" collection 
students = db["students"]

# insert statements with output
print("\n  -- INSERT STATEMENTS --")
rec1 = students.insert_one(rec1).inserted_id
print("  Inserted student record Chris Ward into the students collection with document_id: " + str(rec1))

rec2 = students.insert_one(rec2).inserted_id
print("  Inserted student record Deb Lynne into the students collection with document_id: " + str(rec2))

rec3 = students.insert_one(rec3).inserted_id
print("  Inserted student record Harrison Garrett into the students collection with document_id: " + str(rec3))

# returning the name of the collections under pytech
print ("\n-- pytech collection list --")
print(db.list_collection_names())

# ending the program with grace (-;
print ("\nThis is the end of program sucka, press any key to exit.. ")

input("\n\n  End of program, press any key to exit... ")

