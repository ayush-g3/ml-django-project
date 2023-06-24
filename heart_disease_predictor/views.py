from django.shortcuts import render

# our home page view
def home(request):    
    return render(request, 'index.html')

# custom method for generating predictions
def getPredictions(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):
    import pickle
    model = pickle.load(open("model.sav", "rb"))
    prediction = model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    prediction=prediction[0]
    
    if prediction == 0:
        return "no heart disease"
    elif prediction == 1:
        return "heart disease"
    else:
        return "error"
        

# our result page view
def result(request):
    age = int(request.GET['age'])
    sex = int(request.GET['sex'])
    cp = int(request.GET['cp'])
    trestbps = int(request.GET['trestbps'])
    chol = int(request.GET['chol'])
    fbs = int(request.GET['fbs'])
    restecg = int(request.GET['restecg'])
    thalach = int(request.GET['thalach'])
    exang = int(request.GET['exang'])
    oldpeak = float(request.GET['oldpeak'])
    slope = int(request.GET['slope'])
    ca = int(request.GET['ca'])
    thal = int(request.GET['thal'])

    result = getPredictions(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)

    return render(request, 'result.html', {'result':result})