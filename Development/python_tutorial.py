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

##################################################################
							PYSCAFFOLD
##################################################################


# PyScaffold is a project generator
pip install pyscaffold

# create a project called analysis with pyscaffold
putup analysis --no-skeleton

# pyscaffold - set our project up for development (Note the ending period!) (This makes sure that it's easy to import and test your code.)

python -m pip install -e .

##################################################################
							PANDAS
##################################################################

# Access the column using the name
df.loc[0, 'Released']

# Use a variable <code>q</code> to store the column <b>Rating</b> as a dataframe
q = df[['Rating']]

# Assign the variable <code>q</code> to the dataframe that is made up of the column <b>Released</b> and <b>Artist</b>:
q = df[['Released', 'Artist']]

# Use the following list to convert the dataframe index <code>df</code> to characters and assign it to <code>df_new</code>; find the element corresponding to the row index <code>a</code> and column  <code>'Artist'</code>. Then select the rows <code>a</code> through <code>d</code> for the column  <code>'Artist'</code>
new_index=['a','b','c','d','e','f','g','h']
df_new = df
df_new.index = new_index
df_new.loc['a', 'Artist']
df_new.loc['a':'d', 'Artist']

# Extract column value based on another column in Pandas
df.loc[df['Date'] == 'Jan 01, 2016', 'Open']

##################################################################
							IPYTHON
##################################################################
#install
pip install ipython

#run ipython
ipython

# run file in iptyhon
run test_script.py

# run IPython Windows (watch capital letters!)
python -m IPython


##################################################################
							PYTEST
##################################################################
# when proble running pytest
py -m pip install pytest-cov

#pytest - set enviroment ot recogniize modules, put inside test file
# https://stackoverflow.com/questions/10253826/path-issue-with-pytest-importerror-no-module-named-yadayadayada
# add to contest.py
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '\\..\\src\\assignment06')

# run pytest at level above scr and tests
python -m pytest

# run pytest without warning concerning the report
python -m pytest --cov




##################################################################
							COVERAGE
##################################################################

# install coverage
pip install coverage

#run our tests using the coverage module instead of directly using the Python interpreter
python -m coverage run test.py

#generate a code coverage report using the command
python -m coverage report

# run the test_mock.py unittest file under coverage analysis, collecting data only for mock_tutorial.py.
python -m coverage run --include=mock_tutorial.py -m unittest test_mock.py


##################################################################
							GENERAL
##################################################################

# uninstalls all pip installed modules at once without "are you sure"):
python -m pip freeze > req.del
python -m pip uninstall -y -r req.del
del req.del


#create virtual enviroment
py -m venv venv

# activate virtual enviroment
 .\venv\Scripts\activate

# Generate libraries from current projects virtual enviroment
py -m pip freeze > requirements.txt

If you want install python libs and their dependencies offline, finish following these steps on a machine with the same os, network connected, and python installed:

1) Create a requirements.txt file with similar content (Note - these are the libraries you wish to download):

Flask==0.12
requests>=2.7.0
scikit-learn==0.19.1
numpy==1.14.3
pandas==0.22.0
One option for creating the requirements file is to use 

pip freeze > requirements.txt

. This will list all libraries in your environment. Then you can go in to requirements.txt and remove un-needed ones.

2) Execute command mkdir wheelhouse && pip download -r requirements.txt -d wheelhouse to download libs and their dependencies to directory wheelhouse

3) Copy requirements.txt into wheelhouse directory

4) Archive wheelhouse into wheelhouse.tar.gz with tar -zcf wheelhouse.tar.gz wheelhouse

Then upload wheelhouse.tar.gz to your target machine:

1) Execute tar -zxf wheelhouse.tar.gz to extract the files

2) Execute pip install -r wheelhouse/requirements.txt --no-index --find-links wheelhouse to install the libs and their dependencies