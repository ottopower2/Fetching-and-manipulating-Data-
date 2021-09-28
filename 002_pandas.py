import pandas as pd
import numpy as np
# 2 main datatypes
# 1-dimentional=series
series = pd.Series(["BMW", "Toyota", "Honda"])
print(series)


colours = pd.Series(["Red", "Blue", "White"])
colours

# DataFrame = 2-dimensional
car_data = pd.DataFrame({"Car make": series, "Colour": colours})
print(car_data)
print('*'*40)
# Import data
# Import data
car_sales = pd.read_csv("car-sales.csv")
print(car_sales)
# 2-dimentional=dataframe
# Exporting a dataframe
print('*'*40)
car_sales.to_csv("exported-car-sales.csv", index=False)
exported_car_sales = pd.read_csv("exported-car-sales.csv")
print(exported_car_sales)

# Describe data
#Attribute
print(car_sales.dtypes)
print(car_sales.columns)
print(car_sales.columns[0]=="amouri")
print(car_sales.columns)

#Function with bracket
print(car_sales.describe())#'descrip work in numeric number'
print(car_sales.info())
car_prices=pd.Series([3000,1500,111250])
print(car_prices.mean())
# print(car_sales.sum())
print(car_sales["Doors"].sum())
# print(car_sales["Price"].sum())
print(len(car_sales))

print('*'*40)

# Viewing and selecting data

print(car_sales.head(8))   # the head from the table
print(car_sales.tail())    #the end of table
print('*'*40)


# .loc & .iloc

#loc reffer to index
animals = pd.Series(["cat", "dog", "bird", "panda", "snake"],
                    index=[0, 3, 9, 8, 3])
print(animals)

print(animals.loc[3])
print(animals.loc[9])
print('*'*40)

#iloc referr to position 
print(car_sales.loc[3])
print('*'*40)
print(animals.iloc[3])

#Slicing 

print(animals.iloc[:3])
print(car_sales.iloc[:3])
print(car_sales.loc[:3])

print(car_sales["Make"])
print(car_sales.Make.head(4))
print(car_sales[car_sales["Make"]=="Toyota"])
print('*'*40)

print(car_sales[car_sales["Odometer (KM)"]>100000])
print('*'*40)
print(pd.crosstab(car_sales["Make"], car_sales["Doors"]))

print('*'*40)
#GroupBy

print(car_sales.groupby(["Make"]).mean())

import matplotlib.pyplot as plt


# car_sales["Odometer (KM)"].plot()
# plt.show()
# car_sales["Odometer (KM)"].hist()
# plt.show()

#Convert Obj into integer
print(car_sales["Price"].dtype)
#dataframe['amount'] = dataframe['amount'].str.replace('[\$\,\.]', '').astype(int)
car_sales["Price"]= car_sales["Price"].str.replace('[\$\,\.]', '').astype(int)
print(car_sales["Price"].dtype)
print('*'*40)
print(car_sales)
print('*'*40)

print(car_sales[car_sales["Price"]>70000])

# car_sales["Price"] = car_sales["Price"].str.replace('[\$\,\.]', '').astype(int)
# print(car_sales[car_sales["Price"]>700000])

# Manipulating Data
print('*'*40)

car_sales["Make"] = car_sales["Make"].str.lower()

print('*'*40)
# Messing Data
car_sales_missing=pd.read_csv("car-sales-missing-data.csv")
print(car_sales_missing)

car_sales_missing["Odometer"]=car_sales_missing["Odometer"].fillna(car_sales_missing["Odometer"].mean(),
                                     inplace=False)

print(car_sales_missing)
print('*'*40)
# drop messing Values
print(car_sales_missing.dropna())

print('*'*40)

car_sales_missing_dropped = car_sales_missing.dropna()
print(car_sales_missing_dropped)

car_sales_missing_dropped.to_csv("car-sales-missing-dropped.csv")
print('*'*40)
print(car_sales)
# added a column
Seats_column=pd.Series([5,5,5,5,5])
car_sales["Seats"]=Seats_column
print(car_sales)
# Fill the coloumn 

car_sales["Seats"].fillna(5, inplace=True)
print(car_sales)
# Column from Python list
fuel_economy = [7.5, 9.2, 5.0, 9.6, 8.7, 4.7, 7.6, 8.7, 3.0, 4.5]
car_sales["Fuel per 100KM"] = fuel_economy
print(car_sales)

#calculate Total Total fuel used (L)
car_sales["Total fuel used (L)"]=car_sales["Odometer (KM)"]*car_sales["Fuel per 100KM" ]
print(car_sales)

# Create a column from a single value
car_sales["Number of wheels"] = 4
print(car_sales)
car_sales["Passed road saftey"] = True
print(car_sales)
print(car_sales["Odometer (KM)"])
print(car_sales.shape)

#Axsis 
print('*'*40)
print(car_sales)



car_sales_shuffled = car_sales.sample(frac=1)

print(car_sales_shuffled)

# Only select 20% of data
# car_sales_shuffled=car_sales_shuffled.sample(frac=0.01)
# print(car_sales_shuffled)

#reset
car_sales_shuffled.reset_index(drop=True, inplace=True)
print(car_sales_shuffled)

#apply function 




# car_sales["Odometer (KM)"] = car_sales["Odometer (KM)"].apply(lambda x: x / 1.6)
# print(car_sales)

print('*'*40)

# def myfunc():
#   for i in car_sales["Odometer (KM)"]:
      
#       b=i/1.6
#       return(f"{int(b)}")

# myfunc()

print(car_sales["Odometer (KM)"])

