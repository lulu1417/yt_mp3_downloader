from pytube import YouTube
from moviepy.editor import VideoFileClip
import os

youtube_url = input("please enter the youtube url：")
yt = YouTube(youtube_url)

print("please enter the path you want to store your file：")
print("1. Pop")
print("2. For study")
print("3. Radio")
choice = input("enter the number：")

if choice == "1":
    path = "Pop"
    print("pop music.")
elif choice == "2":
    path = "For study"
    print("music for study")
elif choice == "3":
    path = "Radio"
    print("Radio")
else:
    print("invalid choice")
    exit(1)


video_stream = yt.streams.get_highest_resolution()

video_stream.download(filename='temp_video.mp4')

video_path = 'temp_video.mp4'
yt = YouTube(youtube_url)
audio_path = '/Users/abao/Desktop/Music/{}/'.format(path) + yt.title + '.mp3'

video = VideoFileClip(video_path)

video.audio.write_audiofile(audio_path)

video.close()

if os.path.exists(video_path):
    os.remove(video_path)