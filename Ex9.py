# Interesting-Code
import pymongo


# Config MongoDB


uri = "mongodb://admin:admin@ds119598.mlab.com:19598/cafeteria"


client = pymongo.MongoClient(uri)


db = client.get_default_database()


# Get MENU collection


menu_items = db["order"].find()


menu_items_length = db["order"].count()
menu = db["menu"].find()
menu_length = db["menu"].count()
##for i in menu_items:
##    for key,value in i.items():
##        if key != "_id":
##            print("{0}: {1}".format(key,value),end=" , ")
##    print()


bill= {
        "Pizza" : 0,
        "hambuger":0,
        "Salad":0,
        "Taco" :0
        }
bill_list= {
    "Huy be": 0,
    "Ha": 0,
    "Huy big": 0
    }

Total=0
n = 0

for i in range(menu_length):
    bill[menu[i]["name"]] = menu[i]["price"]


print(bill)

for i in menu_items:
   for j in i["order"]:        
        Total +=  bill[j]
        bill_list[i["customer"]] += bill[j]
        
        
print(bill_list)
print("Total:",Total)

