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


any_info = {
	"tr_info": {
		" description": "type",
		"type": " string",
		"tr_type": [{
			" description": "type1",
			"type": " string"
		}, {
			" description": "type2",
			"type": " string"
		}]
	}
}


if __name__ == "__main__":
    client_db = Ct.get_db_handle(1,2)
    insertDB.check_collection_exist(client_db,'User.any_info')
    # insertDB.insert_new_account(client_db["User"]["User_info"], student1)
    # insertDB.insert_new_account(client_db["User"]["User_info"], student2)
    # insertDB.insert_any_one(client_db, 'User.any_info', any_info)
    client_db.close()