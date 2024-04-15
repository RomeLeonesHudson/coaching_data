import pandas as pd 

table = pd.read_csv(r'Pandas\flights_task_NAN.csv')
df = pd.DataFrame(table)

dep_isna = df['DEP'].isna().sum
mean_dep = (df['DEP'].mean()).astype(int)


new_dep = df['DEP'].fillna(value = mean_dep, inplace = True)# .fillna() - возвращает значения в ДатаФрейм, а не создаёт новый при записи inplace = True
print(df['DEP'].sum(axis = 0))