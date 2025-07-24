import os
from pytubefix import YouTube
from moviepy.editor import AudioFileClip

urls = [
    "https://youtu.be/K8JoYyGCGgQ",
    "https://youtu.be/3JZ_D3ELwOQ",
    ]

directory = rf"{os.path.dirname(os.path.abspath(__file__))}/downloaded-audio"
if not os.path.exists(directory):
    os.makedirs(directory)

def download_youtube_audio(url, output_path="."):
    try:
        # Use Google's OATH for authentication, uses your own personal account in a browser window
        youtube = YouTube(url, use_oauth=True, allow_oauth_cache=True)
        audio_stream = youtube.streams.filter(only_audio=True).order_by('abr').desc().first()
        
        if not audio_stream:
            print("No audio stream found for this video.")
            return

        print(f"Downloading: {youtube.title}...")
        download_path = audio_stream.download(output_path=output_path)
        base_name = os.path.splitext(os.path.basename(download_path))[0]

        # Convert to OGG format using moviepy
        audio_filename = f"{base_name}.ogg"
        audio = AudioFileClip(download_path)
        audio.write_audiofile(audio_filename)

        # Clean up
        os.remove(download_path)
        os.rename(audio_filename, os.path.join(directory, audio_filename))
        
        print(f"Download complete! Saved as: {audio_filename}")
        
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    for url in urls:
        download_youtube_audio(url, output_path=directory)

    print("Download and conversion completed.")