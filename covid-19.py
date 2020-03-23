import pandas as pd
import seaborn as sns
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon
from IPython.display import display

#load dataset
data = pd.read_csv("data/coronavirus_data.csv")
display(data.head()); print('')
display(data.columns); print('')
display(data.columns.str.replace(r'\n','', regex=True))
data.columns = data.columns.str.replace(r'\n','', regex=True)
display(data.columns); print('')
data.rename(columns={'Province/State':'Province_State','Country/Region':'Country_Region'},inplace=True)
display(data.columns); print('')
#shape of dataset
display(data.shape); print('')
#datatypes
display(data.dtypes); print('')
#first 10 rows
display(data.head(10)); print('')
data = data[['Province_State', 'Country_Region', 'Lat', 'Long', 'Date',
       'Confirmed', 'Deaths', 'Recovered']]

#detecting missing values
display(data.isna().sum()); print('')
display(data.describe()); print('')

#number of case per date/day
display(data.head()); print('')
display(data.columns); print('')
display(data.groupby('Date')['Confirmed','Deaths', 'Recovered'].sum()); print('')
display(data.groupby('Date')['Confirmed','Deaths', 'Recovered'].max()); print('')

data_per_day = data.groupby('Date')['Confirmed','Deaths', 'Recovered'].max()
display(data_per_day.head()); print('')
display(data_per_day.describe()); print('')

#max no of cases
display(data_per_day['Confirmed'].max()); print('')
#min no of cases
display(data_per_day['Confirmed'].min()); print('')
#date for max number cases
display(data_per_day['Confirmed'].idxmax()); print('')
#date for min number cases
display(data_per_day['Confirmed'].idxmin()); print('')

#number of case per country
display(data.groupby(['Country_Region'])['Confirmed','Deaths', 'Recovered'].max()); print('')
#number of case per province/country
display(data.groupby(['Province_State','Country_Region'])['Confirmed','Deaths', 'Recovered'].max()); print('')
display(data['Country_Region'].value_counts()); print('')

data1 = data['Country_Region'].value_counts().plot(color='red',edgecolor='black',kind='bar',figsize=(20,10))
data1.tick_params(axis='x', colors='red')
data1.tick_params(axis='y', colors='red')
data1.set_facecolor('black')
plt.show()
plt.savefig('./plot/pic/countrys_aff1.png')
plt.savefig('./plot/pdf/countrys_aff1.pdf')

#how many aountry affect(number)
display(len(data['Country_Region'].unique())); print('')
#how many aountry affect(names)
display(data['Country_Region'].unique()); print('')

plt.figure(figsize=(20,10))
data['Country_Region'].value_counts().plot.pie(autopct="%1.1f%%")
plt.show()
plt.savefig('./plot/pic/countrys_aff2.png')
plt.savefig('./plot/pdf/countrys_aff2.pdf')

display(dir(gpd)); print('')
display(data.head()); print('')

#convert data to geodataframe
geodata = gpd.GeoDataFrame(data,geometry=gpd.points_from_xy(data['Long'],data['Lat']))
display(geodata.head()); print('')
display(type(geodata)); print('')
#map_plot
geodata1 = geodata.plot(color='red',edgecolor='black',figsize=(20,10))
geodata1.tick_params(axis='x', colors='red')
geodata1.tick_params(axis='y', colors='red')
geodata1.set_facecolor('black')
plt.show()
plt.savefig('./plot/pic/aff_pl.png')
plt.savefig('./plot/pdf/aff_pl.pdf')

#overlapping with world map
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
ax = world.plot(color='black',edgecolor='red',figsize=(20,10))
ax.tick_params(axis='x', colors='red')
ax.tick_params(axis='y', colors='red')
ax.axis('off')
plt.show()
plt.savefig('./plot/pic/world_geo.png')
plt.savefig('./plot/pdf/world_geo.pdf')

#overlap
fig,ax = plt.subplots(figsize=(20,10))
geodata.plot(cmap='Purples',ax=ax)
world1 = world.geometry.boundary.plot(color=None,edgecolor='red',linewidth=2,ax=ax)
world1.tick_params(axis='x', colors='red')
world1.tick_params(axis='y', colors='red')
world1.set_facecolor('black')
plt.show()
plt.savefig('./plot/pic/world_geo_aff.png')
plt.savefig('./plot/pdf/world_geo_aff.pdf')

#getting geographic regions
display(world['continent'].unique())
#spliting regions
Asia = world[world['continent'] == 'Asia']#display(Asia.head())
Africa = world[world['continent'] == 'Africa']#display(Africa.head())
North_america = world[world['continent'] == 'North America']#display(North_america.head())
Europe = world[world['continent'] == 'Europe']#display(Europe.head())

