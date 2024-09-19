import random
import csv
with open('occupations.csv', "r") as file:
    csvFile = csv.reader(file)
    info = {}
    count = 0
    for lines in csvFile:
        if not(count == 0):
            info.update({lines[0]:float(lines[1])})
        count = count + 1
    info.popitem()
def randomJob():
    random.randint(0,9980)