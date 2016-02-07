from pymongo import MongoClient
import datetime
import pandas as pd

city = 'Toulouse'
station = '00115 - DEMOISELLES MISTRAL'
days = 7 

client = MongoClient()
db = client.OpenBikes
collection = db[city]

threshold = datetime.datetime.now() - datetime.timedelta(days=days)
pattern = threshold.isoformat()

cursor = collection.find({'_id': {'$gte': pattern}, 'u.n': station},
                         {'u': {'$elemMatch': {'n': station}}})
df = pd.DataFrame(list(cursor))