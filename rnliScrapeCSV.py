#A program that data scrapes a table from wikipedia saves to .csv and outputs to html
#and downloads a csv from RNLI data repository saves and outputs to html 
########################################################################################

import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv


#Use Beautiful Soup to get data
#Adapted from Andrew Beatty lectures
def getStations():
    url = 'https://en.wikipedia.org/wiki/List_of_RNLI_stations'
    page = requests.get(url)
    soup =BeautifulSoup(page.text, 'html.parser')

    stations = open('./Data/locations.csv', mode='w', newline = "")
    writer = csv.writer(stations, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)

    table1 = soup.find('table')

    headers = []
    for i in table1.find_all('th'):
        title = i.text
        headers.append(title.strip())

    #write the header
    writer.writerow(headers)    

    rows = soup.findAll("tr")
    for row in rows:
        cols = row.findAll('td')

        dataList = []
        for col in cols:
            dataList.append(col.text.strip())
        
        #write the data
        writer.writerow(dataList)

    stations.close()

    station = pd.read_csv('./Data/locations.csv', encoding = 'unicode_escape') 
    # to save as html file
    station.to_html("./rnlipages/locations.html") 
    # assign it to a variable (string)
    html_file = station.to_html()

########################################################################################################################
########################################################################################################################

#Download csv straight from data source and save
def getFleet():
    req = requests.get('https://data-rnli.opendata.arcgis.com/datasets/e3c369859c8b490a80d30c54d803e3a1_0.csv')
    url_content = req.content
    csv_file = open('./Data/fleet.csv', 'wb')

    csv_file.write(url_content)
    csv_file.close()

    #to read csv file"
    fleet = pd.read_csv('./Data/fleet.csv') 
    #to save as html file
    fleet.to_html("./rnlipages/fleet.html") 
    #assign it to a variable (string)
    html_file = fleet.to_html()



    
    
    



