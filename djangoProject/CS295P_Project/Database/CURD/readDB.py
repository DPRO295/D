import pymongo
import numpy

def read_random_one(client):
    try:
        result = client.find_one()
        if result is not None:
            print('Successfully read message with: \n', result)
    except Exception as e:
        print("\n message read fail with error: \n", e)
        return -1
    return 1

def read_exact_with_name(client, user_name):
    try:
        result = client.find_one()
        if result is not None:
            print('Successfully read message with: \n', result)
    except Exception as e:
        print("\n message read fail with error: \n", e)
        return -1
    return 1

