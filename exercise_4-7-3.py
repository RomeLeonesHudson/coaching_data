import pandas as pd 

table_1 = pd.read_csv('flights_part1.csv')
table_2 = pd.read_csv('flights_part2.csv')

#print(table_1.head(5))
#print(table_2.head(5))

table_ = pd.concat([table_1, table_2], axis = 0,  join = 'inner', ignore_index = True)
print(table_.shape[1])