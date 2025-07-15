from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import joblib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_info')
def get_info():
    return render_template('get_info.html')

@app.route('/result', methods=['POST'])
def result():
    try:
        request_data = request.form
        print("Received form data:", dict(request_data))  # Debug print
        
        # Load and prepare the data
        data = pd.read_csv('Airlines.csv')
        df = pd.DataFrame(data)
        df.drop('Flight', axis=1, inplace=True)

        # Encode the categorical variables
        le_from = LabelEncoder()
        df['AirportFrom'] = le_from.fit_transform(df['AirportFrom'])

        le_to = LabelEncoder()
        df['AirportTo'] = le_to.fit_transform(df['AirportTo'])
        
        # Prepare features and target
        X = df.iloc[:, 1:-1].values
        y = df.iloc[:, -1].values
        
        # Apply transformations
        ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
        X = ct.fit_transform(X)
        
        # Split and train the model
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Fix convergence warning by increasing max_iter and changing solver
        model = LogisticRegression(max_iter=1000, solver='liblinear')
        model.fit(X_train, y_train)

        # Save the models
        joblib.dump(le_from, 'le_from.pkl')
        joblib.dump(le_to, 'le_to.pkl')
        joblib.dump(ct, 'ct.pkl')
        joblib.dump(model, 'model.pkl')

        # Get user input and make prediction
        # Fix: Use correct form field names and pass as arrays to transform
        airport_from = request_data['AirportFrom']
        airport_to = request_data['AirportTo']
        airline = request_data['airline']  # Form uses 'airline', not 'Airline'
        day_of_week = int(request_data['day'])
        time = int(request_data['time'])
        length = int(request_data['Length'])
        
        # Transform airport codes (pass as lists to avoid the shape error)
        airportfrom_encoded = le_from.transform([airport_from])[0]
        airportto_encoded = le_to.transform([airport_to])[0]

        # Create the input row for prediction
        new_row = [[airline, airportfrom_encoded, airportto_encoded, day_of_week, time, length]]
        
        # Transform and predict
        X_new = ct.transform(new_row)
        prediction = model.predict(X_new)[0]
        
        # Get probability for confidence
        proba = model.predict_proba(X_new)[0]
        confidence = max(proba) * 100
        
        result_text = "Delay Predicted" if prediction == 1 else "No Delay Predicted"
        return render_template('result.html', 
                             delay_prediction=result_text,
                             confidence=f"{confidence:.1f}%")
                             
    except Exception as e:
        print(f"Error in prediction: {str(e)}")
        return render_template('result.html', 
                             delay_prediction="Error in prediction. Please try again.",
                             confidence="N/A")
if __name__ == '__main__':
    app.run(debug=True, port=5001)