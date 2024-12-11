from mongita import MongitaClientDisk # type: ignore
from bson.objectid import ObjectId # type: ignore

client = MongitaClientDisk()
db = client.accommodation_db

# Accommodation CRUD Operations
def retrieve_accommodations():
    collection = db.accommodation_collection
    accommodations = list(collection.find())
    for a in accommodations:
        a["id"] = str(a["_id"])
        del a["_id"]
    return accommodations

def retrieve_accommodation(accommodation_id):
    collection = db.accommodation_collection
    accommodation = collection.find_one({"_id": ObjectId(accommodation_id)})
    accommodation["id"] = str(accommodation["_id"])
    del accommodation["_id"]
    return accommodation

def create_accommodation(data):
    collection = db.accommodation_collection
    collection.insert_one(data)

def update_accommodation(accommodation_id, data):
    collection = db.accommodation_collection
    collection.update_one({"_id": ObjectId(accommodation_id)}, {"$set": data})

def delete_accommodation(accommodation_id):
    collection = db.accommodation_collection
    collection.delete_one({"_id": ObjectId(accommodation_id)})

# Review CRUD Operations
def retrieve_reviews_by_accommodation(accommodation_id):
    collection = db.review_collection
    reviews = list(collection.find({"accommodation_id": ObjectId(accommodation_id)}))
    for review in reviews:
        review["id"] = str(review["_id"])
        del review["_id"]
    return reviews

def create_review(data):
    collection = db.review_collection
    data["accommodation_id"] = ObjectId(data["accommodation_id"])
    collection.insert_one(data)
