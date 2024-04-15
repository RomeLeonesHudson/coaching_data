import pandas as pd 

table = pd.read_csv('flights_task.csv')
cells = pd.DataFrame(table)

max_dep = cells.groupby(['DATE'], as_index=False).agg({'DEP' : 'max', 'ARR' : 'max'}).sort_values(by='DEP', ascending=False)
#max_arr = cells.groupby(['DATE']).agg({'ARR' : 'max'})

print(max_dep['DATE'].head(1).values[0])
