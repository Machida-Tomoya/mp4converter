import yt_dlp

url='https://youtu.be/6sDgjJSoAyY'

ydl_opts={
    'format':'bestvideo+bestaudio/best',
    'merge_output_format':'mp4',
    'outtmpl':r'C:\Users\moroz\Videos\mp4\%(title)s.%(ext)s',
    'ffmpeg_location':'ffmpeg.exe',
    'continuedl':True
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url]) 