import streamlit as st
import os

# App configuration
st.set_page_config(
    page_title="Taji Mvikeni Album by Imara Daima Pathfinder Club, The Saffrons",
    page_icon="album/over.png" if os.path.exists("album/over.png") else "🎵",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)

# CSS for Spotify-like table, consistent styling, and hiding Streamlit branding
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
        padding: 20px;
        border-radius: 10px;
        max-width: 800px;
        margin: auto;
    }
    .title {
        font-size: 36px;
        color: #2c3e50;
        text-align: center;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 18px;
        color: #34495e;
        text-align: center;
        margin-bottom: 20px;
    }
    .footer {
        font-size: 14px;
        color: #7f8c8d;
        text-align: center;
        margin-top: 20px;
    }
    .spotify-header {
        display: flex;
        align-items: center;
        padding: 12px;
        background-color: #e0e0e0;
        font-weight: bold;
        font-family: Arial, sans-serif;
        font-size: 16px;
        color: #2c3e50;
        border-radius: 4px 4px 0 0;
        border-bottom: 2px solid #ccc;
    }
    .spotify-row {
        display: flex;
        align-items: center;
        padding: 5px;
        border-bottom: 1px solid #ddd;
        font-family: Arial, sans-serif;
        font-size: 16px;
        color: #2c3e50;
        background-color: #ffffff;
    }
    .spotify-row:hover {
        background-color: #f9f9f9;
    }
    .track-column {
        width: 50px;
        text-align: left;
    }
    .title-column {
        flex: 1;
        text-align: left;
    }
    .button-column {
        width: 120px;
        text-align: right;
    }
    .download-button {
        background-color: #1db954;
        color: white;
        padding: 6px 12px;
        border-radius: 4px;
        border: none;
        font-size: 14px;
        cursor: pointer;
        width: 100px;
        text-align: center;
    }
    .download-button:hover {
        background-color: #17a34a;
    }
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="stToolbar"] {visibility: hidden;}
    [data-testid="stDecoration"] {visibility: hidden;}
    [data-testid="stFooter"] {display: none;}
    div[data-testid="stFooter"] {visibility: hidden;}
    .streamlit-footer {display: none;}
    .css-1v3fvcr {display: none;}
    .css-1v0mbdj img {display: none;}
    .css-1v0mbdj {display: none;}
    </style>
""", unsafe_allow_html=True)

# Main page
st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown('<h3 class="title">Taji Mvikeni Album by Imara Daima Pathfinder Club, The Saffrons</h3>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Download the album songs below, launching May 24th!</p>', unsafe_allow_html=True)

# Center two album covers side by side
st.markdown('<div style="display: flex; justify-content: center; gap: 20px;">', unsafe_allow_html=True)
col1, col2 = st.columns(2)  # Two equal columns for images

# First image
with col1:
    if os.path.exists("album/over.png"):
        st.image("album/over.png", caption="Taji Mvikeni Album", width=150)  # Passport size
    else:
        st.error("Album cover not found at 'album/over.png'.")

# Second image
with col2:
    if os.path.exists("album/over.jpeg"):  # Replace with your second image path
        st.image("album/over.jpeg", caption="The Saffrons", width=150)  # Passport size
    else:
        st.error("Second album cover not found at 'album/over.jpeg'.")
st.markdown('</div>', unsafe_allow_html=True)

# Song list section
st.markdown("### Song List")
song_folder = "album"
mp3_files = [f for f in os.listdir(song_folder) if f.endswith(".mp3")]

if mp3_files:
    # Header
    st.markdown(
        '<div class="spotify-header">'
        '<div class="track-column">#</div>'
        '<div class="title-column">Title</div>'
        '<div class="button-column">Download</div>'
        '</div>',
        unsafe_allow_html=True
    )

    # Rows
    for index, file in enumerate(sorted(mp3_files)):
        track_number = index + 1
        title = os.path.splitext(file)[0].replace("_", " ").title()
        full_path = os.path.join(song_folder, file)
        if os.path.exists(full_path):
            with open(full_path, "rb") as f:
                st.markdown('<div class="spotify-row">', unsafe_allow_html=True)
                col1, col2, col3 = st.columns([1, 3, 1])
                with col1:
                    st.markdown(f'<div class="track-column">{track_number}</div>', unsafe_allow_html=True)
                with col2:
                    st.markdown(f'<div class="title-column">{title}</div>', unsafe_allow_html=True)
                with col3:
                    st.download_button(
                        label="Download",
                        data=f,
                        file_name=file,
                        mime="audio/mpeg",
                        key=f"song_{index}",
                        help=f"Download {title}"
                    )
                st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.markdown(
                f'<div class="spotify-row">'
                f'<div class="track-column">{track_number}</div>'
                f'<div class="title-column">{title}</div>'
                f'<div class="button-column">Not found</div>'
                f'</div>',
                unsafe_allow_html=True
            )
else:
    st.error("No songs found in the 'album' folder.")

st.markdown('<p class="footer">Presented by Imara Daima Pathfinder Club, The Saffrons © 2025</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)