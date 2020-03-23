from flask import Flask, render_template, request
import pickle as pkl

with open('model.pkl','rb') as f:
    data=pkl.load(f)
    
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def hello():
    if request.method == "POST":
        myDict=request.form
        greScore = int(myDict['greScore'])
        toeflScote = int(myDict['toeflScore'])
        sopRating = float(myDict['sopRating'])
        lorRating = float(myDict['lorRating'])
        uniRank = int(myDict['uniRank'])
        cgpa = float(myDict['cgpa'])
        research = int(myDict['research'])
        inputFeature=[greScore,toeflScote,uniRank,sopRating,lorRating,cgpa,research]
        print(data.predict([inputFeature])[0])
        return render_template('result.htm',adm=round(data.predict([inputFeature])[0]*100))
    return render_template('index.htm')

if __name__ == '__main__':
    app.run(debug=True)
    
    