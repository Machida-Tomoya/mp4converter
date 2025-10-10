import yt_dlp #リンク先動画の対応フォーマット確認

url = "https://youtu.be/6sDgjJSoAyY"

with yt_dlp.YoutubeDL({'listformats': True}) as ydl:
    ydl.download([url])
