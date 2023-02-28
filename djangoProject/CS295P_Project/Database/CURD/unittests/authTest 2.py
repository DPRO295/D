import sys
sys.path.append('..')
import auth
import connect_DB as Ct

if __name__ == "__main__":
    client_db = Ct.get_db_handle()
    user_obj = auth.authenticate(client=client_db,
                                 request=None,
                                 username="TestUserLogin",
                                 password="abcdefg")
    if user_obj is None:
        print("The User Not exist and can not login.")
    else:
        print(user_obj)
        print(user_obj.username)

    uid = auth.create_user(client_db,
                           username="TestUserLogin",
                           password="abcdefg",
                           email=None)
    print(uid, "is created succesfully!")

    user_obj = auth.authenticate(client=client_db,
                                 request=None,
                                 username="TestUserLogin",
                                 password="abcdefg")
    if user_obj is None:
        print("The User Not exist and can not login.")
    else:
        print(user_obj)

