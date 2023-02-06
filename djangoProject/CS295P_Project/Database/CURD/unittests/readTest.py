import sys
sys.path.append('..')
import readDB
import connect_DB as Ct


if __name__ == "__main__":
    client_db = Ct.get_db_handle(1,2)
    readDB.read_random_one(client_db["User"]["User_info"])
    client_db.close()