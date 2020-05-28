import tabula 
import requests
import csv

#usage example: scrape_town_data('may-20-2020')
def scrape_town_data(cur_date: str) -> None:
    url: str = "https://www.mass.gov/doc/confirmed-covid-19-cases-in-ma-by-citytown-january-1-2020-"+cur_date+"/download"

    payload = {}
    headers = {
    'Cookie': '__cfduid=d42282119f860dd279a7c3d8cfd3e5a241590436327'
    }

    response: requests.request = requests.request("GET", url, headers=headers, data = payload)
    with open('data_downloads/cur_data.pdf', 'wb') as f:
        f.write(response.content)


    file: str = "data_downloads/cur_data.pdf"

    tabula.convert_into(file, 'town_data/data.csv', pages='all')

def get_town_list() -> [[str]]:
    #This needs to be updated weekly to get the latest info
    data_list: [str] = []
    with open('town_data/data.csv', newline='') as csvfile:
        data_reader: csv.reader = csv.reader(csvfile)
        for row in data_reader:
            temp_row: [str] = row[0:3]
            if '' not in temp_row:
                data_list.append(temp_row)
    return data_list
