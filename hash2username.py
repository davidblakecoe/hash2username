#This was a quick and dirty throw together to get a job done
#You need to pip install pandas or pip3 install pandas
#ntds = username,hash
#cracked = hash,password

import pandas as pd
import pandas as pandasForSortingCSV
#open .csv files for processing
df1 = pandasForSortingCSV.read_csv("ntds.csv")
df2 = pandasForSortingCSV.read_csv("cracked.csv")
#drop rows that have blank passwords
df2 = df2.dropna()
#default behavior only shows a sample of the output
pd.set_option('display.max_rows', None)
#merge fields based on hash
data_merge = pd.merge(df1, df2)
data_merge = data_merge.sort_index(ascending = False, axis = 1)
print(data_merge)
