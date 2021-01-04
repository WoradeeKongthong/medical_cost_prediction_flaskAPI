After I did the data analysis and built ML models in  
https://github.com/WoradeeKongthong/medical_cost_regression,  

The RMSE of each model is as following :  
Multiple Linear Regression = 5486  
Polynomial Regression = 4610  
SVR = 4524  
Decision Tree = 4791  
Random Forest = 4082  
XGBRegression = 5301  
ANN = 4372  

I selected the Random Forest model to do the deployment.  
  
===============================================================  
Deployment details  
- create API with Flask
- containerization with Docker
- (optional) pull my uploaded docker repository  

===============================================================  
# How to use the ML model
(after you clone or download the project
and install the required libraries in requirements.txt)

## Flask application
1. in your terminal, cd to the project
2. start the flask api with command `$ python app.py`
3. use the api from the following options  
	3.1 type the url in the browser  
		- visit the home page at http://0.0.0.0:8000/  
		- make a prediction from entered information at http://0.0.0.0:8000/predict?age=33&sex=female&bmi=18.36&children=0&smoker=no&region=southeast  
	3.2 using Postman app  
		- predict from GET http://0.0.0.0:8000/predict and specify the parameters age, sex, bmi, children, smoker and region in Params tab  
		- predict from csv file from POST http://0.0.0.0:8000/predict_file, select Body tab, select form-data, specify key as the word file, and select the csv file.  
		- predict from json input from POST http://0.0.0.0:8000/predict_json/, select Body tab, select raw JSON and type the input list such as [33,"female",18.36,0,"no","southeast"]  
	3.3 using curl   
		- open terminal  
		- type `curl --location --request POST '0.0.0.0:8000/predict_json/' --header 'Content-Type: application/json' --data-raw '[33,"female",18.36,0,"no","southeast"]'`  

## Docker container
1. open your terminal, cd to the project
2. create docker image with command `$ docker build -t <projectName>`
3. list docker images with command `$ docker images`
4. run the image with command `docker run -p 8000:8000 <projectName>`
5. use the api as the step 3 in Flas application section above
6. kill the process by opening new terminal and check the container id with the command `$docker ps` and `$ docker stop <CONTAINERID>`

## Pull my uploaded docker repository
1. pull the repository with command `$ docker pull woradee/medical_cost:simple`
2. run the image with command `$ docker run -p 8000:8000 woradee/medical_cost:simple`
