import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time

# --- Spotify API Configuration ---
CLIENT_ID = "62caef9f6d7c443391668af01e48ec8c"
CLIENT_SECRET = "f12fb660ffc04519ac588f568d8a4254"

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# --- Helper Functions ---
def get_song_album_cover_url(song_name, artist_name):
    """Fetches the album cover URL from Spotify."""
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")

    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        return album_cover_url
    else:
        return "https://i.postimg.cc/0QNxYz4V/social.png"

def recommend(song):
    """Generates song recommendations based on similarity."""
    index = music[music['song'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_music_names = []
    recommended_music_posters = []
    recommended_music_artists = []

    for i in distances[1:6]:
        artist = music.iloc[i[0]].artist
        song_name = music.iloc[i[0]].song

        recommended_music_posters.append(get_song_album_cover_url(song_name, artist))
        recommended_music_names.append(song_name)
        recommended_music_artists.append(artist)

    return recommended_music_names, recommended_music_posters, recommended_music_artists

# --- Streamlit UI ---

st.set_page_config(
    page_title="Music Recommender System",
    page_icon="🎵",
    layout="centered",
    initial_sidebar_state="auto"
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #121212;
        color: #ffffff;
        font-family: 'Segoe UI', sans-serif;
    }

    .main-header {
        font-size: 3.5em;
        font-weight: bold;
        color: #1DB954;
        text-align: center;
        margin-top: 1em;
        margin-bottom: 0.3em;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.5);
    }

    .subheader {
        font-size: 1.3em;
        color: #e0e0e0;
        text-align: center;
        margin-bottom: 2em;
    }

    .stSelectbox label {
        font-size: 1.1em;
        font-weight: bold;
        color: #ffffff;
    }

    .stSelectbox div[role="combobox"] {
        background-color: #1e1e1e;
        color: #ffffff;
        border-radius: 8px;
        padding: 10px;
    }

    .stButton > button {
        background: #1DB954;
        color: white;
        font-size: 1.1em;
        font-weight: bold;
        border-radius: 12px;
        padding: 10px 24px;
        border: none;
        transition: all 0.3s ease-in-out;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.3);
    }

    .stButton > button:hover {
        background-color: #1ed760;
        transform: translateY(-2px);
        box-shadow: 4px 4px 15px rgba(0,0,0,0.4);
    }

    .fade-in {
        animation: fadeIn 1s ease-in;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .stImage > img {
        border-radius: 14px;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.5);
        transition: transform 0.3s ease;
    }

    .stImage > img:hover {
        transform: scale(1.05);
    }

    .song-title {
        font-size: 1.1em;
        font-weight: 600;
        color: #ffffff;
        text-align: center;
        margin-top: 0.4em;
    }

    .artist-name {
        font-size: 0.95em;
        color: #b3b3b3;
        text-align: center;
        margin-bottom: 1.2em;
    }

    hr {
        border-top: 1px solid #333;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="main-header">Music Recommender System</h1>', unsafe_allow_html=True)
st.markdown('<p class="subheader">Discover new songs based on your favorites!</p>', unsafe_allow_html=True)

try:
    music = pickle.load(open('df.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
except FileNotFoundError:
    st.error("Error: Data files (df.pkl or similarity.pkl) not found. Please run generate_data.py first.")
    st.stop()

music_list = music['song'].values

selected_song = st.selectbox(
    "Select a song to get recommendations:",
    music_list,
    index=0
)

if st.button('Show Recommendations'):
    with st.spinner('Fetching recommendations...'):
        time.sleep(1.2)  # Slight delay to help fade-in feel natural
        recommended_music_names, recommended_music_posters, recommended_music_artists = recommend(selected_song)

    st.markdown("---")
    st.subheader(f"Recommendations for: {selected_song}")

    if recommended_music_names:
        cols = st.columns(5)
        for i in range(5):
            with cols[i]:
                st.markdown('<div class="fade-in">', unsafe_allow_html=True)
                st.image(recommended_music_posters[i], use_container_width=True)
                st.markdown(f'<p class="song-title">{recommended_music_names[i]}</p>', unsafe_allow_html=True)
                st.markdown(f'<p class="artist-name">{recommended_music_artists[i]}</p>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("No recommendations found for this song. Try another one!")

st.markdown("---")
