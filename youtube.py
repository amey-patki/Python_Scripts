import pytube

from pytube import YouTube

link = input("https://www.youtube.com/watch?v=6zUp3C4AzHU") # i.e. https://youtu.be/dQw4w9WgXcQ

yt = Youtube(link)
yt.streams.first().download()

print("downloaded", link)