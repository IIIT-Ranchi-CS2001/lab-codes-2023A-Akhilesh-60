import pandas as pd
data = pd.read_csv('data.csv')
selected_columns = data[['City', 'AQL', 'PM2.5']]
print(selected_columns.head(10))

