from pytube import YouTube

url = input('Enter Youtube Url: ')
video = YouTube(url)

print('Video Title: ' + video.title)