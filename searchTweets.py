#!/usr/bin/python

#Imports
from twitter import *
from mongodbConect import mongoConnect
import io

mongo = mongoConnect ("coletaTCC")

max_range = 0.05

#Latitude e Logitude
#Geolocation - Torre Eiffel - TE
latitude = 48.858358
longitude = 2.294647


#Credenciais Twitter API  
access_key = 'xxxx'
access_secret = 'xxxx'
consumer_key = 'xxxx'
consumer_secret = 'xxxx'

# Autenticacaoo e conexao Twitter API
twitter = Twitter(auth = OAuth(access_key, access_secret, consumer_key, consumer_secret))

while True:
	try:
		#Busca no Twitter os tweets realizados recentes na geolocalizacao determinada
		#Torre Eiffel
		search = twitter.search.tweets(geocode = "%f,%f,%fkm" % (latitude, longitude, max_range), recent_type = 'recent')
		
	#Exception
	except BaseException as e:
	 		with io.open('error.text', 'a', encoding='utf-8') as err:
	 			err.write(unicode(e))
				err.write(u"\n")
