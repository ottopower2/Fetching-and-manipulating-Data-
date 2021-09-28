import numpy as np 
import pandas as pd
import time

from pandas.tseries.offsets import Day 

## Datatypes & Attributes

a2 = np.array([[1, 2.0, 3.3],[4, 5, 6.5]])
print(a2)

a3 = np.array([[[1, 2, 3],[4, 5, 6],[7, 8, 9]],

[[10, 11, 12],[13, 14, 15],[16, 17, 18]]])
print(a3)

print(a2)
print(a2.shape)
print(a3.shape)

print(a2.ndim ,a3.ndim)

print(a2.size,a3.size)
print(type(a2))

# creat a Dataframe 

df=pd.DataFrame(a2)
print(df)



## 2 Create Arrays

ones=np.ones((2,3))
ones2=np.ones(5)
print(ones)
print(ones2)
zeros=np.zeros((2,3))

print(zeros)

range_array=np.arange(0,10,2)
print(range_array)

random_array = np.random.randint(0, 10, size=(3, 5))

print(random_array)


random_array_4 = np.random.rand(5, 3)
print(random_array_4)

a5 = np.random.randint(10, size=(2, 3, 4, 5))

print(a5)
print("*"*40)
print(a5[:, :, :1, :])


a3 = np.array([[[1, 2, 3],[4, 5, 6],[7, 8, 9]],

[[10, 11, 12],[6 ,7,8],[13, 14, 15]]])
print(a3)

# Aggregation
print("*"*40)

listy_list=[1,2,3]
print(type(listy_list))
print(sum(listy_list))
print(sum(a2))


# Use Python's methods (sum()) on Python datatypes and use NumPy's methods on NumPy arrays (np.sum()).

#creative a massive Numpy array

massive_array=np.random.random(100000)
print(massive_array.size)
print(massive_array[:10])

#magice function
#  %timeit sum(massive_array) #Python's sum()
# %timeit np.sum(massive_array) #Nump Sum np.sum() >>>> very fast than python function 
print(np.std(a2))
print(np.var(a2))

#standard deviation=squaretoot of variance
print(np.sqrt(np.var(a2)))

# Demo of std and var
high_var_array = np.array([1, 100, 200, 300, 4000, 5000])
low_var_array = np.array([2, 4, 6, 8, 10])
print("*"*40)
print(f"the variation is {np.var(high_var_array),np.var(low_var_array)}")
print(f"the standar deviation is {np.std(high_var_array),np.std(low_var_array)}")
print(f"the average is {np.mean(high_var_array),np.mean(low_var_array)}")
print("*"*40)
# import matplotlib.pyplot as plt

# plt.hist(high_var_array)
# plt.show()

# plt.hist(low_var_array)
# plt.show()

# Reshaping & transposing

print("*"*40)
print(a2.shape,a3.shape)

print(a2)
print(a3)
print(a2.reshape(2,3,1))
print(a2.reshape(2,3,1).shape)

a2_rashape=a2.reshape(2,3,1)
print(a2_rashape*a3)

# Transpose =switches the axis
print("*"*40)
print( "Transpose")
print(a2.T)
print(a2)
print("*"*40)
print( "Transpose")
print(a3.T)
print(a3.T.shape)
print( "a3")
print(a3.shape)
print(a3)


################ Dot product##################
# dot product numpy >>research 
np.random.seed(0)
print("*"*40)
mat1 = np.random.randint(10, size=(5, 3))
mat2 = np.random.randint(10, size=(5, 3))

print(mat1)
print(mat2)
# print(mat1*mat2)
# print(np.dot(mat1*mat2))
print(mat1.T.shape,mat2.shape)
# print(mat1.T*mat2)
print(np.dot(mat1,mat2.T))
a=np.dot(mat2,mat1.T)
print(a)
print(a.T)


# Dot product exmaple (nut butter sales)
print("*"*40)
print("*"*40)
np.random.seed(0)
# Number of jars sold
sales_amounts = np.random.randint(20, size=(5,3))
print(sales_amounts)
# create array Price
prices = np.array([10, 8, 12])
print(prices)
print(prices.reshape(1,3))

# Create weekly_sales DataFrame
weekly_sales = pd.DataFrame(sales_amounts,
                            index=["Mon", "Tues", "Wed", "Thurs", "Fri"],
                            columns=["Almond butter", "Peanut butter", "Cashew butter"])
print(weekly_sales)



price_Butter=pd.DataFrame(prices.reshape(1,3),
                          index=["Price"],
                          columns=["Alomd_butter","Peanut_Butter","Cashew_Butter"])

print(price_Butter)

Total_sales=prices.dot(sales_amounts.T)
print(Total_sales)

#Create Daily_sALES
print(price_Butter.shape, weekly_sales.T.shape)
print(weekly_sales.T.shape)
daily_sales = prices.dot(weekly_sales.T)
print(price_Butter.shape)
print(prices.dot(weekly_sales.T))
weekly_sales["Total"] = daily_sales.T
print(weekly_sales)

verified=[]
for verification in daily_sales:
    if verification>200:
        print("True")
        verified.append(verification)
        
    else: 
        False
        print("False")
        verified.append(verification)

verify_me= daily_sales.T>200
print(verify_me)        
weekly_sales["Verification>200"] = verify_me.T
print(daily_sales.T)
for i in verify_me:
    print(i.count('True'))
   
    




# Comparison Operators

