```Download the mongoDB command to your computer
For windows: "https://downloads.mongodb.com/compass/mongosh-1.6.2-win32-x64.zip"
· Add <your mongosh's download directory>/bin to your $PATH variable.
· On your terminal, use command “mongosh "mongodb+srv://dpro.qls8nuc.mongodb.net/myFirstDatabase" --apiVersion 1 --username Dpropro”
· Password is: Dpropro
```

In order to use the APIs, first run:
`client = connect_DB.get_db_handle(),`
this will let you got a mongo DB client connection,
then put this client into any APIs you want.
For example, if you want to insert a user data, try:
`insert_new_account(client, info: Json format)`

# CURD APIs: #
### ~pip install djongo~
### ~pip install pymongo==3.12.3~
### ~double click and install the "lets=encrypt-r3" file~
## connect ##
```angular2html
get_db_handle() # Will return a client and it can work in other APIs
```
```angular2html
check_collection_exist(client, place) # Use to check whether the collection or database
                                      # exists, in format:
                                      # place = "User.User_type"
```
## insert ##
```angular2html
insert_new_account(client, info) # provide a connect client and the user_info
                                 # User_info need name and account part
```
```angular2html
insert_any_one(client, place, info) # the place is the path, in format:
                                    # place = "User.User_type"
```
## update ##


## delete ##


## read ##




