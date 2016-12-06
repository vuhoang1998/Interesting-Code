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


price= {}
bill_list= {}

Total=0
n = 0

for i in range(menu_length):
    price[menu[i]["name"]] = menu[i]["price"]

print(price)

for i in menu_items:
       bill_list[i["customer"]] =0
       n = 0
       for j in i["order"]:
            j = j.capitalize()
            Total +=  price[j]
            bill_list[i["customer"]] += price[j]
           

print(bill_list)
print("Total:",Total)

