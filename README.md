# Sach---The-Fake-News-Detector
Still Working on this project

# 📰 SACH - Fake News Detector

A simple and effective web-based tool that detects whether a news headline or text is likely **Fake** or **Real**, using Machine Learning and Natural Language Processing (NLP).

---

## ✅ Features

- Input news text/headline and check its authenticity.
- Uses a lightweight ML model (TF-IDF + Logistic Regression) or pre-trained models (e.g., BERT).
- Displays confidence scores and helpful fact-checking tips.
- Fast, responsive UI with optional loading animations.
- 100% free – uses open-source libraries and free hosting tools.

---

## 🚀 Project Flow

1. **User Input:** Text box for entering news text or headline.
2. **Frontend → Backend:** Sends data via `POST` request.
3. **Backend Processing:**
   - Preprocesses the text (cleaning, tokenization).
   - Applies ML model for classification.
   - Returns a result: `Fake` or `Real`, optionally with a confidence score.
4. **Frontend Display:** Presents the result with visual cues and helpful messages.

---

## ⚙️ Tech Stack

### 🔵 Frontend

- **React** or **Vanilla JavaScript**
- HTML/CSS for UI
- Displays:
  - Input form
  - Colored tag result (`✅ Real`, `❌ Fake`)
  - Loader during processing (optional)

### 🟡 Backend

- **Flask (Python)**
- Handles `POST` request from frontend
- Loads trained model using `joblib`
- Performs preprocessing and prediction
- Returns JSON result

### 🧠 Machine Learning

- **Model:** TF-IDF + Logistic Regression (lightweight)
- **Training Platform:** Google Colab
- **Dataset:** [Fake and Real News Dataset on Kaggle](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset)
- **Optional Upgrade:** Use `distilBERT` or another transformer model via Hugging Face

---

## 🛠️ Free Tools Used

| Tool           | Purpose                          |
|----------------|----------------------------------|
| Google Colab   | Train & export ML model          |
| GitHub         | Host source code                 |
| Vercel/Netlify | Deploy frontend                  |
| Render/Heroku  | Host Flask backend (free tier)   |
| Replit         | Test Flask + ML easily online    |

---

## 📈 Optional Extra Features

- Confidence score with explanations
- History of user checks
- Integration with real-time fact-checking APIs (e.g., Snopes, Google Fact Check)
- Language toggle for regional use cases

---

## 📂 Folder Structure (Suggested)

