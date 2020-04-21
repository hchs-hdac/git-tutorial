# importing necessary libraries
import pandas as pd

# Reading webpage for tables using pandas' read_html function --returns a list of all tables on the page as dataframes
tables = pd.read_html('https://www.cdc.gov/coronavirus/2019-ncov/covid-data/covidview/index.html')

data = tables[0] # the first of the list of tables - there are two more if you're interested!

# Exporting the data to a CSV file using pandas' to_csv funtion
data.to_csv('covid19_testing_data.csv', encoding='UTF-8')
