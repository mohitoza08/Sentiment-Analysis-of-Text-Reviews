from flask import Flask, request, jsonify
import joblib
import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

app = Flask(__name__)

model = joblib.load("lr3_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))
stop_words = stop_words - {"not", "no", "nor", "never"}

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    tokens = text.split()
    tokens = [lemmatizer.lemmatize(w) for w in tokens if w not in stop_words]
    return " ".join(tokens)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    review = data.get("review")

    if not review or not review.strip():
        return jsonify({"error": "Empty review"}), 400

    cleaned = preprocess_text(review)
    vector = vectorizer.transform([cleaned])

    prob = model.predict_proba(vector)[0][1] 

   
    sentiment = "Positive" if prob >= 0.6 else "Negative"

    return jsonify({
        "sentiment": sentiment,
        "score": round(prob, 3)
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
