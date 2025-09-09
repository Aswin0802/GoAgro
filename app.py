from flask import Flask,render_template,request
import numpy as np
import pandas
import sklearn
import joblib

#importing model
model=joblib.load('model.joblib')
scaler=joblib.load('scaler.joblib')

#creating flask app
app=Flask(__name__)

#creating routes
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    N=int(request.form['Nitrogen'])
    P=int(request.form['Phosporus'])
    K=int(request.form['Potassium'])
    temperature=float(request.form['Temperature'])
    humidity=float(request.form['Humidity'])
    ph=float(request.form['Ph'])
    rainfall=float(request.form['Rainfall'])
    

    features=[N,P,K,temperature,humidity,ph,rainfall]
    single_pred=np.array(features).reshape(1,-1)
    rescaled_pred=scaler.transform(single_pred)
    prediction=model.predict(rescaled_pred)

    crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
                 8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
                 14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
                 19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"}
    if prediction[0] in crop_dict:
        crop=crop_dict[prediction[0]]
        print(f"{crop} is a best crop to be cultivated")
    else:
        print("No proper crop to be recommended")

    return render_template('home.html',result=crop)


#python main
if __name__=='__main__':
    app.run(debug=True)