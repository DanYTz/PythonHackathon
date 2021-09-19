from pytube import YouTube

url = input('Enter Youtube Url: ')  # variable to receive the Youtube Url
video = YouTube(url)  # this variable to convert the url to video

print('Video Title: ' + video.title)  # to show the video title
confirm = input('Is the url correct? (y/n):')  # to make sure the url is correct based on video's title

# if user say no
while confirm != 'y':
    url = input('Enter Youtube Url: ')  # ask the user reenter the url

    print('Video Title: ' + video.title)  # to show the video title
    confirm = input('Is the url correct? (y/n):')  # to make sure the url is correct based on video's title

# to choose the video resolution
print('Choose the video resolution:')  #
print('Please wait loading.............')
for i in video.streams.filter(audio_codec = 'mp4a.40.2'):  
    print(str(i.resolution))  # to show the list of available resolution
res = input("e.g.(360p) (note: resolution 720p and higher doesn't support audio. Please choose lower resolution): ")  # ask the user to enter the resolution based on the given resolution in the previous line
stream = video.streams.filter(
    res=res, audio_codec = 'mp4a.40.2').first()  # change the video  resolution based on what the user type in the previous line

# to show all the setting and information about the video
print()
print('Title: ' + video.title)  # video title
print('Resolution: ' + res)  # video resolution


# to confirm before proceed
confirm2 = input('Continue?(y/n): ')  # ask the user to continue

# if the user say no
while confirm2 != 'y':
    stop_all = input('Do you want to exit?(y/n): ')  # ask if the user want to exit the program
    if stop_all == 'y':
        exit()
    else:
        confirm2 = input('Continue?(y/n): ')  # if the user don't want to exit, ask the user to proceed
print()
print('Downloading......')

stream.download()  # start downloading
print()
print('Download Completed')