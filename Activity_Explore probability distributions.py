#!/usr/bin/env python
# coding: utf-8

# # Activity: Explore probability distributions

# ## **Introduction**
# 
# The ability to determine which type of probability distribution best fits data, calculate z-score, and detect outliers are essential skills in data work. These capabilities enable data professionals to understand how their data is distributed and identify data points that need further examination.
# 
# In this activity, you are a member of an analytics team for the United States Environmental Protection Agency (EPA). The data includes information about more than 200 sites, identified by state, county, city, and local site names. One of your main goals is to determine which regions need support to make air quality improvements. Given that carbon monoxide is a major air pollutant, you will investigate data from the Air Quality Index (AQI) with respect to carbon monoxide.

# ## **Step 1: Imports** 

# Import relevant libraries, packages, and modules. For this lab, you will need `numpy`, `pandas`, `matplotlib.pyplot`, `statsmodels.api`, and `scipy`.

# In[3]:


# Import relevant libraries, packages, and modules.

### YOUR CODE HERE ###
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sts
import scipy as sci


# A subset of data was taken from the air quality data collected by the EPA, then transformed to suit the purposes of this lab. This subset is a .csv file named `modified_c4_epa_air_quality.csv`. As shown in this cell, the dataset has been automatically loaded in for you. You do not need to download the .csv file, or provide more code, in order to access the dataset and proceed with this lab. Please continue with this activity by completing the following instructions.

# In[4]:


# RUN THIS CELL TO IMPORT YOUR DATA.

### YOUR CODE HERE ###
data = pd.read_csv("modified_c4_epa_air_quality.csv")


# <details><summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to what you learned about loading data in Python.
#     
#   
# </details>

# <details><summary><h4><strong>Hint 2</strong></h4></summary>
# 
# There is a function in the `pandas` library that allows you to load data from a .csv file into a DataFrame.
#     
#   
# </details>

# <details><summary><h4><strong>Hint 3</strong></h4></summary>
# 
# Use the `read_csv()` function and pass in the name of the csv file as a string.
#     
# </details>

# ## **Step 2: Data exploration** 

# Display the first 10 rows of the data to get a sense of how the data is structured.

# In[5]:


# Display first 10 rows of the data.

### YOUR CODE HERE ###
data.head(10)


# <details><summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to what you learned about exploring datasets in Python.
#     
#   
# </details>

# <details><summary><h4><strong>Hint 2</strong></h4></summary>
# 
# There is a function in the `pandas` library that allows you to display a specific number of rows from the top of a DataFrame.
#     
#   
# </details>

# <details><summary><h4><strong>Hint 3</strong></h4></summary>
# 
# Use the `head()` function and pass in how many rows from the top of the DataFrame you want to display.
#     
# </details>

# The `aqi_log` column represents AQI readings that were transformed logarithmically to suit the objectives of this lab. Taking a logarithm of the aqi to get a bell-shaped distribution is outside the scope of this course, but is helpful to see the normal distribution.

# To better understand the quantity of data you are working with, display the number of rows and the number of columns.

# In[7]:


# Display number of rows, number of columns.

### YOUR CODE HERE ###

data.shape


# <details><summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to what you learned about exploring datasets in Python.
#     
# </details>

# <details><summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Every DataFrame in `pandas` has a property that gives you access to the number of rows and number of columns in that DataFrame.
#   
# </details>

# <details><summary><h4><strong>Hint 3</strong></h4></summary>
# 
# Call the `shape` property of the DataFrame, which will display the number of rows and the number of columns as a tuple.
#     
# </details>

# Now, you want to find out whether `aqi_log` fits a specific type of probability distribution. Create a histogram to visualize the distribution of `aqi_log`. Then, based on its shape, visually determine if it resembles a particular distribution.

# In[9]:


# Create a histogram to visualize distribution of aqi_log.

### YOUR CODE HERE ###
data["aqi_log"].hist()


# <details><summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to the video about creating a histogram to visualize the distribution of a particular variable in the data.
#     
#   
# </details>

# <details><summary><h4><strong>Hint 2</strong></h4></summary>
# 
# There is a function in the `matplotlib` library that can be called to create a histogram.
#     
#   
# </details>

