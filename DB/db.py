from pymongo import MongoClient
from pymongo.errors import PyMongoError
from bson.json_util import dumps

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

    def get_data(self, get_collection, search_id=None):
        data=[]
        if search_id == None:
            try:
                db_collection = self.db[f'{get_collection}']
                users = db_collection.find(projection= {'_id':False})
                data  = [ user for user in users]
                return { 'request':{'message': 'All records received'}, 'response':data}
            except PyMongoError:
                return {'message':self.database_error_msg}
        else:
            try:
                db_collection = self.db[f'{get_collection}']
                data = db_collection.find_one(filter={'St_id':search_id}, projection= {'_id':False})
                return { 'request':{'message': 'record received', 'Search Id':f'{search_id}'}, 'response':data}
            except PyMongoError:
                return {'message':self.database_error_msg}

    def detele_data(self, del_collections, search_id):
        try:
            db_collection = self.db[f'{del_collections}']
            db_collection.delete_one({'St_id': search_id})
        except PyMongoError:
            return {'message':self.database_error_msg}
        else:
            return {'message': 'Successfully remove the user'}

    def update_data(self, up_collections, search_id, updated_value):
        try:
            db_collection = self.db[f'{up_collections}']
            db_collection.update_one({'St_id':search_id},{"$set":updated_value})
        except PyMongoError:
            return {'request': {'message':self.database_error_msg}}
        else:
            return {'request':{'message':'Successfully update the response', 'updated':updated_value}}

    def course_lookup_db(self, code):
        resp=[]
        pipeline = [
            {'$match': {'Course_code': code}}
            ]
        
        results = self.db['TEACHER'].aggregate(pipeline)
        for result in results:
            data = {'Name' : result['Name'], 'Subject': result['Subject']}
            resp.append(data)
        return resp


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
    
