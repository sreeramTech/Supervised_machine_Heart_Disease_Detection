from flask import  Flask,render_template,request,url_for,redirect
from flask_bootstrap import Bootstrap
from datetime import date,datetime
import process
import prediction
app = Flask(__name__)
Bootstrap(app)
today = date.today()
now = datetime.now()
current = now.strftime("%H:%M:%S")

name = ""
@app.route('/', methods = ["POST", "GET"])
def index():
    if request.method == "POST":
        name = request.form['patientNameInput']
        sex = request.form['patientSexInput']
        age = request.form['patientAgeInput']
        cp = request.form['patientCpInput']
        trestbps = request.form['patientTrestbpsInput']
        chol = request.form['patientCholInput']
        fbs  = request.form['patientFbsInput']
        restecg  = request.form['patientRestecgInput']
        thalach  = request.form['patientThalacInput']
        exang  = request.form['patientExangInput']
        oldpeak  = request.form['patientOldpeakInput']
        slope  = request.form['patientSlopeInput']
        ca  = request.form['patientCaInput']
        thal  = request.form['patientThalInput']
             
        data = {
            'age':age,
            'sex':sex,	
            'cp':cp,	
            'trestbps':trestbps,	
            'chol':chol,	
            'fbs':fbs,	
            'restecg':restecg,	
            'thalach':thalach,	
            'exang':exang,	
            'oldpeak':oldpeak,	
            'slope':slope,	
            'ca':ca,	
            'thal':thal
        }

        predict = prediction.Prediction(data)
        temp = process.proc(data)
        


        

      

        
        return redirect(url_for("user",usr = predict , nm = name, sex = temp['sex'], age = data['age'],chol = temp['chol'],trestbps = temp['trestbps'],thalach = temp['thalach'],cp = temp['cp'],tdate = today,ttime = current))
      

    else:    
        return render_template('index.html')
@app.route('/<usr>/<nm>/<sex>/<age>/<chol>/<trestbps>/<thalach>/<cp>/<tdate>/<ttime>')
def user(usr,nm,sex,age,chol,trestbps,thalach,cp,tdate,ttime):
    if usr == "[1]":
        return render_template("result_risk.html", prediction = "High Risk",name = nm,sex = sex,age = age, chol = chol,trestbps = trestbps, thalach = thalach,cp = cp,tdate = tdate,ttime = ttime)
    else:
        return render_template("result_risk.html",prediction = "Low Risk", name = nm,sex = sex, age =  age, chol = chol,trestbps = trestbps,thalach = thalach,cp = cp,tdate = tdate,ttime = ttime)
if __name__=='__main__':
    app.run(debug=True)
