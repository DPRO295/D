import pymongo

def insert_lists(client, info):
    try:
        result = client.insert_one(info)
        if result is not None:
            print('Successfully insert.')
    except Exception as e:
        print("\n insertion fail with error: \n",e)
        return -1
    return 1
