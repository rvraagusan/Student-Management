from pymongo import MongoClient
from pymongo.errors import PyMongoError

# client = MongoClient(port=27017)
# db = client.STUDENTMDB

# collections = db['STUDENT']

# collections.insert_one({"St_id": "21425454", "Name":"Ragul","Email":"ravi@gmail.com","Grade" :"11", "Stream":"Maths"})

class Database(object):
    _instance = None
    database_error_msg = ' error raised in db ,'

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        
        return cls._instance

    def __init__(self):
        try:
            self.client = MongoClient("mongodb://localhost:27017")
            self.db = self.client['STUDENTMDB']
        
        except PyMongoError as e:
            raise
            print(e)
    
    def insert_data(self, insert_collection, inserted_data):
        res=[]
        try:
            db_collection = self.db[f'{insert_collection}']
            db_collection.insert_one(inserted_data)

        except PyMongoError:
            return {'message':self.database_error_msg}

        else:
            return {'message': 'Successfully insert a response'}    

if __name__ == "__main__":
    db = Database()
#     data = {
#         "St_id": "21425456", 
#         "Name":"ravi ram",
#         "Email":"raja@gmail.com",
#         "Grade" :"12", 
#         "Stream":"Bio"
#         }
#     db.insert_data('STUDENT', data)
    
