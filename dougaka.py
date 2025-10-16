import yt_dlp

url='https://youtu.be/tDO3ymjTvqc' #変換したい動画のリンク

ydl_opts={
    'format':'bestvideo[height<=1080]+bestaudio[ext=m4a]/best',
    'merge_output_format':'mp4',
    'outtmpl':r'C:\Users\admin\Videos\movie\%(title)s.%(ext)s', #mp4の保存先を指定
    'ffmpeg_location':'ffmpeg.exe',
    'continuedl':True ,
    'concurrent_fragment_downloads': 10,
    'retries':10 ,
    'throttled-rate':0,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url]) 