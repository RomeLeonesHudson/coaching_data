import pandas as pd 

table_1 = pd.read_csv('weather_part1.csv')
table_2 = pd.read_csv('weather_part2.csv')

#print(table_1, table_2, end = '\n')

table_ = pd.concat([table_1, table_2], axis = 0, ignore_index = True)

print(table_['temperature'].mean().round(1))