# <details><summary><h4><strong>Hint 3</strong></h4></summary>
# 
# The `hist()` function can be called directly on the `aqi_log` column from the data. 
# 
# A semicolon can be used at the end as a quick way to make sure only the plot gets displayed (other text does not get displayed).
#     
# </details>

# **Question:** What do you observe about the shape of the distribution from the histogram? 

# The historgram shows right skewed distribution of data

# ## **Step 3: Statistical tests**
# 
# Use the empirical rule to observe the data, then test and verify that it is normally distributed.
# 

#  As you have learned, the empirical rule states that, for every normal distribution: 
# - 68% of the data fall within 1 standard deviation of the mean
# - 95% of the data fall within 2 standard deviations of the mean
# - 99.7% of the data fall within 3 standard deviations of the mean
# 

# First, define two variables to store the mean and standard deviation, respectively, for `aqi_log`. Creating these variables will help you easily access these measures as you continue with the calculations involved in applying the empirical rule. 

# In[11]:


# Define variable for aqi_log mean.

### YOUR CODE HERE ###
aqi_log_mean = data["aqi_log"].mean()

# Print out the mean.
aqi_log_mean

### YOUR CODE HERE ###


# In[12]:


# Define variable for aqi_log standard deviation.

### YOUR CODE HERE ###

aqi_log_std= data["aqi_log"].std()

# Print out the standard deviation.
aqi_log_std

### YOUR CODE HERE ###


# <details><summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to the lesson about calculating the mean and standard deviation for a particular variable in the data.
#     
#   
# </details>

# <details><summary><h4><strong>Hint 2</strong></h4></summary>
# 
# There are functions in the `numpy` library that can be called to calculate mean and standard deviation, respectively.
#     
#   
# </details>

# <details><summary><h4><strong>Hint 3</strong></h4></summary>
# 
# The `mean()` function can be called directly on the `aqi_log` column from the data to compute the mean.
# 
# The `std()` function can be called directly on the `aqi_log` column from the data to compute the standard deviation.
#     
# </details>

# Now, check the first part of the empirical rule: whether 68% of the `aqi_log` data falls within 1 standard deviation of the mean.
# 
# To compute the actual percentage of the data that satisfies this criteria, define the lower limit (for example, 1 standard deviation below the mean) and the upper limit (for example, 1 standard deviation above the mean). This will enable you to create a range and confirm whether each value falls within it.

# In[14]:


# Define variable for lower limit, 1 standard deviation below the mean.

### YOUR CODE HERE ###

lower_limit_aqi= aqi_log_mean - 1 * aqi_log_std

# Define variable for upper limit, 1 standard deviation above the mean.

### YOUR CODE HERE ###
upper_limit_aqi = aqi_log_mean + 1 * aqi_log_std



# Display lower_limit, upper_limit.
print(lower_limit_aqi)
print(upper_limit_aqi)

### YOUR CODE HERE ###


# <details><summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to the video about using the empirical rule.
#     
#   
# </details>

# <details><summary><h4><strong>Hint 2</strong></h4></summary>
# 
# The lower limit here is $mean - 1 * std$.
# 
# The upper limit here is $mean + 1 * std$.
# 
# The `print` function can be called to display.
#     
#   
# </details>

# <details><summary><h4><strong>Hint 3</strong></h4></summary>
# 
# Use the variables that you defined for mean and standard deviation of `aqi_log`, ensuring the spelling is correct. 
# 
# Call the `print` function and pass in the values one after the other, with a comma between them.
#     
# </details>

# In[17]:


# Display the actual percentage of data that falls within 1 standard deviation of the mean.

### YOUR CODE HERE ### 
first_emp_rule= ((data["aqi_log"]>= lower_limit_aqi) & (data["aqi_log"]<= upper_limit_aqi)).mean()
first_emp_rule


# <details><summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to the video about using the empirical rule.
#     
# </details>

# <details><summary><h4><strong>Hint 2</strong></h4></summary>
# 
# The `>=` operator can be used to confirm whether one value is greater than or equal to another value.
# 
# The `<=` operator can be used to check whether one value is less than or equal to another value.
# 
# The `&` operator can be used to check if one condition and another condition is met. 
#     
# </details>

