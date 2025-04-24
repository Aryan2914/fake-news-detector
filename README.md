# 📰 Fake News Detection System

## 📌 Objective
To build a system that can classify news articles (especially headlines or body text) as real or fake using machine learning techniques.

## 🔍 Problem Background
With the rise of social media, misinformation spreads quickly. Detecting fake news is a crucial real-world problem, especially during elections and pandemics. This project applies NLP and ML to analyze text and identify whether a piece of news is trustworthy.

## 🧠 How It Works
1. **Data Collection**: Use open-source datasets like the Fake News Dataset from Kaggle or LIAR dataset.
2. **Preprocessing**: Clean text, remove stop words, lemmatize, and transform using TF-IDF.
3. **Modeling**: Train machine learning models such as Logistic Regression, Naive Bayes, and Random Forest.
4. **Evaluation**: Use metrics like accuracy, precision, recall, and F1-score.
5. **(Optional)**: Deploy via Streamlit/Flask.

## ⚙️ Tech Stack
- **Language**: Python
- **Libraries**: scikit-learn, pandas, NLTK, spaCy
- **ML Models**: Logistic Regression, Naive Bayes, Random Forest
- **(Optional)**: Streamlit or Flask for UI, HuggingFace Transformers for BERT-based modeling

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Aryan2914/fake-news-detection.git
   cd fake-news-detection
