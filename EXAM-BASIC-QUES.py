import pandas 
import numpy


dataframe=pandas.read_csv('AQI_Data.csv')
print("A. Display the first 5 rows of the dataframe:")
print(dataframe.head(5))
print("B. Display the last 6 rows of the dataframe:")
print(dataframe.tail(6))
print("C. Show summary statistics for all numeric columns:")
print(dataframe.describe())
print("D. Use numpy to compute mean AQI,PM2.5 and PM10 values for each city:")
print(dataframe.groupby('City')[['AQI',"PM2.5",'PM10']].mean())
print("2 B. Extract AQI column as Numpy array and display its mean median and standard deviation:")
column_data = dataframe['AQI'].to_numpy()
mean_value = numpy.mean(column_data)
median_value = numpy.median(column_data)
std_deviation = numpy.std(column_data)
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Standard Deviation: {std_deviation}")
