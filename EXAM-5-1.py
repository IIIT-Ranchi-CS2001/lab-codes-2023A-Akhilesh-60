import pandas as pd

file_path = 'AQI_Data.csv'
data = pd.read_csv(file_path)


delhi_data = data[data['City'] == 'Delhi']

print(delhi_data)
delhi_data.to_csv('Delhi_Data.csv', index=False)
