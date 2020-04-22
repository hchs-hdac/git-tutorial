# importing necessary libraries
import pandas as pd
import os

# reading the covid data CSV -- df stands for dataframe
# the os library (operating system) is built into Python, and is helpful for finding files on your computer

# os.path.abspath() will return the full path of the folder 3-Making Sense of Data with Pandas
path = os.path.abspath('3-Making Sense of Data with Pandas')
df = pd.read_csv(path + '\covid19_testing_data.csv')

# pandas' describe function returns summary statistics (count, mean, median, standard deviation)
summary_statistics = df.describe()
print(summary_statistics)

# renaming dataframe column using .rename() - the key-value pairs in columns={} are the old and new column names
data = df.rename(columns={'Unnamed: 0': 'Index', 'Unnamed: 0.1': 'Category',
                                    'Week 15 (April 5 – April 11, 2020)': 'Data for 4/5-4/11'})
print(data)

# dropping the unnecessary 'Index' column with .drop
cleaned_data = data.drop(columns=['Index'])
print(cleaned_data)

# indexing dataframe columns --> <name of dataframe>['<name of column>']
categories = cleaned_data['Category']
print(categories)

# slicing the dataframe with .loc - returns only the columns with the statistics
# .loc uses slicing syntax like so-- [<startrow>:<endrow>, <startcolumn>:<endcolumn>]
stats_only = cleaned_data.loc[:, 'Data for 4/5-4/11': 'Cumulative since March 1, 2020'] # the :, here means we want all the rows (we're only slicing by columns)
print(stats_only)
