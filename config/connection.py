from pymongo import MongoClient

host = 'localhost'
port = '27017'

class Connection:
    
    def __init__(self, database):
        self.client = MongoClient(f'mongodb://{host}:{port}')
        self.db = self.client[database]

        
    def get_all(self, collection):
        collect = self.db[collection]
        return collect.find()

    def get_all_by(self, collection, condition = {}):
        collect = self.db[collection]
        return collect.find(condition)
    
    def get_one(self, collection, condition={}):
        collect = self.db[collection]
        return collect.find_one(condition)
    
    def insert(self, collection, data):
        collect = self.db[collection]
        result = collect.insert_one(data)
        print(f'Insert ID -> {result.inserted_id}')
    
    def insert_many(self, collection, data):
        collect = self.db[collection]
        result = collect.insert_many(data)
        print(f'Insert IDs -> {result.inserted_ids}')

    def update(self, collection, condition, change):
        collect = self.db[collection]
        collect.update_one(condition, {
            '$set': change
        })
        print('Updated Document')

    def update_many(self, collection, condition, change):
        collect = self.db[collection]
        result = collect.update_many(condition, {
            '$set': change
        })
        print(f'Updated Document -> {result.raw_result} - Match {result.matched_count}')

    def delete(self, collection, condition):
        collect = self.db[collection]
        collect.delete_one(condition)
        print(f'Delete Document')

    def delete_many(self, collection, condition):
        collect = self.db[collection]
        result = collect.delete_many(condition)
        print(f'Delete Documents -> {result.deleted_count}')