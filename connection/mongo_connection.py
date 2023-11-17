from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from exception.mongo_exception import MongoException
from logging import fatal
URL = "mongodb+srv://admin:iesjandula@huelgadb.lboe9th.mongodb.net/?retryWrites=true&w=majority"
class MongoConnection:
    def __init__(self,databaseName:str,collectionName:str) -> None:
        """Constructor que crea los atributos de la conexion"""
        self.databaseName = databaseName
        self.collectionName = collectionName
        self.client = None
        self.database = None
        self.collection = None
    def connection(self) -> MongoClient | Database | Collection:
        """Metodo que conecta con la base de datos de mongodb Atlas\n
        Returns:\n 
        Cliente que contacta con atlas\n
        Base de datos con la que se trabaja\n
        Coleccion con la que se trabaja"""
        try:
            self.client = MongoClient(URL)
            self.database = self.client[self.databaseName]
            self.collection = self.database[self.collectionName]
        except Exception:
            fatal("Error al conectar con la base de datos")
            
        return self.client,self.database,self.collection
    
    def closeConnection(self):
        self.client.close()
        
