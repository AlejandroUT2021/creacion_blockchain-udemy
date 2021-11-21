# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 01:58:50 2021

@author: Alejandro
"""

#Modulo 1: Crear una cadena de bloques (Blockchain)


#Para instalar:
    #Flask==0.12.2: pip install Flask==0.12.2
    #Cliente HTTP Postman: https://www.getpostman.com 
    
    
# Importar las librerías
import datetime
import hashlib           
import json   
from flask import Flask, jsonify
#es la forma más rapida de enviar los datos

#Parte 1 - Crear la cadena de bloques----
#mentalidad de desarrollador, estructurar a través de clases
class Blockchain:

    def __init__(self):
        self.chain = []
        self.create_block(proof =1, previous_hash= '0')
        
    def create_block(self, proof, previous_hash):
        block = {'index'  : len(self.chain)+1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash' : previous_hash }
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        return self.chain(-1)
    
    def proof_of_work(self, previous_proof):
        new_proof =1
        check_proof =False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4]=='0000':
                check_proof=True
            else:
                new_proof += 1
        return new_proof
            
    
#Parte 2 - Minado de un bloque de la cadena --------

































