🚀 Project Title & Tagline
===========================
### Sentiment Analysis Web Application 🌟
> "Unlock the Power of Text Analysis with Our Cutting-Edge Sentiment Analysis Tool" 💡

📖 Description
----------------
The Sentiment Analysis Web Application is a powerful tool designed to analyze text data and determine the sentiment behind it. This project utilizes Natural Language Processing (NLP) techniques to categorize text as positive, negative, or neutral. The application is built using a combination of Flask and Streamlit, providing a robust and user-friendly interface for users to input text and receive sentiment analysis results.

The application's primary function is to provide accurate sentiment analysis, which can be applied to various domains such as customer review analysis, social media monitoring, and market research. By leveraging the power of NLP, this project aims to help businesses and individuals gain valuable insights into customer opinions and preferences. With its intuitive interface and robust backend, the Sentiment Analysis Web Application is an ideal solution for anyone looking to unlock the power of text analysis.

The project consists of two primary components: a Flask-based backend API and a Streamlit-based frontend interface. The backend API is responsible for handling text analysis using NLP techniques, while the frontend interface provides a user-friendly platform for users to input text and receive sentiment analysis results. By separating the backend and frontend logic, the project ensures a clean and maintainable architecture, making it easier to update and extend the application in the future.

✨ Features
-------------
The following features are included in the Sentiment Analysis Web Application:

1. **Text Analysis**: The application can analyze text data and determine the sentiment behind it, categorizing it as positive, negative, or neutral.
2. **NLP Techniques**: The project utilizes various NLP techniques, including tokenization, lemmatization, and stopword removal, to preprocess text data and improve analysis accuracy.
3. **Flask Backend**: The application features a Flask-based backend API, providing a robust and scalable platform for handling text analysis requests.
4. **Streamlit Frontend**: The project includes a Streamlit-based frontend interface, offering a user-friendly and intuitive platform for users to input text and receive sentiment analysis results.
5. **API Connectivity**: The frontend interface connects to the backend API via HTTP requests, enabling seamless communication between the two components.
6. **Text Input**: The application provides a text input field, allowing users to enter text data for sentiment analysis.
7. **Sentiment Results**: The project displays sentiment analysis results, including the sentiment label (positive, negative, or neutral) and a confidence score.
8. **Error Handling**: The application includes error handling mechanisms to handle invalid input, API connection issues, and other potential errors.

🧰 Tech Stack Table
-------------------
| Category | Technology |
| --- | --- |
| Frontend | Streamlit |
| Backend | Flask |
| NLP Library | NLTK |
| Machine Learning Library | scikit-learn (via joblib) |
| HTTP Client | requests |
| Text Preprocessing | NLTK (tokenization, lemmatization, stopword removal) |

📁 Project Structure
---------------------
The project is organized into the following folders and files:

* `app.py`: The Flask-based backend API, responsible for handling text analysis requests.
* `ui.py`: The Streamlit-based frontend interface, providing a user-friendly platform for users to input text and receive sentiment analysis results.
* `Sentiment.ipynb`: Jupyter Notebook containing dataset exploration, NLP preprocessing, model training, and evaluation for sentiment analysis.
* `lr3_model.pkl`: Trained Logistic Regression machine learning model used for sentiment prediction in the application.
* `requirements.txt`: A file listing dependencies required to run the project.
* `README.md`: This file, providing an overview of the project and its features.

⚙️ How to Run
----------------
To run the Sentiment Analysis Web Application, follow these steps:

1. **Setup**: Clone the repository and navigate to the project directory.
2. **Environment**: Create a virtual environment using `python -m venv venv` and activate it using `source venv/bin/activate` (on Linux/Mac) or `venv\Scripts\activate` (on Windows).
3. **Dependencies**: Install dependencies listed in `requirements.txt` using `pip install -r requirements.txt`.
4. **Build**: Build the Flask backend API by running `python app.py`.
5. **Deploy**: Deploy the Streamlit frontend interface by running `streamlit run ui.py`.

🧪 Testing Instructions
------------------------
To test the Sentiment Analysis Web Application, follow these steps:

1. **Text Input**: Enter a sample text into the text input field.
2. **Sentiment Analysis**: Click the "Analyze" button to trigger sentiment analysis.
3. **Results**: Verify that the sentiment analysis results are displayed correctly, including the sentiment label and confidence score.
4. **Error Handling**: Test error handling mechanisms by entering invalid input or disconnecting from the backend API.


📦 API Reference
-----------------
The Sentiment Analysis Web Application provides a RESTful API for sentiment analysis. The API endpoint is `http://127.0.0.1:5000/predict`, and it accepts POST requests with a JSON payload containing the text to be analyzed.

* **Request Body**: `{
  "review": "This movie was amazing and entertaining"
}`
* **Response**: `{
  "sentiment": "Positive",
  "score": 0.91
}`

👤 Author
-----------
The Sentiment Analysis Web Application was developed by Mohit Oza.

📝 License
-----------
The Sentiment Analysis Web Application is licensed under the [MIT License](https://opensource.org/licenses/MIT).