# <details><summary><h4><strong>Hint 3</strong></h4></summary>
# 
# The `mean()` function can be used to compute the proportion of the data that satisfies the specified conditions. 
# 
# Multiplying that proportion by $100$ can get you the percentage.
#     
# </details>

# Now, consider the second part of the empirical rule: whether 95% of the `aqi_log` data falls within 2 standard deviations of the mean.
# 
# To compute the actual percentage of the data that satisfies this criteria, define the lower limit (for example, 2 standard deviations below the mean) and the upper limit (for example, 2 standard deviations above the mean). This will enable you to create a range and confirm whether each value falls within it.

# In[20]:


# Define variable for lower limit, 2 standard deviations below the mean.

### YOUR CODE HERE ###
lower_limit_aqi1= aqi_log_mean - 2 * aqi_log_std



# Define variable for upper limit, 2 standard deviations below the mean.

### YOUR CODE HERE ###
upper_limit_aqi1= aqi_log_mean + 2 * aqi_log_std




# Display lower_limit, upper_limit.


### YOUR CODE HERE ###

print(lower_limit_aqi1)
print(upper_limit_aqi1)


# <details><summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to the video about using the empirical rule.
#     
#   
# </details>

# <details><summary><h4><strong>Hint 2</strong></h4></summary>
# 
# The lower limit here is $mean - 2 * std$.
# 
# The upper limit here is $mean + 2 * std$.
# 
# The `print` function can be called to display.
#     
#   
# </details>

# <details><summary><h4><strong>Hint 3</strong></h4></summary>
# 
# Use the variables that you defined for mean and standard deviation of `aqi_log`, ensuring the spelling is correct. 
# 
# Call the `print` function and pass in the values one after the other, with a comma between them.
#     
# </details>

# In[21]:


# Display the actual percentage of data that falls within 2 standard deviations of the mean.

### YOUR CODE HERE ### 

first_emp_rule_1= ((data["aqi_log"]>= lower_limit_aqi1) & (data["aqi_log"]<= upper_limit_aqi1)).mean()
first_emp_rule_1


# <details><summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to the video section about using the empirical rule.
#     
# </details>

# <details><summary><h4><strong>Hint 2</strong></h4></summary>
# 
# The `>=` operator can be used to confirm whether one value is greater than or equal to another value.
# 
# The `<=` operator can be used to check whether one value is less than or equal to another value.
# 
# The `&` operator can be used to check if one condition and another condition is met. 
#     
# </details>

# <details><summary><h4><strong>Hint 3</strong></h4></summary>
# 
# The `mean()` function can be used to compute the proportion of the data that satisfies the specified conditions. 
# 
# Multiplying that proportion by $100$ can get you the percentage.
#     
# </details>

# Now, consider the third part of the empirical rule:whether 99.7% of the `aqi_log` data falls within 3 standard deviations of the mean.
# 
# To compute the actual percentage of the data that satisfies this criteria, define the lower limit (for example, 3 standard deviations below the mean) and the upper limit (for example, 3 standard deviations above the mean). This will enable you to create a range and confirm whether each value falls within it.

# In[22]:


# Define variable for lower limit, 3 standard deviations below the mean.

### YOUR CODE HERE ###
lower_limit_aqi2= aqi_log_mean - 3 * aqi_log_std



# Define variable for upper limit, 3 standard deviations above the mean.

### YOUR CODE HERE ###
upper_limit_aqi2= aqi_log_mean + 3 * aqi_log_std




# Display lower_limit, upper_limit.

### YOUR CODE HERE ###
print(lower_limit_aqi2)
print(upper_limit_aqi2)


# <details><summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to the video about using the empirical rule.
#     
#   
# </details>

# <details><summary><h4><strong>Hint 2</strong></h4></summary>
# 
# The lower limit here is $mean - 3 * std$.
# 
# The upper limit here is $mean + 3 * std$.
# 
# The `print` function can be called to display.
#     
#   
# </details>

# <details><summary><h4><strong>Hint 3</strong></h4></summary>
# 
# Use the variables that you defined for mean and standard deviation of `aqi_log`, ensuring the spelling is correct. 
# 
# Call the `print` function and pass in the values one after the other, with a comma between them.
#     
# </details>

# In[24]:


# Display the actual percentage of data that falls within 3 standard deviations of the mean.

### YOUR CODE HERE ### 

