import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



data = pd.read_csv("/Users/charliegray/Downloads/Pearson Edexcel GCE AS and AL Mathematics data set (5).csv",sep='delimiter', header=None, encoding = "ISO-8859-1")

ignoredVal = ["n/a", "#n/a", "-", "na"]

length = 247-63

placesMap = [["CAMBORNE", 63, 1018], ["HEATHROW", 254, 1209], ["HURN", 445, 1400], ["LEEMING", 636, 1591], ["LEUCHARS", 827, 1782]]

def plot(collumn, placesMap, data, ignoredVal, length, increment):

    if collumn in [5, 12, 14]:
        return "not shown, data is qualitative"

    if not (0 < collumn < 14):
        return "not a viable collumn"

    yearInd = 0
    count = 1
    while yearInd < 2:

        for index in range(0, len(placesMap)):

            x = []
            y = []

            for i in range(0, length):

                val = data[0][placesMap[index][yearInd+1]+i+1].split(',')[collumn]

                if val.lower() in ignoredVal:
                    continue
                elif val.lower() == "tr":
                    x.append(i)
                    y.append(0.05)
                else:
                    x.append(i)
                    y.append(float(val))

            plt.subplot(3,4,count)
            year = "1987"
            if yearInd == 1:
                year = "2015"
            plt.title(f"{placesMap[index][0]} {year}")
            plt.plot(x, y)

            plt.yticks(np.arange(min(y), max(y), increment))
            count += 1
        yearInd += 1


    plt.suptitle(f"{data[0][placesMap[index][1]].split(',')[collumn]} VS days after 01/05")
    plt.show()
    return "shown"

params = [0, 1, 5, 2, 4, 0, 6, 5 ,1 ,1000, 10, 100, 0, 100, 0]

while True:
    inp = input("enter number 1 to 14 inclusive to view collumn, if END entered, program will halt")
    if inp == "END":
        break
    inp = int(inp)
    plot(inp, placesMap, data, ignoredVal, length, params[inp])