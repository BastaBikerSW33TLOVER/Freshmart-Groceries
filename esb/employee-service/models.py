from pymongo import MongoClient
from bson.objectid import ObjectId
from config import Config

client = MongoClient(Config.MONGO_URI)
db = client.get_database()

class PersonalInfo:
    def __init__(self, name, date_of_birth, contact_number, emergency_contact_number):
        self.name = name
        self.date_of_birth = date_of_birth
        self.contact_number = contact_number
        self.emergency_contact_number = emergency_contact_number

    def save(self):
        personal_info_data = {
            "name": self.name,
            "date_of_birth": self.date_of_birth,
            "contact_number": self.contact_number,
            "emergency_contact_number": self.emergency_contact_number
        }
        result = db.personal_info.insert_one(personal_info_data)
        return str(result.inserted_id)

    @staticmethod
    def get_all():
        return list(db.personal_info.find())

    @staticmethod
    def get_by_id(info_id):
        return db.personal_info.find_one({"_id": ObjectId(info_id)})

