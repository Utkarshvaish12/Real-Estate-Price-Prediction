from flask import Flask, render_template, request
import pickle
app = Flask(__name__)
# load the model
model = pickle.load(open('linear_regression_model.sav', 'rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html', **locals())

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    features = features = ['L', 'La', 'TP', 'S', 'LR', 'DR', 'K', 'BR',
                           'F', 'BT', 'CT', 'RC', 'BS', 'LRa', 'E', 'YP', 'Sub', 'D']

    input_values = [request.form[feature] for feature in features]

    input_values = list(map(int, input_values)) 
    result = model.predict([input_values])[0]
    return render_template('index.html', result=result)
if __name__ == '__main__':
    app.run(debug=True)