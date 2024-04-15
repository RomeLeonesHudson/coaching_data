import pandas as pd 

table = pd.read_csv(r'flights_task.csv')
df = pd.DataFrame(table)

day_uniq = df['DATE'].nunique()
print(day_uniq)
