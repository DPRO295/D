import pymongo
from pymongo import MongoClient
import certifi


def get_db_handle(DBname, DBpw):
    ca = certifi.where()
    client = pymongo.MongoClient(
        'mongodb+srv://Dpropro:Dpropro@dpro.qls8nuc.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
    print("Connection Successful... Please remember to close the connection")
    return client


