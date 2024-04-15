import pandas as pd 

table_1 = pd.read_csv('greece_flights_20200101.csv')
table_2 = pd.read_csv('greece_flights_20200102.csv')
#table_2 = table_2[['DATE', 'STATE', 'DEP','APT_CODE' ,'YEAR', 'MONTH', 'ARR']]#Перемешиваем порядок столбцов - они всё равно будут соединяться по названию и значения будут в тех же столбцах

#table_1 = table_1.drop(columns=['MONTH'])
#table_2 = table_2.drop(columns=['YEAR', 'APT_CODE'])
#При удалении каких-то колонок из таблицы - при соединении значения в отсутствующих колонках заполняются Null

#table = pd.concat([table_1, table_2], axis = 0)
#table = pd.concat([table_1, table_2], axis = 0, join = 'inner')#При такой записи - соединение происходит только по колонкам, которые есть во всех таблицах
#print(table_1, table_2)
table_3 = pd.read_csv('greece_flights_20200103.csv')#Добавили 3 таблицу
table = pd.concat([table_1, table_2, table_3], axis = 0, ignore_index=True)#Проигнорировали предыдущие индексы, также можно сделать с помощью reset_index(), заменили на новые 

print(table)
table_date = table['DATE'].str.split('-', expand = True)#Вывод из списка, после разделения какой-то ячейки по разделителю '-'
new_columns_names = {0 : 'year', 1 : 'month', 2 : 'day'}#сделаем словарь имён
table_date = table_date.rename(columns = new_columns_names)#переименуем числовые колнки в текстовые

print(table_date)

new_table = pd.concat([table, table_date], axis = 1)#показываем, что соединяем справа с таблицей

print(new_table)

new_table_dummy_1 = pd.get_dummies(new_table['STATE'])
new_table_dummy_2 = pd.concat([new_table, pd.get_dummies(new_table['STATE'])], axis = 1)
print(new_table_dummy_1, new_table_dummy_2, sep ='\n')




































