Getting Started:

Pandas is a very powerful Python library which allows for cleaning and analysis of data in a tabular format (called a dataframe).

In this tutorial we'll extract a table from a webpage (pandas is able to find tables within a webpage) and export it to a CSV file (comma separated values). A CSV is a spreadsheet with the cell borders indicated by commas -- these files can be opened in Microsoft Excel or Google Sheets.

We'll also be using Pandas to read data from a CSV file, run summary statistics on the data, and use indexing concepts (similar to those of dictionaries) to extract data from the dataframe.

For this tutorial, run the following in your terminal/command prompt:

pip install pandas 
pip install xlrd
pip install html5lib

xlrd allows for Excel compatibility, and html5lib allows pandas to read html from a web page to look for <table> tags.