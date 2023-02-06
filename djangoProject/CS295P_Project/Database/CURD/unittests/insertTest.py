import sys
sys.path.append('..')
import insertDB
import connect_DB as Ct

student1 = {
    'id': 'K',
    'name': 'F',
    'age': 'C',
    'account': 'v',
    'gender': 50
}

student2 = {
    'id': 'gaga',
    'name': 'gigi',
    'age': 50,
    'account': 'lolo',
    'gender': 'm'
}


if __name__ == "__main__":
    client_db = Ct.get_db_handle(1,2)
    insertDB.insert_lists(client_db["User"]["User_info"], student1)
    insertDB.insert_lists(client_db["User"]["User_info"], student2)
    client_db.close()