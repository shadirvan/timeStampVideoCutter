from pytube import YouTube
from moviepy.editor import *
import csv

    
    




# def Download(link):
#     youtubeObject = YouTube(link)
#     print("Please wait while the file is downloaded....")
#     youtubeObject = youtubeObject.streams.get_highest_resolution()
#     try:
#         youtubeObject.download(filename="full.mp4")
#     except:
#         print("Download Failed !")
#     print("Download completed successfully")

with open("timeStamps.csv", 'r') as file:
  csvreader = csv.reader(file)
  timeList = []
  for row in csvreader:
    hour = int(row[0][0:2]) * 3600
    minute = int(row[0][3:5]) * 60
    second = int(row[0][6:8]) 
    timeInSec = hour + minute + second
    timeList.append(timeInSec)


    


def CutVideo(initialTime, finalTime):
    # loading video gfg
    clip = VideoFileClip("full.mp4")
    # getting only first 5 seconds
    clip = clip.subclip(initialTime, finalTime)
    # showing clip
    clip.write_videofile("clip.mp4")


# link = input("Enter the YouTube video URL: ")
# Download(link)

