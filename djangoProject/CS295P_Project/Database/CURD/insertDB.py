import pymongo
import hashlib

def insert_lists(client, info):
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

def generate_uid(name: str, account_nm: str):
    obj = hashlib.md5()
    obj.update(str(name[0]+'B10'+account_nm[0]+name[1:]+'B10'+account_nm[1:]).encode(encoding='utf-8'))
    result = obj.hexdigest()
    return str(result)
