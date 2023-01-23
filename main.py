import csv
with open("timeStamps.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    print(row[0])
