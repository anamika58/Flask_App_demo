from flask import Flask
from pymongo import MongoClient
from flask import request
from bson.json_util import dumps
import json
import traceback

client =MongoClient("mongodb://localhost:27017/")

db=client["acc"]
col=db["acc_data"]

app = Flask(__name__)
app.debug=True
@app.route("/get-value", methods = ['POST'])
def find_value():
    try:            
        data=json.loads(request.data)
        query={"company_id":"d5209bee-7b16-4236-a21a-e805cc8fcb1a"}
        projection={"data_array":1}
        result = list(col.find(query,projection))
        return result        
    except Exception as e:        
        traceback.print_exc()
        return dumps({'error' : str(e)})
app.run()




