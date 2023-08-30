from pymongo import MongoClient


class MongoAccess : 
    __USER = "root"
    __PW = "pass12345"
    __DB_NAME = "DBLP"

    
    @classmethod
    def connexion(cls):
#        cls.client = MongoClient(f"mongodb://{cls.__USER}:{cls.__PW}@127.0.0.1:27017")
        cls.client = MongoClient(f"mongodb://{cls.__USER}:{cls.__PW}@mongo-db:27017")
        cls.db = cls.client[cls.__DB_NAME]
        return cls.db


    @classmethod
    def deconnexion(cls) :
        cls.client.close()
