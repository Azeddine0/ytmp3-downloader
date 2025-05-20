import os
import tempfile
import shutil
from flask import Flask, render_template, request, send_file, redirect, url_for, flash
import yt_dlp

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        if not url:
            flash('Please enter a YouTube URL.', 'error')
            return redirect(url_for('index'))
        try:
            with tempfile.TemporaryDirectory() as tmpdir:
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'outtmpl': os.path.join(tmpdir, 'audio.%(ext)s'),
                    'quiet': True,
                    'no_warnings': True,
                    'ffmpeg_location': r'C:\Users\azeddine\Downloads\ffmpeg-2025-05-19-git-c55d65ac0a-essentials_build\ffmpeg-2025-05-19-git-c55d65ac0a-essentials_build\bin',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info_dict = ydl.extract_info(url, download=True)

                # Clean the title to be a safe filename
                title = info_dict.get('title', 'download').replace('/', '_').replace('\\', '_')

                files = os.listdir(tmpdir)
                mp3_file = next((os.path.join(tmpdir, f) for f in files if f.endswith('.mp3')), None)

                if not mp3_file:
                    flash('Failed to convert audio to mp3.', 'error')
                    return redirect(url_for('index'))

                # Copy to a new temp file to avoid file locking issues
                with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp_mp3:
                    shutil.copy(mp3_file, tmp_mp3.name)
                    temp_mp3_path = tmp_mp3.name

                return send_file(
                    temp_mp3_path,
                    as_attachment=True,
                    download_name=f"{title}.mp3",
                    mimetype='audio/mpeg'
                )
        except Exception as e:
            flash(f'Error: {str(e)}', 'error')
            return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)