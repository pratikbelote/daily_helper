from pytube import YouTube
from sys import argv
try:
    # url = input("Enter the YouTube URL: ")
    link = argv[1]
    
    yt = YouTube(link)
    
    print("Title:", yt.title)
    print("Views:", yt.views)

    yd = yt.streams.get_lowest_resolution()
    
    yd.download('/Users/PANKAJ BELOTE/Desktop')
    
    print("Download complete.")
except Exception as e:
    print("An error occurred:", str(e))