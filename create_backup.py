from datetime import date
import pymongo as c

def add():
    file = open("Backup.txt", "w+")
    temp = ""
    for l in collections.find({}):
        temp += str(l)
    file.write(temp)
    file.close()

db_client = c.MongoClient("mongodb://localhost:27017/")
current_db = db_client["Accounting"]
collections = current_db["Graphic_Interface"]


today = date.today()
day = today.strftime("%B.%D.%Y")