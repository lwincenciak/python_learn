# Import the necessary libraries
from pytube import YouTube

# Create a YouTube object by specifying the URL of the video
url = 'https://www.youtube.com/watch?v=VMO3YNoNyTY'
yt = YouTube(url)
resol = '1080p'
file_type = 'mp4'
v_path = 'E:/Mov/yt/'


# Print the video title and length
print(f"Title: {yt.title}")
print(f"Length: {yt.length} seconds")

# Specify the video stream that you want to download
stream = yt.streams.filter(res=resol, file_extension=file_type).first()
stream.download(output_path=v_path)
