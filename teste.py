# postgresql
# import psycopg2

# con = psycopg2.connect(
#     host="localhost",
#     database="nomeDB",
#     user="user",
#     password="password")

# cur = con.cursor()

# cur.execute("select id, name from employees")

# rows = cur.fetchall()
# for r in rows:
#     print(f"id {r[0]} name {r[1]}")

# con.close()

# mongoDB
import pymongo

connection = pymongo.MongoClient('localhost', 27017)
database = connection['archtimer']
collection = database['clients']

data = {'Name': 'SM_Cristal'}

collection.insert_one(data)

connection.close()
