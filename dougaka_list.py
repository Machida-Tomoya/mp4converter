import yt_dlp

playlist_url = 'https://www.youtube.com/watch?v=uagHwzRxV6I&list=PLjocbGlrxCdStTf4bU_yxnnQTR0K1zRSW&pp=gAQB'

ydl_opts = {
    'format': 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best',
    'merge_output_format': 'mp4',
    'outtmpl': r'C:\Users\admin\Videos\movie\%(playlist_title)s\%(playlist_index)s - %(title)s.%(ext)s',
    'ffmpeg_location': 'ffmpeg.exe',
    'sleep_interval': 10,
    'max_sleep_interval': 20,
    'nooverwrites': True,
    'continuedl': True,
    'concurrent_fragment_downloads': 10,
    'retries': 10,
    'fragment_retries': 10,
    'http_chunk_size': 4 * 1024 * 1024,
    'throttled-rate': 0,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])
