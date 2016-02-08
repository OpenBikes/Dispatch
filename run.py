import datetime
from mongo.timeseries import query

city = 'Toulouse'
station = '00115 - DEMOISELLES MISTRAL'
days = 30

threshold = datetime.datetime.now() - datetime.timedelta(days=days)

df = query.station(city, station, threshold)
