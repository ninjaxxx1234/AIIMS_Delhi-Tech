import datetime

from pymongo import MongoClient

client = MongoClient('mongodb+srv://xabcd9172:xabcd9172@cluster0.euudrlp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

def db_data(rr, vte, peep, pip, fio2, sp, tinsp):
    db = client['data']
    collection = db['parameters']
    timestamp=datetime.datetime.now()
    document = {'timestamp':timestamp, 'rr' : rr, 'vte' : vte, 'peep' : peep, 'pip' : pip, 'fio2' : fio2, 'sp' : sp, 'tinsp': tinsp }
    inserted_document = collection.insert_one(document)