#ploting affected countrys
#mainland_china
fig,ax = plt.subplots(figsize = (20,10))
geodata[geodata['Country_Region'] == 'Mainland China'].plot(cmap = 'Purples',ax=ax)
mainland_china = Asia.geometry.boundary.plot(color=None,edgecolor='red',linewidth=2,ax = ax)
mainland_china.tick_params(axis='x', colors='red')
mainland_china.tick_params(axis='y', colors='red')
mainland_china.set_facecolor('black')
plt.show()
plt.savefig('./plot/pic/countrys/mainland_china.png')
plt.savefig('./plot/pdf/mainland_china.pdf')
#thailand
fig,ax = plt.subplots(figsize = (20,10))
geodata[geodata['Country_Region'] == 'Thailand'].plot(cmap = 'Purples',ax=ax)
thailand = Asia.geometry.boundary.plot(color=None,edgecolor='red',linewidth=2,ax = ax)
thailand.tick_params(axis='x', colors='red')
thailand.tick_params(axis='y', colors='red')
thailand.set_facecolor('black')
plt.show()
plt.savefig('./plot/pic/countrys/thailand.png')
plt.savefig('./plot/pdf/thailand.pdf')
#us
fig,ax = plt.subplots(figsize = (20,10))
geodata[geodata['Country_Region'] == 'US'].plot(cmap = 'Purples',ax=ax)
us = Asia.geometry.boundary.plot(color=None,edgecolor='red',linewidth=2,ax = ax)
us.tick_params(axis='x', colors='red')
us.tick_params(axis='y', colors='red')
us.set_facecolor('black')
plt.show()
plt.savefig('./plot/pic/countrys/us.png')
plt.savefig('./plot/pdf/us.pdf')
#uk
fig,ax = plt.subplots(figsize = (20,10))
geodata[geodata['Country_Region'] == 'UK'].plot(cmap = 'Purples',ax=ax)
uk = Asia.geometry.boundary.plot(color=None,edgecolor='red',linewidth=2,ax = ax)
uk.tick_params(axis='x', colors='red')
uk.tick_params(axis='y', colors='red')
uk.set_facecolor('black')
plt.show()
plt.savefig('./plot/pic/countrys/uk.png')
plt.savefig('./plot/pdf/uk.pdf')
#egypt
fig,ax = plt.subplots(figsize = (20,10))
geodata[geodata['Country_Region'] == 'Egypt'].plot(cmap = 'Purples',ax=ax)
egypt = Asia.geometry.boundary.plot(color=None,edgecolor='red',linewidth=2,ax = ax)
egypt.tick_params(axis='x', colors='red')
egypt.tick_params(axis='y', colors='red')
egypt.set_facecolor('black')
plt.show()
plt.savefig('./plot/pic/countrys/egypt.png')
plt.savefig('./plot/pdf/egypt.pdf')
#france
fig,ax = plt.subplots(figsize = (20,10))
geodata[geodata['Country_Region'] == 'France'].plot(cmap = 'Purples',ax=ax)
france = Asia.geometry.boundary.plot(color=None,edgecolor='red',linewidth=2,ax = ax)
france.tick_params(axis='x', colors='red')
france.tick_params(axis='y', colors='red')
france.set_facecolor('black')
plt.show()
plt.savefig('./plot/pic/countrys/france.png')
plt.savefig('./plot/pdf/france.pdf')

#analizing covid-19
display(data.head()); print('')
display(data_per_day.head()); print('')

#copying covid-19 data
data2 = data
data['cases_date'] = pd.to_datetime(data2['Date'])
display(data); print('')
data['cases_date'].plot()
plt.show()

#cases by date
cd = data2.set_index('cases_date')
display(cd.loc['2020-01'])
cd2 = cd.loc['2020-01-24' :'2020-02-25'][['Confirmed','Recovered']].plot(color=None,kind ='line',figsize= (20,10))
cd2.tick_params(axis='x', colors='red')
cd2.tick_params(axis='y', colors='red')
cd2.set_facecolor('black')
plt.show()
plt.savefig('./plot/pic/cases_date.png')
plt.savefig('./plot/pdf/cases_date.pdf')

data_date = cd.groupby(['cases_date']).sum().reset_index(drop=None)
dd = data_date[['Confirmed','Recovered','Deaths']].plot(kind='line',figsize=(20,10))
dd.tick_params(axis='x', colors='red')
dd.tick_params(axis='y', colors='red')
dd.set_facecolor('black')
plt.show()
plt.savefig('./plot/pic/cases_crd.png')
plt.savefig('./plot/pdf/cases_crd.pdf')