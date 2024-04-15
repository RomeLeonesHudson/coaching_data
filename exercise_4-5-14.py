import pandas as pd 

table = pd.read_csv(r'Pandas\flights_task_NAN.csv')
df = pd.DataFrame(table)

df_drop = df.dropna(inplace = True)


print(df.size, df.shape)