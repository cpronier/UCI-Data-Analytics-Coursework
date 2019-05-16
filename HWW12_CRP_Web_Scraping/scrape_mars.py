#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser


# Headline From Mars News Website

# In[2]:


#Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.
news_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'


# In[3]:


news_response = requests.get(news_url)


# In[4]:


news_soup = bs(news_response.text, 'html.parser')


# In[5]:


print(news_soup.prettify())


# In[17]:


news_results = news_soup.find_all('div', class_="content_title")


# In[24]:


news_title = news_results[0].text.strip()
print(news_title)


# Mars Weather from Twitter Account

# In[38]:


weather_url = "https://twitter.com/marswxreport?lang=en"


# In[39]:


weather_response = requests.get(weather_url)


# In[40]:


weather_soup = bs(weather_response.text, 'html.parser')


# In[41]:


print(weather_soup.prettify())


# In[42]:


weather_results = weather_soup.find_all('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")


# In[46]:


#Not all tweets on this account are weather.  I could not differeniate between the related retweets on the page and the specific weather tweets.
mars_weather = weather_results[1].text.strip()
print(mars_weather)


# Mars Facts

# In[51]:


#Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
#Use Pandas to convert the data to a HTML table string.
facts_table_url = "https://space-facts.com/mars/"


# In[52]:


facts_table = pd.read_html(facts_table_url)
facts_table


# In[53]:


type(facts_table)


# In[56]:


df = facts_table[0]
df.columns
df.head()


# In[58]:


df = facts_table[0]
df.columns = ['Mars Information', 'Measurements']
df.head()


# In[59]:


df.set_index('Mars Information', inplace=True)
df.head()


# In[60]:


html_table = df.to_html()
html_table


# In[62]:


html_table.replace('\n', '')


# In[63]:


df.to_html('table.html')


# In[66]:


#To open table in PC environment
#!explorer table.html


# In[67]:


# OSX Users can run this to open the file in a browser, 
#!open table.html


# Mars Hemispheres

# In[ ]:


# Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
# You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
# Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
# Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.


# In[ ]:




