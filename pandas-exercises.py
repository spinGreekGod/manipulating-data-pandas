#!/usr/bin/env python
# coding: utf-8

# # Pandas Practice
# 
# This notebook is dedicated to practicing different tasks with pandas. The solutions are available in a solutions notebook, however, you should always try to figure them out yourself first.
# 
# It should be noted there may be more than one different way to answer a question or complete an exercise.
# 
# Exercises are based off (and directly taken from) the quick introduction to pandas notebook.
# 
# Different tasks will be detailed by comments or text.
# 
# For further reference and resources, it's advised to check out the [pandas documnetation](https://pandas.pydata.org/pandas-docs/stable/).

# In[1]:


# Import pandas
import pandas as pd


# In[2]:


# Create a series of three different colours
colors = pd.Series(["Blue", "Green", "Yellow"])


# In[3]:


# View the series of different colours
colors


# In[4]:


# Create a series of three different car types and view it
cars = pd.Series(["BMW", "Mercedes", "Hundai"])
cars


# In[9]:


# Combine the Series of cars and colours into a DataFrame
combine = pd.DataFrame({"Cars": cars,
                        "colors": colors})
combine


# In[11]:


# Import "../data/car-sales.csv" and turn it into a DataFrame
car_sales = pd.read_csv("../data/car-sales.csv")
car_sales


# **Note:** Since you've imported `../data/car-sales.csv` as a DataFrame, we'll now refer to this DataFrame as 'the car sales DataFrame'.

# In[15]:


# Export the DataFrame you created to a .csv file
export = car_sales.to_csv("../data/car-sales.csv")


# In[21]:


# Find the different datatypes of the car data DataFrame
car_sales.dtypes


# In[22]:


# Describe your current car sales DataFrame using describe()
car_sales.describe()


# In[23]:


# Get information about your DataFrame using info()
car_sales.info()


# What does it show you?

# In[28]:


# Create a Series of different numbers and find the mean of them
series = pd.Series([4,5,9])
series.mean()


# In[29]:


# Create a Series of different numbers and find the sum of them
numbers = pd.Series([4,9,20])
numbers.sum()


# In[35]:


# List out all the column names of the car sales DataFrame
car_sales.columns


# In[32]:


# Find the length of the car sales DataFrame
len(car_sales)


# In[40]:


# Show the first 5 rows of the car sales DataFrame
car_sales.head()


# In[43]:


# Show the first 7 rows of the car sales DataFrame
car_sales.head(7)


# In[44]:


# Show the bottom 5 rows of the car sales DataFrame
car_sales.tail(5)


# In[46]:


# Use .loc to select the row at index 3 of the car sales DataFrame
car_sales.loc[3]


# In[47]:


# Use .iloc to select the row at position 3 of the car sales DataFrame
car_sales.iloc[3]


# Notice how they're the same? Why do you think this is? 
# 
# Check the pandas documentation for [.loc](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html) and [.iloc](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html). Think about a different situation each could be used for and try them out.

# In[48]:


# Select the "Odometer (KM)" column from the car sales DataFrame
car_sales["Odometer (KM)"]


# In[54]:


# Find the mean of the "Odometer (KM)" column in the car sales DataFrame
car_sales["Odometer (KM)"].mean()


# In[58]:


# Select the rows with over 100,000 kilometers on the Odometer
car_sales[car_sales["Odometer (KM)"] > 100000]


# In[61]:


# Create a crosstab of the Make and Doors columns
pd.crosstab(car_sales["Make"], car_sales["Doors"])


# In[63]:


# Group columns of the car sales DataFrame by the Make column and find the average
car_sales.groupby(["Make"]).mean()


# In[67]:


# Import Matplotlib and create a plot of the Odometer column
# Don't forget to use %matplotlib inline
import matplotlib.pyplot as plt
car_sales["Odometer (KM)"].plot()


# In[68]:


# Create a histogram of the Odometer column using hist()
car_sales["Odometer (KM)"].hist()


# In[74]:


# Try to plot the Price column using plot()


# Why didn't it work? Can you think of a solution?
# 
# You might want to search for "how to convert a pandas string columb to numbers".
# 
# And if you're still stuck, check out this [Stack Overflow question and answer on turning a price column into integers](https://stackoverflow.com/questions/44469313/price-column-object-to-int-in-pandas).
# 
# See how you can provide the example code there to the problem here.

# In[75]:


# Remove the punctuation from price column
car_sales["Price"] = car_sales["Price"].str.replace("[\$\,\.]", "")


