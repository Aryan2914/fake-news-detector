import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required resources (only the first time)
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')  # for WordNetLemmatizer

# Initialize tools
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    """
    Cleans and preprocesses raw text:
    - Lowercases
    - Removes punctuation and digits
    - Tokenizes
    - Removes stop words
    - Lemmatizes
    Returns: Cleaned text string
    """
    # Lowercase
    text = text.lower()
    
    # Remove special characters and digits
    text = re.sub(r'[^a-z\s]', '', text)
    
    # Tokenize and clean
    words = text.split()
    cleaned_words = [
        lemmatizer.lemmatize(word) for word in words if word not in stop_words
    ]
    
    return ' '.join(cleaned_words)

if __name__ == "__main__":
    sample = "Breaking: This is absolutely SHOCKING news! COVID19 vaccine found!!"
    print("Original:", sample)
    print("Cleaned:", clean_text(sample))
