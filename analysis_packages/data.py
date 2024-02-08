import requests
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

FREMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=Download'

    
def get_data(filename='Fremont.csv', url=FREMONT_URL, force_download=False):
	"""Download and cache  the data
	Parameters
	__________
	filename: string(optional)
		location to  save the data
	url: string(optional)
		web location of the data
	force_download: bool (optional)
		if True, force redownload of data
	Returns
	_______
	df: pandas.DataFrame
		The fremont bridge data
	"""
	if force_download or not os.path.exists(filename):
		response = requests.get(URL)
		with open('Fremont.csv', 'wb') as f:
			f.write(response.content)
	date_format = "%m/%d/%Y %I:%M:%S %p"
	df = pd.read_csv('Fremont.csv', index_col='Date', parse_dates=True, date_format=date_format)
	df.columns = ['Total', 'West', 'East']
	return df
