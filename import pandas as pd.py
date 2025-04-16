import pandas as pd
car = pd.read_csv("cars.csv")
car.head()
#To know the rows and columns
car.shape
#Cleaning
#Find all the null values in the dataset.if there is any null value in any column,then fill it with the mean of that column
car.isnull().sum()
car['EngineSize'].fillna(car['EngineSize'].mean())
car
#Value counts
#Check what are the different types of make are there in our dataset and ,what is the count(occurance) of each make in the data

car.head(2)
car['Make'].value_counts()
#Filtering
#Show all the recors where origin is Asia or Europe

car[car['Origin'].isin(['Asia','Europe'])]  
#Remove unwanted records
#Remove all records(rows) where weight is above 4000

car[~(car['Weight']>4000)]
#Apply Function

# Increase all the values of "MPG_City" column by 3

car['MPG_City']= car['MPG_City'].apply(lambda x:x+3)
car