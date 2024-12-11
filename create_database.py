from mongita import MongitaClientDisk # type: ignore

client = MongitaClientDisk()
db = client.accommodation_db

def create_database():
    db.drop_collection("accommodation_collection")
    accommodation_collection = db.accommodation_collection
    accommodation_collection.insert_many([
        {"name": "The Tree House", "location": "Ohio", "price": 250.0, "amenities": ["Security", "Parking", "Swimming Pool", "Garden Area", "Roof Top"]},
        {"name": "Historic Homestead", "location": "Kent", "price": 300.0, "amenities": ["Outdoor Space", "Fire Place", "Back Yard", "Wifi"]},
        {"name": "The Luxury Villa", "location": "Cleveland", "price": 350.0, "amenities": ["Fitness Center", "Fire Place", "In-unit Laundry", "Wifi"]}
    ])

    db.drop_collection("review_collection")
    review_collection = db.review_collection

    print("Database created successfully.")

if __name__ == "__main__":
    create_database()
