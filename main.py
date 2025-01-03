from flask import Flask, request, render_template, redirect, url_for, session  # Import additional methods
import numpy as np
import pandas as pd
import pickle
import io
from PIL import Image
import pytesseract  # Import pytesseract for OCR
from pymongo import MongoClient  # Import MongoClient for MongoDB
from werkzeug.security import generate_password_hash, check_password_hash  # For password hashing

# flask app
app = Flask(__name__)

# Initialize MongoDB client
client = MongoClient('mongodb://localhost:27017/')
db = client['mediocr_db']  # Change the database name as needed
users_collection = db['users']  # Change the collection name as needed

# Ensure you have an index on email for faster queries
users_collection.create_index('email', unique=True)

# Set the path for Tesseract executable (if necessary)
# For Windows, make sure Tesseract is installed and add its path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Adjust the path if needed

# Load dataset
sym_des = pd.read_csv("dataset/symtoms_df.csv")
precautions = pd.read_csv("dataset/precautions_df.csv")
workout = pd.read_csv("dataset/workout_df.csv")
description = pd.read_csv("dataset/description.csv")
medications = pd.read_csv('dataset/medications.csv')
diets = pd.read_csv("dataset/diets.csv")

# Load model
svc = pickle.load(open('models/svc.pkl', 'rb'))

# Custom and helping functions
def helper(dis):
    desc = description[description['Disease'] == dis]['Description']
    desc = " ".join([w for w in desc])

    pre = precautions[precautions['Disease'] == dis][['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']]
    pre = [col for col in pre.values]

    med = medications[medications['Disease'] == dis]['Medication']
    med = [med for med in med.values]

    die = diets[diets['Disease'] == dis]['Diet']
    die = [die for die in die.values]

    wrkout = workout[workout['disease'] == dis]['workout']

    return desc, pre, med, die, wrkout



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        symptoms = [x for x in symptoms_dict.keys() if request.form.get(x)]
        input_features = [1 if symptom in symptoms else 0 for symptom in symptoms_dict.keys()]

        # Get the prediction from the model
        prediction = svc.predict([input_features])
        disease = diseases_list.get(prediction[0], "Disease not found")
        
        # Get additional information based on the predicted disease
        desc, pre, med, die, wrkout = helper(disease)
        
        return render_template('index.html', disease=disease, desc=desc, pre=pre, med=med, die=die, wrkout=wrkout)

@app.route('/extract_text', methods=['POST'])
def extract_text():
    if 'image' not in request.files:
        return render_template('index.html', extracted_text="No file uploaded.")
    
    file = request.files['image']
    if file.filename == '':
        return render_template('index.html', extracted_text="No file selected.")
    
    # Convert the file to an image format that Tesseract can process
    image = Image.open(io.BytesIO(file.read()))
    
    # Use Tesseract to extract text
    extracted_text = pytesseract.image_to_string(image)
    
    return render_template('index.html', extracted_text=extracted_text)

if __name__ == "__main__":
    app.run(debug=True)
