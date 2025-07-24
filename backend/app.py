from flask import Flask, request, jsonify
from joblib import load
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')

app = Flask(__name__)

# Initialize preprocessing tools
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Tokenize
    words = text.split()
    
    # Remove stopwords and lemmatize
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    
    return ' '.join(words)

# Load models (in production, load these once when starting the app)
try:
    tfidf = load('models/tfidf_vectorizer.joblib')
    model = load('models/logistic_regression.joblib')
except Exception as e:
    print(f"Error loading models: {e}")
    tfidf = None
    model = None

@app.route('/predict', methods=['POST'])
def predict():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    data = request.get_json()
    text = data.get('text', '')
    
    if not text:
        return jsonify({"error": "Text is required"}), 400
    
    if not tfidf or not model:
        return jsonify({"error": "Model not loaded"}), 500
    
    try:
        # Preprocess text
        processed_text = preprocess_text(text)
        
        # Vectorize
        X = tfidf.transform([processed_text])
        
        # Predict
        prediction = model.predict(X)[0]
        proba = model.predict_proba(X)[0]
        
        # Get confidence
        confidence = np.max(proba)
        
        # Map prediction to label
        label = 'real' if prediction == 1 else 'fake'
        
        return jsonify({
            'prediction': label,
            'confidence': float(confidence),
            'text': text[:200] + '...' if len(text) > 200 else text
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    return "SACH Fake News Detector API is running!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
