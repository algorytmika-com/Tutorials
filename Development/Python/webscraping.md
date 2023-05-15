##################################################################
							YFINANCE
##################################################################
import yfinance as yf
import pandas as pd

apple = yf.Ticker("AAPL")

#!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json

import json
with open('apple.json') as json_file:
    apple_info = json.load(json_file)
    # Print the type of data variable   
    #print("Type:", type(apple_info))
apple_info

apple_info['country']

#  Using the ticker object and the function `history` extract stock information and save it in a dataframe . 
# Set the `period` parameter to `max` so we get information for the maximum amount of time.
apple_share_price_data = apple.history(period="max")

#  display the first five rows of the  dataframe using the `head` function. 
apple_share_price_data.head()

# **Reset the index** using the `reset_index(inplace=True)` function
apple_share_price_data.reset_index(inplace=True)

apple_share_price_data.plot(x="Date", y="Open")

apple.dividends

apple.dividends.plot()

##################################################################
							WEBSCRAPING
##################################################################

import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"

data  = requests.get(url).text

#parse the text into html using `beautiful_soup`
soup = BeautifulSoup(data, 'html5lib')

#turn the html table into a pandas dataframe
netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

# First we isolate the body of the table which contains all the information
# Then we loop through each row and find all the column values for each row
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    # Finally we append the data of each row to the table
    netflix_data = netflix_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)  
	
# We can now print out the dataframe
netflix_data.head()

# print last 5 rows
netflix_data.tail()

# use the pandas `read_html` function using the url
read_html_pandas_data = pd.read_html(url)

# Or we can convert the BeautifulSoup object to a string
read_html_pandas_data = pd.read_html(str(soup))

# Beacause there is only one table on the page, we just take the first table in the list returned
netflix_dataframe = read_html_pandas_data[0]

netflix_dataframe.head()

# find title attribute
title = soup.find('title')

#

import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()
	

# remove comma and dollar sign
tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"")
	
# remove null and empty strings
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]