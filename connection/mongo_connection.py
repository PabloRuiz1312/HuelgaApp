from pymongo import MongoClient
from exception.mongo_exception import MongoException
from logging import fatal
URL = "mongodb+srv://admin:iesjandula@huelgadb.lboe9th.mongodb.net/?retryWrites=true&w=majority"
class MongoConnection:
    def connection(databaseName:str,collectionName:str):
        client = None
        database = None
        collection = None
        try:
            client = MongoClient(URL)
            database = client[databaseName]
            collection = database[collectionName]
        except MongoException:
            fatal("Error al conectar con la base de datos")
            
        return client,database,collection
        
