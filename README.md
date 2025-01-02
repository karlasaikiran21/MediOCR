**MediOCR: Medical Prescription OCR & Medicine Recommendation System********
MediOCR is an AI-powered application designed to digitize handwritten medical prescriptions using Optical Character Recognition (OCR) and provide relevant medicine recommendations. Built with a robust stack of Python, React.js, Node.js, and MongoDB, the system seamlessly integrates OCR and Natural Language Processing (NLP) for efficient text extraction and analysis.

Features
Extract handwritten text from prescriptions using Tesseract OCR.
Analyze prescription content with NLP to identify medicines and dosages.
Dynamically fetch relevant medicines from a MongoDB database.
Fully responsive React.js frontend and scalable Node.js backend.
Supports real-time prescription upload and medicine recommendations.

Tech Stack
Frontend: React.js, HTML, CSS, JavaScript
Backend: Node.js, Express.js, Python
Database: MongoDB
OCR Engine: Tesseract (Version 5.4.0)
NLP Frameworks: spaCy, NLTK

Use Case
MediOCR is ideal for hospitals, pharmacies, and healthcare providers to digitize prescription management and enhance medication tracking and accuracy.

How to Use
Upload a scanned or photographed prescription.
MediOCR extracts text from the image and processes it.
Get an instant recommendation of relevant medicines.


## Installation & Setup

Prerequisites
1. **Node.js** (v16+)
2. **Python** (v3.8+)
3. **MongoDB**
4. **Tesseract OCR**: Install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) (ensure version 5.4.0 is installed and added to your system's PATH).

### Backend Setup
1. Install dependencies:
   npm install
  
2. Configure the environment:
   - Create a `.env` file in the `backend` directory.
   - Add the following variables:
     ```env
     PORT=5000
     MONGO_URI=your_mongodb_connection_string
     TESSERACT_PATH=/path/to/tesseract
     ```
3. Start the backend server:
   bash
   npm start
   
### Frontend Setup
1. Navigate to the frontend directory:
   cd ../frontend
2. Install dependencies:
   npm install
3. Start the React development server:
   npm start

 Running the Application
1. Ensure MongoDB is running.
2. Start the backend server and frontend server simultaneously.
3. Open the app in your browser at `http://localhost:3000`.

### Additional Notes
- **Database Seeding**: Use a script to populate the database with sample medicines.
- **Testing OCR**: Upload a sample prescription to test the OCR functionality.
