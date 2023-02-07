import sys
sys.path.append('..')
import insertDB
import connect_DB as Ct

student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}


if __name__ == "__main__":
    client_db = Ct.get_db_handle(1,2)
    insertDB.insert_lists(client_db["User"]["User_info"], student)
    client_db.close()