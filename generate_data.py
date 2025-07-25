import pandas as pd
import nltk
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

nltk.download('punkt')
nltk.download('punkt_tab') 

# Load dataset
df = pd.read_csv('spotify_millsongdata.csv')

# Clean and preprocess text
df['text'] = df['text'].str.lower().replace(r'\n', ' ', regex=True)

# Sample for faster processing
df = df.sample(1500).drop('link', axis=1).reset_index(drop=True)

# Tokenization + Stemming
stemmer = PorterStemmer()
def token(txt):
    tokens = nltk.word_tokenize(txt)
    return " ".join([stemmer.stem(w) for w in tokens])

df['text'] = df['text'].apply(token)

# TF-IDF and similarity
tfidf = TfidfVectorizer(analyzer='word', stop_words='english')
matrix = tfidf.fit_transform(df['text'])
similarity = cosine_similarity(matrix)

# Save
pickle.dump(df, open('df.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))
print("✅ Saved df.pkl and similarity.pkl")