first_emp_rule_2= ((data["aqi_log"]>= lower_limit_aqi2) & (data["aqi_log"]<= upper_limit_aqi2)).mean()
first_emp_rule_2


# <details><summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to the video about using the empirical rule.
#     
# </details>

# <details><summary><h4><strong>Hint 2</strong></h4></summary>
# 
# The `>=` operator can be used to confirm whether one value is greater than or equal to another value.
# 
# The `<=` operator can be used to check whether one value is less than or equal to another value.
# 
# The `&` operator can be used to check if one condition and another condition is met. 
#     
# </details>

# <details><summary><h4><strong>Hint 3</strong></h4></summary>
# 
# The `mean()` function can be used to compute the proportion of the data that satisfies the specified conditions. 
# 
# Multiplying that proportion by $100$ can get you the percentage.
#     
# </details>

# ## **Step 4: Results and evaluation** 

# **Question:** What results did you attain by applying the empirical rule? 

# From empirical rule, I found that within 1 standard deviation 76.1% of the dataset lies, irrespective of 68%

# **Question:** How would you use z-score to find outliers? 

# when the value pof z-score values exceeds +3 and lesser than -3, one can determine that value as an outlier.

# Compute the z-score for every `aqi_log` value. Then, add a column named `z_score` in the data to store those results. 

# In[28]:


# Compute the z-score for every aqi_log value, and add a column named z_score in the data to store those results.
from scipy import stats
### YOUR CODE HERE ###
data["z_score"]= stats.zscore(data["aqi_log"])
data



# Display the first 5 rows to ensure that the new column was added.

### YOUR CODE HERE ###
data.head(5)


# <details><summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to the video about calculating z-score.
#     
# </details>

# <details><summary><h4><strong>Hint 2</strong></h4></summary>
# 
# There is a function in the `stats` module of the `scipy` library that you can call to calculate z-score.
#     
# </details>

# <details><summary><h4><strong>Hint 3</strong></h4></summary>
# 
# Call the `zscore()` function and pass in the `aqi` column from the data.
#     
# </details>

# Identify the parts of the data where `aqi_log` is above or below 3 standard deviations of the mean.

# In[35]:


# Display data where `aqi_log` is above or below 3 standard deviations of the mean

### YOUR CODE HERE ###
outliers= data[(data["z_score"]>3) | (data["z_score"]< -3)]
outliers


# <details><summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to the video about outlier detection.
#     
# </details>

# <details><summary><h4><strong>Hint 2</strong></h4></summary>
# 
# The `>` operator can be used to evaluate whether one value is greater than another value. 
# 
# The `<` operator can be used to evaluate whether one value is less than another value. 
# 
# The `|` operator can used to evaluate whether one condition or another condition is met.  
#     
# </details>

# <details><summary><h4><strong>Hint 3</strong></h4></summary>
# 
# To index the DataFrame, place a pair of parantheses around the evaluation of the two conditions and pass that into a pair of square brackets. This will allow you to get all rows in the data where the specified criteria is met.
# 
# Make sure the spelling of the column matches the name you specified when creating that column. 
#     
# </details>

# **Question:** What do you observe about potential outliers based on the calculations?
# 

# One can observe from the above that Arizona with aqi_log of 3.931826 shows high variability from the rest of teh datset, hence is conidered as an outlier here.

# **Question:** Why is outlier detection an important part of this project? 

# It is an important step as it can lead biased results that can distrupt our desired output.

# ## **Considerations**

# **What are some key takeaways that you learned during this lab?**

# Outlier analysis is important to get the proper outcome from any analysis as it can give bias results which is undesirable in most of the data science cases.

# **What summary would you provide to stakeholders? Consider the distribution of the data and which sites would benefit from additional research.**

# The data is right-skewed which shows that there is more value distribution below the mean and within 1 standard deviation. So, One need to go for predictions according to the provided result.

# **Reference**
# 
# US EPA, OAR. 2014, July 8. [Air Data: Air Quality Data Collected at Outdoor Monitors Across the US](https://www.epa.gov/outdoor-air-quality-data). 

# **Congratulations!** You've completed this lab. However, you may not notice a green check mark next to this item on Coursera's platform. Please continue your progress regardless of the check mark. Just click on the "save" icon at the top of this notebook to ensure your work has been logged.
