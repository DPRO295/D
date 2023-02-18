import pymongo
from pymongo import MongoClient
import certifi


def get_db_handle(dbname=None, dbpw=None):
    ca = certifi.where()
    client = pymongo.MongoClient(
        'mongodb+srv://Dpropro:Dpropro@dpro.qls8nuc.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
    print("Connection Successful... Please remember to close the connection")
    return client

def check_collection_exist(client, place):
    try:
        place_sp = place.split(".")
        if len(place_sp) > 2 or len(place_sp) == 0:
            print("Please use a valid input format")
            return -1
        collist = client.list_database_names()
        if place_sp[0] not in list(collist):
            print("The Database not exist, please check the database first!")
            return -1
        collist = client.list_collection_names()
        if place_sp[1] not in list(collist):
            print("The Collection not exist, please check the database first!")
            return -1
        print("The database and the collections is work! ")
        return 1
    except Exception as e:
        print("\n Check fail with error: \n",e)
        return -1
    return 1

