import yt_dlp

video_url = "https://youtu.be/OzXiL-QWUgc?si=IaFeLOhODyv5X2yS"

ydl_opts = {
    "ignoreerrors": True,
    "nocheckcertificate": True,
}

# Now to download specific format (e.g., 136 for 720p)
ydl_opts = {
    'format': '140',  # 720p video + audio
    'outtmpl': '%(title)s.%(ext)s'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])
