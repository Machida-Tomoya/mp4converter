import yt_dlp

playlist_url = "https://youtube.com/playlist?list=PLjocbGlrxCdSc9gNF3uJWI5ERSJnaGn5o&si=wtZRRrvSTntCAX_Y"

download_path = r"C:\Users\moroz\Videos\mp4\%(title)s.%(ext)s"

ydl_opts = {
    'format': 'bestvideo[height<=1080]+bestaudio[ext=m4a]/best',
    'outtmpl': download_path,
    'merge_output_format': 'mp4',
    'sleep_interval': 10,
    'max_sleep_interval': 20,
    'retries': 10,
    'fragment_retries': 10,
    'http_chunk_size': 4 * 1024 * 1024,  # ← 4MBをバイト単位で指定（整数）
    # 'ffmpeg_location': 'ffmpeg.exe',
    'nooverwrites': True,
    'continuedl': True,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])
