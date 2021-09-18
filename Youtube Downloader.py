from pytube import YouTube


url = input('Enter Youtube Url: ') #variable to receive the Youtube Url
video = YouTube(url)

print('Video Title: ' + video.title)
confirm = input('Is the url correct? (y/n):')


while confirm != 'y':
    url = input('Enter Youtube Url: ')

    print('Video Title: ' + video.title)
    confirm = input('Is the url correct? (y/n):')

print('Choose the video resolution:')
print('Please wait loading.............')
for i in video.streams: print(str(i.resolution))
res = input("e.g.(1080p): ")
stream = video.streams.filter(res=res).first()
print()
print('Title: '+ video.title)
print('Resolution: ' + res)
print("File Size: " + str(round(stream.filesize / 1000000, 2)) + 'MB')

confirm2 = input('Continue?(y/n): ')
while confirm2 != 'y':
    exit = input('Do you want to exit?(y/n): ')
    if exit == 'y':
        quit()
    else:
        confirm2 = input('Continue?(y/n): ')
print()
print('Downloading......')

stream.download()
print()
print('Download Completed')
