import numpy as np 
import pandas as pd


df=pd.read_csv("movies.csv")
print('*'*40)
# print(df)
print('*'*40)
# print(df.head())
# print(df.shape)
print(df.columns)

df["Worldwide Gross"]= df["Worldwide Gross"].str.replace('[\$\,\.]', '').astype(int) # Converting Data
print('*'*40)


 ################                         Testing                             ################ 
print('*'*40)
## Creating Data based on "Genre"
grouped=df.groupby("Genre")
for key,value in grouped:
    # print(key)
    # print(value)
    if key== "Drama":
       
        print(value)
print('*'*40)
print('*'*40)
print(grouped.get_group("Drama"))
print(grouped.get_group("Drama").sum()) #BUILDING THE SUM using sum function
print('*'*40) 
print(df["Worldwide Gross"].sum()) 
 
print('*'*40)

My_Year_of_editon_Genre=[]
for key,value in grouped:
    # print(key)
    # print(value)
    if key== "Comedy":
        print(value)
        comedy_price=value["Worldwide Gross"]
        print(comedy_price.sum())
        Year_of_editon_Genre=value["Year"]
        for i in Year_of_editon_Genre:
            
            My_Year_of_editon_Genre.append(i)
        print(f"Number of Drama_Film in 2010 is  : {My_Year_of_editon_Genre.count(2010)}")
print(df.columns) 
print('*'*40)
print('*'*40)

 ################                         Testing                             ################ 
#remove duplicate string from List #
seen = set()
result = []
for item in df["Genre"]:
    if item not in seen:
        seen.add(item)
        result.append(item)
print(result)



  ################ Building Function to drive specific data incl. calculations############### 
print("Creat Function to retrieve Data: ")
 
def My_Genre():
    
    print(f" Available Genre is : {result}")
    print(f" put the available Genre, Note: choose just one genre from the list : {result}")
    grouped=df.groupby("Genre") 
    key=input()
    value=grouped.get_group(key)
    print(value)
    The_price=value["Worldwide Gross"]
    print(f" the Total Price of Drama Film in $ is : {The_price.sum()}")

    print(f" The total numbers of Drama Film is {len(My_Year_of_editon_Genre)}")

    Year_vec=[2007, 2008, 2009, 2010, 2011]# there is a python syntax to remove duplicated years ......
    for i in Year_vec:
     
        print(f"Number of Drama_Film {i} in Years is  : {My_Year_of_editon_Genre.count(i)}") #already methode created line 36-48
   
My_Genre()

 ################ Building Function to drive specific data incl. calculations############### 