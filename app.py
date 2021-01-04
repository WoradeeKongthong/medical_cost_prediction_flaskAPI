from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
import json

app=Flask(__name__)
pickle_in = open("model/MedicalCostRandomForest.pkl","rb")
data=pickle.load(pickle_in)
estimator=data['model']

@app.route('/')
def welcome():
    return "Welcome to Medical Cost Prediction Project"

@app.route('/predict')
def predict_from_get():
    
    age=request.args.get("age")
    sex=request.args.get("sex")
    bmi=request.args.get("bmi")
    children=request.args.get("children")
    smoker=request.args.get("smoker")
    region=request.args.get("region")
    
    x=[age,sex,bmi,children,smoker,region]
    
    # convert x to DataFrame
    col = ['age','sex','bmi','children','smoker','region']
    x = pd.DataFrame(data=[x],columns=col)
    
    prediction=estimator.predict(x)
    
    return "The answer is"+str(prediction)
    # try http://0.0.0.0:8000/predict?age=33&sex=female&bmi=18.36&children=0&smoker=no&region=southeast on your url
    # try postman > GET > params

@app.route('/predict_file',methods=["POST"])
def predict_from_file():
 
    df_test = pd.read_csv(request.files.get("file"))
    prediction=estimator.predict(df_test)
    
    return str(list(prediction))
    # try with postman > POST > Body > from-data > KEY: file > select file

@app.route('/predict_json/', methods=['GET','POST'])
def predict_from_json():
    
    # json input
    x = request.get_json()
    
    # convert x to DataFrame
    col = ['age','sex','bmi','children','smoker','region']
    x = pd.DataFrame(data=[x],columns=col)
        
    # make prediction
    prediction = estimator.predict(x)
    response = json.dumps({'prediction':list(prediction)})
    print(response)
    return response
    # try with postman
    # or curl --location --request POST '0.0.0.0:8000/predict_json/' --header 'Content-Type: application/json' --data-raw '[33,"female",18.36,0,"no","southeast"]'

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)
    
    
