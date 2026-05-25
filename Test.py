import yt_dlp

video_url = "https://youtu.be/OzXiL-QWUgc?si=IaFeLOhODyv5X2yS"

ydl_opts = {
    'cookiefile': 'cookies.txt',
    'cookiesfrombrowser': ('edge',),
    "ignoreerrors": True,
    "nocheckcertificate": True,
}

# List available formats
with yt_dlp.YoutubeDL() as ydl:
    info_dict = ydl.extract_info(video_url, download=False)
    formats = info_dict.get('formats', [])

    print("\nAvailable Formats:")
    for f in formats:
        print(f"{f['format_id']: <8} | {f['ext']: <4} | {f.get('resolution', 'audio')}")

# Now to download specific format (e.g., 136 for 720p)
