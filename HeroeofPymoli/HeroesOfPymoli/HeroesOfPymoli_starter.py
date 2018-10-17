
# coding: utf-8

# ### Heroes Of Pymoli Data Analysis
# * Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).
# 
# * Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%).  
# -----

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[1]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
file_to_load = "C:/Users/randy/Desktop/GWUBOOTCAMP/GWARL201808DATA3/04-Pandas/Homework/HeroesOfPymoli/Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)
purchase_data.head()


# ## Player Count

# * Display the total number of players
# 

# In[41]:


players_data = purchase_data.groupby(["SN"])
total_players = len(players_data)
player_count_summary = pd.DataFrame({"Total Players":total_players},index=[0])
print("Player Count")
player_count_summary


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[3]:


#unique items
unique_items = purchase_data["Item ID"].nunique()
unique_items


# In[4]:


average_price = purchase_data["Price"].mean()
average_price
round(average_price,2)


# In[5]:


Total_revenue = purchase_data['Price'].sum()
Total_revenue


# In[6]:


total_purchase = purchase_data['Purchase ID'].nunique()
total_purchase


# In[7]:


pd.DataFrame({'Number of Unique Items': [unique_items],
                  'Average Price': [round(average_price,2)],
                  'Number of Purchases': [total_purchase],
                  'Total Revenue': [Total_revenue]})


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[8]:


# Count gender first
df= purchase_data.drop_duplicates(['SN', 'Gender'])
df.count()


# In[15]:


df1 = df[df['Gender'] == 'Male']
male_players= len(df1.index)
pd.DataFrame({'Male Players': [male_players]})


# In[16]:


df1 = df[df['Gender'] == 'Female']
Female_players= len(df1.index)
pd.DataFrame({'Female Players': [Female_players]})


# In[19]:


#other plaeyer
df3=df[(df['Gender'] != 'Male') & (df['Gender'] != 'Female')]
other_players= len(df3.index)
pd.DataFrame({'Other/Non-Disclosed': [other_players]})


# In[23]:


gender_counts_df = pd.DataFrame(gender_counts)
gender_counts_df = gender_counts_df.rename(columns={"Gender": "Total Count"})
gender_counts_df["Percentage of Players"] = player_percentage.values
gender_counts_df = gender_counts_df[["Percentage of Players", "Total Count"]]
pd.options.display.float_format = '{:,.2f}'.format
print("Gender Demographics")
gender_counts_df


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[32]:


gender_counts = purchase_data["Gender"].value_counts()
gender_counts_df = pd.DataFrame(gender_counts)
gender_counts_df = gender_counts_df.rename(columns={"Gender": "Purchase Count"})
gender_average_price = purchase_data.groupby("Gender").mean()
gender_average_price = gender_average_price[["Price"]]
gender_average_price = gender_average_price.rename(columns={"Price": "Average Purchase Price"})
merge1 = pd.concat([gender_average_price, gender_counts_df], axis=1)
gender_total_purchase = purchase_data.groupby("Gender").sum()
gender_total_purchase = gender_total_purchase[["Price"]]
gender_total_purchase = gender_total_purchase.rename(columns={"Price": "Total Purchase Value"})
merge2 = pd.concat([merge1, gender_total_purchase], axis=1)
merge2["Normalized Totals"] = merge2["Total Purchase Value"] / merge2["Purchase Count"]
gender_purchases = merge2[["Purchase Count", "Average Purchase Price", "Total Purchase Value", "Normalized Totals"]]
pd.options.display.float_format = '${:,.2f}'.format
print("Purchasing Analysis (Gender)") 
gender_purchases


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[33]:


bins = [0, 9, 14, 19, 24, 29, 34, 39, 99]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]
unique_players_df["Age Group"] = pd.cut(unique_players_df["Age"], bins, labels=group_names)
age_group = unique_players_df.groupby("Age Group").count()
age_group = age_group[["Age"]]
age_group = age_group.rename(columns={"Age": "Total Count"})
age_group["Percentage of Players"] = age_group["Total Count"] / total_players * 100
age_group = age_group[["Percentage of Players", "Total Count"]]
pd.options.display.float_format = '{:,.2f}'.format
print("Age Demographics")
age_group


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[37]:


purchase_data["Age Group"] = pd.cut(purchase_data["Age"], bins, labels=group_names)
age_counts_df = purchase_data.groupby("Age Group").count()
age_counts_df = age_counts_df[["Age"]]
age_counts_df = age_counts_df.rename(columns={"Age": "Purchase Count"})
age_average_price = purchase_data.groupby("Age Group").mean()
age_average_price = age_average_price[["Price"]]
age_average_price = age_average_price.rename(columns={"Price": "Average Purchase Price"})
merge1 = pd.concat([age_average_price, age_counts_df], axis=1)
age_total_purchase = purchase_data.groupby("Age Group").sum()
age_total_purchase = age_total_purchase[["Price"]]
age_total_purchase = age_total_purchase.rename(columns={"Price": "Total Purchase Value"})
merge2 = pd.concat([merge1, age_total_purchase], axis=1)
merge2["Avg Total Purchase per Person"] = merge2["Total Purchase Value"] / merge2["Purchase Count"]
age_purchases = merge2[["Purchase Count", "Average Purchase Price", "Total Purchase Value", "Avg Total Purchase per Person"]]
pd.options.display.float_format = '${:,.2f}'.format
print("Purchasing Analysis (Age)")
age_purchases


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[44]:


top_five_spenders = players_data[["Price"]].sum().nlargest(5,"Price")
top_five_spenders = top_five_spenders.rename(columns={"Price": "Total Purchase Value"})
player_purchases = players_data[["Price"]].count()
player_purchases = player_purchases.rename(columns={"Price": "Purchase Count"})
merge1 = top_five_spenders.join(player_purchases)
average_player_purchase = players_data[["Price"]].mean()
average_player_purchase = average_player_purchase.rename(columns={"Price": "Average Purchase Price"})
merge2 = merge1.join(average_player_purchase)
top_five_spenders = merge2[["Purchase Count", "Average Purchase Price", "Total Purchase Value"]]
print("Top Spenders")
top_five_spenders


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[46]:


items_df = purchase_data.groupby(["Item ID","Item Name"])
top_five_items = items_df[["Price"]].count().nlargest(5,"Price")
top_five_items = top_five_items.rename(columns={"Price": "Purchase Count"})
item_prices = items_df[["Price"]].mean()
item_prices = item_prices.rename(columns={"Price": "Item Price"})
merge1 = top_five_items.join(item_prices)
item_purchase_total = items_df[["Price"]].sum()
item_purchase_total = item_purchase_total.rename(columns={"Price": "Total Purchase Value"})
top_five_items = merge1.join(item_purchase_total)
print("Most Popular Items")
top_five_items


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[47]:


top_five_item_sales = items_df[["Price"]].sum().nlargest(5,"Price")
top_five_item_sales = top_five_item_sales.rename(columns={"Price": "Total Purchase Value"})
top_five_item_sales
item_purchases = items_df[["Price"]].count()
item_purchases = item_purchases.rename(columns={"Price": "Purchase Count"})
merge1 = top_five_item_sales.join(item_purchases)
item_prices = items_df[["Price"]].mean()
item_prices = item_prices.rename(columns={"Price": "Item Price"})
merge2 = merge1.join(item_prices)
top_five_item_sales = merge2[["Purchase Count", "Item Price", "Total Purchase Value"]]
print("Most Profitable Items")
top_five_item_sales

