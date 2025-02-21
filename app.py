from flask import Flask, request, abort
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json
from dotenv import load_dotenv
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST' :
        print (request.json)
        return 'success', 200
    else:
        abort
@app.route('/mongodb')
def mongodb():
    load_dotenv()
    uri = os.getenv('mongodburl')
# Create a new client and connect to the server
    mongodbclient = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
    mongodbclient.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    return "success"
@app.route('/')
def rootfunction():
    with open('samplepayload.json','r') as file:
        data = json.load(file)
        print(data)
        return data    
if __name__=='__main__':
    app.run(debug=True)
    app.run()

