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