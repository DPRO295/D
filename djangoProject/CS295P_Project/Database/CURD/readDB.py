import pymongo
from collections import defaultdict

def read_random_one(client):
    try:
        result = client.find_one()
        if result is not None:
            print('Successfully read message with: \n', result)
    except Exception as e:
        print("\n message read fail with error: \n", e)
        return -1
    return 1

def read_exact_with_key_words(client, keywd: list, values: list):
    if len(keywd) != len(values):
        print("Please use same amount of keywords and values")
        return -1
    fd = defaultdict(None)
    for num in range(len(keywd)):
        fd[keywd[num]] = values[num]
    try:
        result = client.find_one(fd)
        if result is not None:
            print('Successfully read message with: \n', fd, '\n the result is: \n',result)
        else:
            print('Can not find the data with: ', fd)
            return 1
    except Exception as e:
        print("\n read the data fail with error: \n", e)
        return -1


