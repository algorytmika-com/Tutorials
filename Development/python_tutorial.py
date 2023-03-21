# PyScaffold is a project generator
pip install pyscaffold

# create a project called analysis with pyscaffold
putup analysis --no-skeleton

# pyscaffold - set our project up for development (Note the ending period!) (This makes sure that it's easy to import and test your code.)

python -m pip install -e .

##################################################################
##################################################################
PANDAS START
##################################################################
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
##################################################################
PANDAS END
##################################################################
##################################################################

# uninstalls all pip installed modules at once without "are you sure"):
python -m pip freeze > req.del
python -m pip uninstall -y -r req.del
del req.del

# run pytest at level above scr and tests
python -m pytest

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