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

            #generate plot for country vs total confirmed cases
            
            x = []
            y = []

            y_rate = []

            count = 0

            for i in countryData:
                x.append(i['Country'])
                y.append(i['TotalConfirmed'])

                y_rate.append((i['TotalDeaths'] / i['TotalConfirmed'])*100)

                if (count == 49):
                    break

                count = count + 1
            title = "Total Confirmed Cases by Country"
            filename = "countryData"
            x_name = "Country"
            y_name = "Total Cases Confirmed"
            visualizeJson(x, y, x_name, y_name, title, filename)

            #generate plot for country vs death rate
            
            for j in range(len(y_rate)-1):
                maxRate = j 
                for z in range(j, len(y_rate)):
                    if (y_rate[z] > y_rate[maxRate]):
                        maxRate = z 
                temp = y_rate[j]
                temp_x = x[j]
                y_rate[j] = y_rate[maxRate]
                x[j] = x[maxRate]
                y_rate[maxRate] = temp
                x[maxRate] = temp_x


            title = "Total Deaths / Total Positives in %"
            filename = "rateCountry"
            y_name = "Rate (%)"
            visualizeJson(x, y_rate, x_name, y_name, title, filename)  
            
            return countryData

    def states():
        with urllib.request.urlopen("https://covidtracking.com/api/states") as url:
            stateURL = json.loads(url.read().decode())

            stateData = sorted(stateURL, key = itemgetter('positive'), reverse = True)

            x = []
            y = []

            y_rate = []

            x_infection = []
            y_infection = []

            for i in stateData:
                x.append(i['state'])
                x_infection.append(i['state'])
                y.append(i['positive'])

                if (i['positive'] == 0):
                    y_rate.append(0)
                    y_infection.append(0)
                else:
                    y_rate.append((i['death'] / i['positive']) * 100)
                    y_infection.append((i['positive'] / i['totalTestResults']) * 100)
            
            title = "Cases per State"
            filename = "stateData"
            x_name = "State"
            y_name = "Positive Cases"
            visualizeJson(x, y, x_name, y_name, title, filename)

            #death rate

            for j in range(len(y_rate)-1):
                maxRate = j 
                for z in range(j, len(y_rate)):
                    if (y_rate[z] > y_rate[maxRate]):
                        maxRate = z 
                temp = y_rate[j]
                temp_x = x[j]
                y_rate[j] = y_rate[maxRate]
                x[j] = x[maxRate]
                y_rate[maxRate] = temp
                x[maxRate] = temp_x

            title = "Total Deaths / Total Positives in %"
            filename = "rateState"
            y_name = "Rate (%)"
            visualizeJson(x, y_rate, x_name, y_name, title, filename)  

            #infection rate


            for j in range(len(y_infection)-1):
                maxRate = j 
                for z in range(j, len(y_infection)):
                    if (y_infection[z] > y_infection[maxRate]):
                        maxRate = z 
                temp = y_infection[j]
                temp_x = x_infection[j]
                y_infection[j] = y_infection[maxRate]
                x_infection[j] = x_infection[maxRate]
                y_infection[maxRate] = temp
                x_infection[maxRate] = temp_x


            title = "Total Positives / Total Tests in %"
            filename = "rateInfectionState"
            y_name = "Rate (%)"
            visualizeJson(x_infection, y_infection, x_name, y_name, title, filename)  

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
    

