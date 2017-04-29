# -*- coding: utf-8 -*-

#import pandas as pd
from pymongo import MongoClient


class mongoConnect:    
    
    #atributos da classe    
    connect = None    
    
    #construtor da classe que se conecta ao banco
    def __init__(self, db,host='localhost', port=27017, username=None, password=None):
        self.connect = self._connect_mongo(db=db, host=host, port=port, username=username, password=password)
    
    #Conexao com o banco
    def _connect_mongo(self, db,host='localhost', port=27017, username=None, password=None):
        """ A util for making a connection to mongo """
    
        if username and password:
            mongo_uri = 'mongodb://%s:%s@%s:%s/%s' % (self.username, self.password, self.host, self.port, self.db)
            conn = MongoClient(mongo_uri)
        else:
            conn = MongoClient(host, port)
    
        #retorna a conexão
        return conn[db]
    
    #retorna o dataframe do pandas    
  
    #insere o documento no mongodb, recebendo como parametro o arquivo a ser inserido e o nome da colecao
    def insert_document(self, data, collection):
       result = self.connect[collection].insert_one(data)
        
       return result.inserted_id
