import pymongo
import hashlib

def insert_new_account(client, info):
    try:
        if 'name' not in info or 'account' not in info:
            print("User should provide their name and account_number")
            return -1
        unic = generate_uid(info['name'], info['account'])
        info['uid_gn'] = unic
        result = client.insert_one(info)
        if result is not None:
            print('Successfully insert.')
    except Exception as e:
        print("\n insertion fail with error: \n",e)
        return -1
    return 1

def insert_any_one(client, place, info):
    try:
        serve = client
        for each_item in place.split("."):
            serve = serve[each_item]
        result = serve.insert_one(info)
        if result is not None:
            print('Successfully insert.')
    except Exception as e:
        print("\n insertion fail with error: \n",e)
        return -1
    return 1

def generate_uid(name: str, account_nm: str):
    obj = hashlib.md5()
    obj.update(str(name[0]+'B10'+account_nm[0]+name[1:]+'B10'+account_nm[1:]).encode(encoding='utf-8'))
    result = obj.hexdigest()
    return str(result)
