# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 13:05:16 2023

@author: vaide
"""

import pandas as pd 
# file_name =pd.read_csv('files.csv')
data=pd.read_csv('transaction.csv',sep=';')

data.info()
#calculationg markup and profit per transaction 
CostPerItem = data['CostPerItem']

NumberofItemsPurchased=data['NumberOfItemsPurchased']

CostPerTransaction=CostPerItem * NumberofItemsPurchased

data['CostPerTransaction'] = CostPerTransaction

data['SalesPerTransaction']= data['SellingPricePerItem']*data['NumberOfItemsPurchased']

data['ProfitperTransaction'] = data['SalesPerTransaction']-data['CostPerTransaction']

data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction'])/data['CostPerTransaction']

roundmarkup=round(data['Markup'],2)

data['Markup']=roundmarkup

date = data['Day'].astype(str)

year = data['Year'].astype(str)

my_date = date+'-'+data['Month']+'-'+year

data['date']=my_date

split_col = data['ClientKeywords'].str.split(',' , expand=True)
#Creating new columns for the split columns in client keywords 
data['ClientAge'] = split_col[0]

data['ClientType'] = split_col[1]

data['Lengthofcontract'] = split_col[2]

data['ClientAge'] = data['ClientAge'].str.replace('[','')

data['Lengthofcontract'] = data['Lengthofcontract'].str.replace(']','')
#using the lower function to change item to lower case

data['ItemDescription'] = data['ItemDescription'].str.lower()

#to merge files

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

data = pd.merge(data,seasons,on = 'Month')

data = data.drop('ClientKeywords',axis=1)

data = data.drop('Day',axis=1)

data = data.drop('Month',axis=1)

data = data.drop('Year',axis=1)

#export into csv

data.to_csv('Value_Cleaned.csv' , index = False)
