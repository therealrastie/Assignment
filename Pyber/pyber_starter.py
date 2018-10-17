
# coding: utf-8

# In[10]:


get_ipython().run_line_magic('matplotlib', 'inline')
# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# File to Load (Remember to change these)
city_data = "C:/Users/randy/Desktop/GWUBOOTCAMP/GWARL201808DATA3/05-Matplotlib/Homework/Instructions/Pyber/data/city_data.csv"
ride_data = "C:/Users/randy/Desktop/GWUBOOTCAMP/GWARL201808DATA3/05-Matplotlib/Homework/Instructions/Pyber/data/ride_data.csv"

# Read the City and Ride Data
city_df = pd.read_csv(city_data)
city_df.head()

# Combine the data into a single dataset

# Display the data table for preview


# In[11]:


ride_df = pd.read_csv(ride_data)
ride_df.head()


# In[12]:


single_dataset = pd.merge(city_df, ride_df, on = 'city', how='outer')
single_dataset.head()


# ## Bubble Plot of Ride Sharing Data

# In[15]:


# Obtain the x and y coordinates for each of the three city types

# Build the scatter plots for each city types

# Incorporate the other graph properties

# Create a legend

# Incorporate a text label regarding circle size

# Save Figure

#city 
city = single_dataset.groupby('city')
# Avgerage 
avg_fare = city.mean()['fare']

ride_count = city['ride_id'].count()

# driver_count
driver_count = city.mean()['driver_count']

city_type = city_df.set_index('city')['type']

city_data = pd.DataFrame({
    "Number of Rides": ride_count,
    "Average Fare": avg_fare,
    "Number of Drivers": driver_count,
    "Type of City": city_type
})

city_data.sort_values('Number of Drivers', ascending = False)


# In[39]:


color_scheme = {'Light Coral':'#f08080', 'Light Sky Blue':'#87CEFA', 'Gold':'#ffd700'}

#city categories
rural = city_data[city_data['Type of City'] == 'Rural']
suburban = city_data[city_data['Type of City'] == 'Suburban']
urban = city_data[city_data['Type of City'] == 'Urban']

city_color = {'Urban': color_scheme['Light Coral'], 'Suburban': color_scheme['Light Sky Blue'], 'Rural': color_scheme['Gold']}



# scatter plots for each city type
plt.scatter(rural['Number of Rides'], rural['Average Fare'], s = rural['Number of Drivers']*10, color = city_color['Rural'], edgecolor = 'black', label = 'Rural', alpha = .75)
plt.scatter(suburban['Number of Rides'], suburban['Average Fare'], s = suburban['Number of Drivers']*10, color = city_color['Suburban'], edgecolor = 'black', label = 'Suburban', alpha = .75)
plt.scatter(urban['Number of Rides'], urban['Average Fare'], s = urban['Number of Drivers']*10, color = city_color['Urban'], edgecolor = 'black', label = 'Urban', alpha = .75)

#print scatter plot
plt.title('Pyber RIde Sharing Data (2016)')
plt.xlabel('Total Number of Rides (per City)')
plt.ylabel('Average Fare (S)')



lgnd = plt.legend(frameon = True, edgecolor = 'black')
lgnd.legendHandles[0]._sizes = [75]
lgnd.legendHandles[1]._sizes = [75]
lgnd.legendHandles[2]._sizes = [75]

plt.show()


# ## Total Fares by City Type

# In[ ]:


# Calculate Type Percents

# Build Pie Chart

# Save Figure


# In[51]:


city_type = single_dataset.groupby('type')['type', 'fare', 'ride_id', 'driver_count']

fare_sum =  city_type.sum()['fare']

labels = fare_sum.index


# In[52]:


# Show Figure
colors = [city_color[n] for n in labels]
explode = [0, 0, .3]

plt.pie(fare_sum, startangle = 90, colors = colors, explode = explode, labels = labels, autopct = "%1.1f%%", shadow = True, wedgeprops = {'linewidth': .5, 'edgecolor': 'black'})


plt.title('% of Total Fares by City Type')
plt.axis('equal')
plt.show()


# ## Total Rides by City Type

# In[48]:


# Calculate Ride Percents

# Build Pie Chart

# Save Figure
# number of ride per city type
ride_sum = city_type.count()['ride_id']



# In[49]:


# Show Figure
labels = ride_sum.index
plt.pie(ride_sum, startangle = 90, explode = explode, colors = colors, labels = labels, autopct = "%1.1f%%", shadow = True, wedgeprops = {'linewidth': .5, 'edgecolor': 'black'})
plt.title('Percentage of Total Rides by City Type')
plt.axis('equal')
plt.show()


# ## Total Drivers by City Type

# In[46]:


# Calculate Driver Percents

# Build Pie Charts

# Save Figure
driver_sum = city_type.sum()['driver_count']

labels = driver_sum.index


# In[47]:


# Show Figure
plt.pie(driver_sum, startangle = 125, explode = explode, colors = colors, labels = labels, autopct = "%1.1f%%", shadow = True, wedgeprops = {'linewidth': .5, 'edgecolor': 'black'})
plt.title('% of Total Drivers by City Type')
plt.axis('equal')
plt.show()

