import streamlit as st
import qrcode
from PIL import Image
import os

# App configuration
st.set_page_config(
    page_title="Siondoki Album Launch by Imara Daima Youth Choir",
    page_icon="🎵",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS for Spotify-like table and consistent styling
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
        padding: 12px;
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
    </style>
""", unsafe_allow_html=True)

# Helper to generate QR code
def generate_qr_code(url):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr_code.png")
    return "qr_code.png"

# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Download The Siondoki Album"])

# Handle query params
query_params = st.query_params
if "page" in query_params and query_params["page"] == "download":
    page = "Download The Siondoki Album"

# Pages
if page == "Home":
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown('<h3 class="title">Siondoki Album by Adventist Youth Choir, Imara Daima</h3>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Scan or download the QR code to access our music album, launching June 1st!</p>', unsafe_allow_html=True)

    # Generate and show QR code
    download_page_url = "http://127.0.0.1:4009/?page=download"  # Update for deployment
    qr_code_path = generate_qr_code(download_page_url)
    qr_image = Image.open(qr_code_path)

    # Show album cover and QR code side by side
    col1, col2 = st.columns(2)
    with col1:
        if os.path.exists("album/cover.jpg"):
            st.image("album/cover.jpg", caption="Album Cover", use_container_width=True)
        else:
            st.error("Album cover not found at 'album/cover.jpg'.")
    with col2:
        st.image(qr_image, caption="Scan to download the Siondoki Album", use_container_width=True)

    # QR Code Download Button
    with open(qr_code_path, "rb") as file:
        st.download_button(
            label="Download QR Code",
            data=file,
            file_name="siondoki_qr_code.png",
            mime="image/png",
            key="qr_download"
        )

    st.markdown('<p class="footer">Presented by Imara Daima Youth Choir © 2025</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "Download The Siondoki Album":
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown('<h3 class="title">Download The Siondoki Album</h3>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Click to download songs or the full album.</p>', unsafe_allow_html=True)

    # List songs in a table-like layout
    song_folder = "album"
    mp3_files = [f for f in os.listdir(song_folder) if f.endswith(".mp3")]

    st.markdown("### Song List")
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
                    # Create row with track number, title, and button
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

    # Full album download
    st.markdown("### Full Album")
    album_file = os.path.join(song_folder, "siondoki_album.zip")
    if os.path.exists(album_file):
        with open(album_file, "rb") as f:
            st.download_button(
                label="Download Full Album",
                data=f,
                file_name="siondoki_album.zip",
                mime="application/zip",
                key="full_album"
            )
    else:
        st.error("Error: Full album not found at 'album/siondoki_album.zip'.")

    st.markdown('<p class="footer">Presented by Imara Daima Youth Choir © 2025</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)