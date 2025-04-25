from flask import Flask, render_template, request
import pickle

# Load model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        news_text = request.form['news']
        transformed_text = vectorizer.transform([news_text])
        prediction = model.predict(transformed_text)

        result = "Fake News 🛑" if prediction[0] == 0 else "Real News ✅"
        return render_template('index.html', prediction=result, text=news_text)

if __name__ == '__main__':
    app.run(debug=True)
