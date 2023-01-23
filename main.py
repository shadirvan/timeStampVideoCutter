from pytube import YouTube
import csv
with open("timeStamps.csv", 'r') as file:
  csvreader = csv.reader(file)
#   for row in csvreader:
#     print(row[0])




def Download(link):
    youtubeObject = YouTube(link)
    print("Please wait while the file is downloaded....")
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("Download Failed !")
    print("Download completed successfully")


link = input("Enter the YouTube video URL: ")
Download(link)
