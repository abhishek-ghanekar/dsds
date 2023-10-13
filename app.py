from flask import Flask,request, render_template , url_for , redirect
import pickle
import numpy as np
app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def hello():
    return render_template("forest_fire.html")
@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    # int_features = [int(request.form.get('key', default=None)) for key in request.form.keys()]
    final = [np.array(int_features)]
    print(int_features)
    print(final)
    prediction = model.predict_proba(final)
    output = '{0:.{1}f}'.format(prediction[0][1], 2)
    if(output > str(0.5)):
        return render_template('forest_fire.html', pred = 'Your forest is in danger. \n Probablity of fire is {}'.format(output),bhai="kuch karna hain kya")
    else:
        return render_template('forest_fire.html',pred='Your Forest is safe.\n Probability of fire occuring is {}'.format(output),bhai="Your Forest is Safe for now")

if __name__ == '__main__':
    app.run(debug=True)