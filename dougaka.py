import yt_dlp

url='https://youtu.be/6sDgjJSoAyY' #変換したい動画のリンク

ydl_opts={
    'format':'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',
    'merge_output_format':'mp4',
    'outtmpl':r'C:\Users\admin\Videos\movie\%(title)s.%(ext)s', #コンピュータの保存先を指定
    'ffmpeg_location':'ffmpeg.exe',
    'continuedl':True
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url]) 