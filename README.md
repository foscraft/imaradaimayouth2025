# Siondoki Album Launch App

## Overview
The **Siondoki Album Launch App** is a simple, user-friendly web application built with Streamlit to promote and distribute the "Siondoki" music album by the Adventist Youth Choir, Imara Daima. The app allows users to view the album cover, scan or download a QR code to access the download page, and download individual songs or the full album in a Spotify-like table format.

## Features
- **Home Page**:
  - Displays the album cover and a QR code linking to the download page.
  - Includes a button to download the QR code as an image.
  - Branded with the choir's name and album launch details.
- **Download Page**:
  - Presents a table listing songs with track numbers, titles, and download buttons, styled like a Spotify track list.
  - Offers a button to download the full album as a ZIP file.
  - Shows error messages if files are missing.
- **Navigation**:
  - Sidebar with links to "Home" and "Download The Siondoki Album" pages.
  - Supports URL query parameters (e.g., `?page=download`) for direct access to the download page.

## Prerequisites
- **Python 3.8+**
- **Dependencies**:
  - Install required packages:
    ```bash
    pip install streamlit qrcode pillow
    ```
- **File Structure**:
  - Place the following files in an `album/` folder in the same directory as the app script (`imaradaima.py`):
    - `cover.jpg`: Album cover image.
    - `.mp3` files (e.g., `amenikomboa.mp3`): Individual songs.
    - `siondoki_album.zip`: Full album archive.
  - Example:
    ```
    project_folder/
    ├── imaradaima.py
    ├── album/
    │   ├── cover.jpg
    │   ├── amenikomboa.mp3
    │   ├── siondoki_album.zip
    ```

## Installation
1. Clone or download the project files.
2. Install dependencies:
   ```bash
   pip install streamlit qrcode pillow

   ```
Ensure the `album/` folder contains the required files (see File Structure).

## Running the App Locally
Navigate to the project directory:
```bash
cd path/to/project_folder

```

Run the Streamlit app:
bash

streamlit run imaradaima.py

Open http://0.0.0.0:4009 in your browser.
Deployment
To make the QR code scannable on any device:
Deploy the app to a public server (e.g., Streamlit Community Cloud):
Push the project to a GitHub repository.

Sign in to share.streamlit.io and deploy the app.

Note the public URL (e.g., https://siondoki-album.streamlit.app).

Update the download_page_url in imaradaima.py to:
python

download_page_url = "https://siondoki-album.streamlit.app/?page=download"

Redeploy the app.

Usage
Home Page: View the album cover, scan the QR code, or download it to access the download page.

Download Page: Browse the song list in a table, click "Download" next to each song to get the .mp3 file, or click "Download Full Album" for the .zip file.

Navigation: Use the sidebar or QR code to switch between pages.

Troubleshooting
Table Not Displaying: Ensure .mp3 files are in album/. Check browser cache or try a different browser.

QR Code Not Redirecting: For local testing, use http://127.0.0.1:4009/?page=download in a browser. For scanning, deploy the app and update download_page_url.

Missing Files: Verify album/ contains cover.jpg, .mp3 files, and siondoki_album.zip. Error messages will indicate missing files.

