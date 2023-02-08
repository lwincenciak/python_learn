from pytube import YouTube

path = 'e:/mov'
url = "https://www.youtube.com/watch?v=EpsQx8JDIvI"
resol = "1080p"
file_type = "mp4"

video = YouTube(url)
Streams = video.streams
vid = Streams.filter(progressive=True)
vid = Streams.filter(res=resol, file_extension=file_type).first()

vid.download(path)
