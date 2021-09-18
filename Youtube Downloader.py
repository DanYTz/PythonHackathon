from pytube import YouTube

url = input('Enter Youtube Url: ')
video = YouTube(url)

print('Video Title: ' + video.title)
confirm = input('is the url correct? (y/n):')

while confirm != 'y':
    url = input('Enter Youtube Url: ')

    print('Video Title: ' + video.title)
    confirm = input('is the url correct? (y/n):')

confirm2 = input('continue?(y/n): ')
while confirm2 != 'y':
    exit = input('Do you want to exit?(y/n): ')
    if exit == 'y':
        exit()
    else:
        confirm = input('is the url correct? (y/n):')
print('downloading......')
stream = video.streams.get_lowest_resolution()
stream.download()
