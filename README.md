# ForestStatsViewing
The idea with this repository is to make a tool for analyzing the data collected with the Forest app. It uses the exports from the app.
Here is the webpage of [Forest](https://www.forestapp.cc).

There are some python modules that need to be installed and imported for it to work, this modules are the following:
- pandas (it needs to be [installed](https://pandas.pydata.org))
- sys
- re
- datetime

The location of the exported file can ve modified in the line:

```df = pandas.read_csv('Forest.csv',names=col_names,skiprows=[0],usecols=[0,1,2,5])```

Where the code says Forest.csv is the location of the file exported from forest. In this case the code and the file are stored in the same folder so the location can be pointed with just the name of the file.
