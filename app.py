from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import pandas as pd
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedKFold
app = Flask(__name__, template_folder='C:/Users/Richa/Downloads/EXECUTABLE/template')

model = pickle.load(open('C:/Users/Richa/Downloads/EXECUTABLE/Attack_traffic_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    #sttl','ct_dst_sport_ltm', 'ct_src_dport_ltm', 'swin', 'dwin',
    #int_features = [int(x) for x in request.form.values()]
    #final_features = [np.array(int_features)]
    
    #cv_object= StratifiedKFold(10)
   
    #prediction = model.predict(final_features)
    #pred=pd.DataFrame(prediction)
     if request.method == 'POST':
        sttl = int(request.form['sttl'])
        ct_dst_sport_ltm=int(request.form['ct_dst_sport_ltm'])
        ct_src_dport_ltm=int(request.form['ct_src_dport_ltm'])
        swin=int(request.form['swin'])
        dwin=int(request.form['dwin'])
        
     prediction=model.predict([[sttl,ct_dst_sport_ltm, ct_src_dport_ltm, swin, dwin]])
     
     if(prediction==1):
       output="Attack"
     else:
        output="Normal"
         
     return render_template('index.html',prediction_text="prediction is {}".format(output))
    
     
if __name__=="__main__":
    app.run(debug=True)