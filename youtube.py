from pytube import YouTube


url = "https://www.youtube.com/watch?v=EpsQx8JDIvI"
video = YouTube(url)
resol = "1080p"
file_type = "mp4"
path = 'e:/mov'

Streams = video.streams
vid = Streams.filter(progressive=True)
vid = Streams.filter(res=resol, file_extension=file_type).first()

vid.download(path)
