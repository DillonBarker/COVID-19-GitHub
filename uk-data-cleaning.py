# imports
from typing import Any, Union

import pandas as pd

# loading the data
# daily indicators
from pandas import DataFrame, Series
from pandas.io.parsers import TextFileReader

url = "https://www.arcgis.com/sharing/rest/content/items/bc8ee90225644ef7a6f4dd1b13ea1d67/data"
dailyindicators = pd.read_excel(url)


# daily confirmed cases
url = "https://www.arcgis.com/sharing/rest/content/items/e5fd11150d274bebaaf8fe2a7a2bda11/data"
confirmedcases = pd.read_excel(url)


# NHSR cases table
url = "https://www.arcgis.com/sharing/rest/content/items/ca796627a2294c51926865748c4a56e8/data"
NHSRcasestable = pd.read_csv(url)
NHSRcasestable = NHSRcasestable.drop(columns="GSS_CD")


# adding a coordinate column for each region (lat, long)
Latitude = ['51.279999', '51.509865', '52.489471', '53.958332', '53.483959', '50.827778	', '50.259998']
Longitude = ['1.080000', '-0.118092', '-1.898575', '-1.080278', '-2.244644', '-0.152778', '-5.051000']
NHSRcasestable['Latitude'] = Latitude
NHSRcasestable['Longitude'] = Longitude

# CountyUAs cases table
url = "https://www.arcgis.com/sharing/rest/content/items/b684319181f94875a6879bbc833ca3a6/data"
CountyUAsCasesTable = pd.read_csv(url)
CountyUAsCasesTable = CountyUAsCasesTable.drop(columns="GSS_CD")


# save all files to csv for access by qlikview
dailyindicators.to_csv('C:/Users/barke/Dropbox/Coding/PycharmProjects/UK-COVID-19/data/dailyindicators.csv')
confirmedcases.to_csv('C:/Users/barke/Dropbox/Coding/PycharmProjects/UK-COVID-19/data/confirmedcases.csv')
NHSRcasestable.to_csv('C:/Users/barke/Dropbox/Coding/PycharmProjects/UK-COVID-19/data/NHSRcasestable.csv')
CountyUAsCasesTable.to_csv('C:/Users/barke/Dropbox/Coding/PycharmProjects/UK-COVID-19/data/CountyUAsCasesTable.csv')

