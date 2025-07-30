from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model and scaler
model = pickle.load(open('rfc.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict')
def predict():
    return render_template('inner-page.html')

@app.route('/submit', methods=['POST'])
def submit():
    # The form sends back the encoded integer values
    input_features = [int(x) for x in request.form.values()]
    
    # Reshape for the scaler
    input_array = np.array(input_features).reshape(1, -1)
    
    # Scale the features
    scaled_features = scaler.transform(input_array)
    
    # Predict
    prediction = model.predict(scaled_features)
    
    # Determine the result message
    if prediction[0] == 0: # Assuming 0 is 'Critical'
        result_text = "According to our study, the animal's condition appears to be critical. Immediate consultation is advised."
    else:
        result_text = "The animal appears to be in normal condition."

    return render_template('output.html', result=result_text)

if __name__ == "__main__":
    app.run(debug=True)