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
  nameList =[]
  for row in csvreader:
    hour = int(row[0][0:2]) * 3600
    minute = int(row[0][3:5]) * 60
    second = int(row[0][6:8]) 
    timeInSec = hour + minute + second
    timeList.append(timeInSec)
    nameList.append(row[1])

link = input("Enter the YouTube video URL: ")
# Download(link)

def CutVideo(initialTime, finalTime, fileName):
   clip = VideoFileClip("full.mp4")
   clip = clip.subclip(initialTime, finalTime)
   
   clip.write_videofile(str(fileName) + ".mp4")

clip = VideoFileClip("full.mp4")
timeList.append(clip.duration)

for i in range(0,len(timeList)-1):
    CutVideo(timeList[i],timeList[i+1],nameList[i])

    
print("Video Cutting Succesfull")