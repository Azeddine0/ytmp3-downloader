# ytmp3-downloader

A minimalist Flask web application that allows users to download YouTube videos as MP3 audio files. The app uses `yt-dlp` for downloading and `ffmpeg` for audio conversion, with a clean dark-themed interface.

---

## Features

- Download audio from any YouTube video URL.
- Converts video audio to MP3 format.
- Names the downloaded MP3 file after the YouTube video title.
- Minimalist dark style frontend.
- Handles file locking issues on Windows.

---

## Requirements

- Python 3.8+
- [ffmpeg](https://ffmpeg.org/download.html) installed and accessible in your system PATH or specify its location in the app.
- Python packages listed in `requirements.txt`.

---

## Installation

A minimalist Flask web application that allows users to download YouTube videos as MP3 audio files. The app uses `yt-dlp` for downloading and `ffmpeg` for audio conversion, with a clean dark-themed interface.

---

## Features

- Download audio from any YouTube video URL.
- Converts video audio to MP3 format.
- Names the downloaded MP3 file after the YouTube video title.
- Minimalist dark style frontend.
- Handles file locking issues on Windows.

---

## Requirements

- Python 3.8 or higher
- [ffmpeg](https://ffmpeg.org/download.html) installed and accessible in your system PATH or specify its location in the app.
- Python packages listed in `requirements.txt`.

---

## Installation

1. Clone the repository or download the source code, then navigate into the project folder.

2. (Optional but recommended) Create and activate a virtual environment.

3. Install the Python dependencies listed in `requirements.txt`.

4. Install ffmpeg for your operating system by downloading it from the official site. Extract it and add the folder containing `ffmpeg` and `ffprobe` executables to your system PATH. Alternatively, specify the full path to this folder in `app.py` under the `ffmpeg_location` option.

5. Verify ffmpeg installation by running `ffmpeg -version` and `ffprobe -version` in your terminal or command prompt. You should see version information printed.

---

## Usage

1. Run the Flask application by executing `python app.py`.

2. Open your web browser and go to `http://127.0.0.1:5000/`.

3. Enter a YouTube video URL in the input box and click the "Download MP3" button.

4. The MP3 file will be downloaded with the YouTube video’s title as the filename.

---

## Project Structure

ytmp3-downloader/
│
├── app.py # Flask server application
├── requirements.txt # Python dependencies
├── templates/
│ └── index.html # Frontend HTML page
└── static/
└── style.css # Minimalist dark style CSS


---

## Notes

- The app uses temporary directories to store downloads and cleans up automatically.
- On Windows, file locking issues are handled by copying the MP3 file before sending.
- Ensure your ffmpeg installation is correct to avoid conversion errors.
- For production deployment, consider configuring Flask for production use and securing the app.
