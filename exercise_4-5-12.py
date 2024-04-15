import pandas as pd 

table = pd.read_csv(r'Pandas\flights_task_NAN.csv')
df = pd.DataFrame(table)

print((df.isna().sum()).sum())#2 .sum() - изначально мы считаем незаполненные ячейке в каждой строке и у нас получается 1 колонка / столбец, а потом мы считаем в 
#этом столбце / колонке все значения