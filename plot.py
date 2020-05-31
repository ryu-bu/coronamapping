import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import urllib.request, json
import numpy as np
from operator import itemgetter

class parseURL:
    
    def countries():
        with urllib.request.urlopen("https://api.covid19api.com/summary") as url:   
            countryURL = json.loads(url.read().decode())
            countryData = countryURL['Countries']

            countryData = sorted(countryData, key = itemgetter('TotalConfirmed'), reverse=True)
            
            x = []
            y = []

            count = 0

            for i in countryData:
                x.append(i['Country'])
                y.append(i['TotalConfirmed'])

                if (count == 49):
                    break

                count = count + 1
            title = "Total Confirmed Cases by Country"
            filename = "countryData"
            x_name = "Country"
            y_name = "Total Cases Confirmed"
            visualizeJson(x, y, x_name, y_name, title, filename)

            return countryData

    def states():
        with urllib.request.urlopen("https://covidtracking.com/api/states") as url:
            stateURL = json.loads(url.read().decode())

            stateData = sorted(stateURL, key = itemgetter('positive'), reverse = True)

            x = []
            y = []

            for i in stateData:
                x.append(i['state'])
                y.append(i['positive'])
            
            title = "Cases per State"
            filename = "stateData"
            x_name = "State"
            y_name = "Positive Cases"
            visualizeJson(x, y, x_name, y_name, title, filename)

            return stateData



def visualizeJson(x, y, x_name, y_name, title, filename):
    y_pos = np.arange(len(x))
    plt.figure(figsize=(25,20))
    plt.bar(y_pos, y, align='center', alpha=0.5)
    plt.xticks(y_pos, x)
    plt.axes().set_xticklabels(x, rotation = 90)
    plt.title(title)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    path = "./static/images/" + filename + ".png"
    plt.savefig(path)


        # plt.plot([0, 1, 2, 3, 4], [0, 3, 5, 9, 11])

        # plt.xlabel('Months')
        # plt.ylabel('Books Read')

        # plt.savefig("./static/images/test.png")
    

