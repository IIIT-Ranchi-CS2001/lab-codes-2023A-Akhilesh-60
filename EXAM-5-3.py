import pandas as pd
file_path = 'AQI_Data.csv'  

data = pd.read_csv(file_path)
print("First few rows of the dataset:")
print(data.head())

filtered_data = data[(data['AQI'] > 300) & (data['PM10'] > 200)]

if not filtered_data.empty:
    print("\nFiltered rows where AQI > 300 and PM10 > 200:")
    print(filtered_data)
else:
    print("\nNo rows found where AQI > 300 and PM10 > 200.")

output_path = 'Filtered_AQI_Data.csv'
filtered_data.to_csv(output_path, index=False)
print(f"\nFiltered data has been saved to {output_path}.")
