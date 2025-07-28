# 🎵 Music Recommendation System

A simple content-based music recommender system using song lyrics, TF-IDF, and cosine similarity.

---

## 🚀 Features

- Recommends similar songs based on lyrical content
- Uses stemming and tokenization for better matching
- Powered by Scikit-learn, NLTK, and pandas
- Built with Streamlit for UI

---

## 📁 Project Structure

music-recommender/

│

├── app.py # Streamlit web app

├── generate_data.py (Preprocesses lyrics and builds similarity matrix)

├── df.pkl ( Processed and stemmed DataFrame )

├── similarity.pkl ( Cosine similarity matrix )

├── spotify_millsongdata.csv ( Original dataset (not uploaded to GitHub) )

├── .gitignore

└── README.md

---

## 🔧 Setup Instructions

1. **Clone the repo**  
   git clone https://github.com/vanditajain-29/music-recommender.git
   
   cd music-recommender

3. **Install dependencies**
   pip install -r requirements.txt

4. **Download the dataset manually**
   Download spotify_millsongdata.csv from:

   Kaggle Dataset at https://www.kaggle.com/datasets/notshrirang/spotify-million-song-dataset

   Place it in the root folder of the project.

6. **Generate model files**
   python generate_data.py

7. **Run the app**
   streamlit run app.py

## 🔗 Dataset Note
Due to GitHub's file size limits, the full CSV and .pkl files are not included.

This project uses a reduced sample of 1,500 songs to keep file sizes small. You can increase this number in generate_data.py for better results (if you have enough memory).

## 📦 Dependencies
pandas

nltk

scikit-learn

streamlit

pickle

**Install them via:**
pip install pandas nltk scikit-learn streamlit

## ✨ Output
Streamlit web app that suggests similar songs based on your song selection   

<img width="1919" height="942" alt="image" src="https://github.com/user-attachments/assets/ef7a694d-c8a2-40dd-b607-5fe4e41335c7" />

<img width="1918" height="954" alt="image" src="https://github.com/user-attachments/assets/316d3a9c-f964-4c34-b2ff-96a4e65010c9" />


## 🪪 License
MIT License



