from pymongo import MongoClient
import os

db_hostname = 't2mdb.eastus.cloudapp.azure.com'
db_port = os.getenv('DB_PORT')
conn = MongoClient(db_hostname, db_port)

db_name = conn.Prueba_Tier2
