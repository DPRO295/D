import sys
sys.path.append('..')
import readDB
import connect_DB as Ct


if __name__ == "__main__":
    client_db = Ct.get_db_handle(1,2)
    testinfo = client_db["User"]["User_info"]
    readDB.read_all_info(testinfo)
    # readDB.read_exact_with_key_words(testinfo,['name'],['Jordan'])
    client_db.close()