# In[76]:


# Check the changes to the price column
car_sales["Price"]


# In[77]:


# Remove the two extra zeros at the end of the price column
car_sales["Price"] = car_sales["Price"].str[:-2]


# In[78]:


# Check the changes to the Price column
car_sales["Price"]


# In[79]:


# Change the datatype of the Price column to integers
car_sales["Price"] = car_sales["Price"].astype(int)


# In[80]:


# Lower the strings of the Make column
car_sales["Make"].str.lower()


# If you check the car sales DataFrame, you'll notice the Make column hasn't been lowered.
# 
# How could you make these changes permanent?
# 
# Try it out.

# In[81]:


# Make lowering the case of the Make column permanent
car_sales["Make"] = car_sales["Make"].str.lower()


# In[82]:


# Check the car sales DataFrame
car_sales


# Notice how the Make column stays lowered after reassigning.
# 
# Now let's deal with missing data.

# In[84]:


# Import the car sales DataFrame with missing data ("../data/car-sales-missing-data.csv")

car_sales_missing = pd.read_csv("../data/car_sales-missing-data.csv")
# Check out the new DataFrame
car_sales


# Notice the missing values are represented as `NaN` in pandas DataFrames.
# 
# Let's try fill them.

# In[85]:


# Fill the Odometer (KM) column missing values with the mean of the column inplace
car_sales_missing["Odometer"].fillna(car_sales_missing["Odometer"].mean(),
                                     inplace=True)


# In[86]:


# View the car sales missing DataFrame and verify the changes
car_sales_missing


# In[87]:


# Remove the rest of the missing data inplace
car_sales_missing.dropna(inplace=True)


# In[40]:


# Verify the missing values are removed by viewing the DataFrame
car_sales_missing


# We'll now start to add columns to our DataFrame.

# In[41]:


# Create a "Seats" column where every row has a value of 5
car_sales["Seats"] = 5
car_sales


# In[88]:


# Create a column called "Engine Size" with random values between 1.3 and 4.5
# Remember: If you're doing it from a Python list, the list has to be the same length
# as the DataFrame
engine_sizes = [1.3, 4.3, 2.3, 3.3, 3.0, 2.3, 1.4, 1.7, 2.5, 3.1]
car_sales["Engine Size"] = engine_sizes
car_sales


# In[89]:


# Create a column which represents the price of a car per kilometer
# Then view the DataFrame
car_sales["Price per KM"] = car_sales["Price"] / car_sales["Odometer (KM)"]
car_sales


# In[90]:


# Remove the last column you added using .drop()
car_sales = car_sales.drop("Price per KM", axis=1)
car_sales


# In[91]:


# Shuffle the DataFrame using sample() with the frac parameter set to 1
# Save the the shuffled DataFrame to a new variable
car_sales_sampled = car_sales_sampled = car_sales.sample(frac=1)
car_sales_sampled


# Notice how the index numbers get moved around. The [`sample()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html) function is a great way to get random samples from your DataFrame. It's also another great way to shuffle the rows by setting `frac=1`.

# In[94]:


# Reset the indexes of the shuffled DataFrame
car_sales_sampled.reset_index()


# Notice the index numbers have been changed to have order (start from 0).

# In[95]:


# Change the Odometer values from kilometers to miles using a Lambda function
# Then view the DataFrame
car_sales["Odometer (KM)"] = car_sales["Odometer (KM)"].apply(lambda x: x/1.6)
car_sales


# In[96]:


# Change the title of the Odometer (KM) to represent miles instead of kilometers
car_sales = car_sales.rename(columns={"Odometer (KM)": "Odometer (Miles)"})
car_sales


# ## Extensions
# 
# For more exercises, check out the pandas documentation, particularly the [10-minutes to pandas section](https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html). 
# 
# One great exercise would be to retype out the entire section into a Jupyter Notebook of your own.
# 
# Get hands-on with the code and see what it does.
# 
# The next place you should check out are the [top questions and answers on Stack Overflow for pandas](https://stackoverflow.com/questions/tagged/pandas?sort=MostVotes&edited=true). Often, these contain some of the most useful and common pandas functions. Be sure to play around with the different filters!
# 
# Finally, always remember, the best way to learn something new to is try it. Make mistakes. Ask questions, get things wrong, take note of the things you do most often. And don't worry if you keep making the same mistake, pandas has many ways to do the same thing and is a big library. So it'll likely take a while before you get the hang of it.
