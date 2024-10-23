import yt_dlp

def download_youtube_audio(url, output_format="mp3"):
    """
    Downloads audio from a YouTube video using yt-dlp.

    Args:
        url (str): The URL of the YouTube video.
        output_format (str, optional): The desired output format (e.g., 'mp3', 'wav', 'ogg'). Defaults to 'mp3'.

    Returns:
        str: The path to the downloaded audio file.
    """

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'extract_audio': True,
        'audioformat': output_format,
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        return info_dict['filepath']
    
youtube_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
audio_file = download_youtube_audio(youtube_url, output_format="wav")

print(f"Audio downloaded to: {audio_file}")