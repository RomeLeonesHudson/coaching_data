import pandas as pd 

table = pd.read_csv(r'flights_task.csv')
df = pd.DataFrame(table)
uniq_ser = df['STATE'].unique()#применимо только для объектов списка(Series)
uniq = df['DEP'].nunique()#будут выведены уникальные значения в колонке 'dep'
how_many_airports = df['STATE'].value_counts()#посчитало сколько аэропортов по каждой отдельной стране
percents = df['STATE'].value_counts(normalize = True)#процентная доля отвсех аэропортов


print(how_many_airports, how_many_airports.sum(), percents * 100, end = '\n')
print(uniq_ser, uniq)
print(df.nunique())#вывели все уникальные значения

df.index = df['APT_CODE']#превращаем столбец в строку
print(df.head(10))
df = df.reset_index(drop = True)#возврааем строку обратно в столбец
print(df.head(10))

df = df.rename(columns = {'APT_CODE' : 'airport', 'STATE' : 'country'})#переименовываем столбцы
df = df.rename(index = {0 : 'a', 1 : 'b'})#переименовываем строки
#отмечаю, что в скобках прописываем строку/стоблбец, а дальше словарь, где ключ - текущее, значение - имя, которе хотим
print(df.head(10))

df_parts = df[(df.country == 'United Kingdom')]#выбрали часть или части по котрым будет сортироваться
print(df_parts.sort_values(by=['ARR'], ascending = False))#сортируем данныеот больших к меньшим по столбцу
#если акцендин будет правильным,то сортировка происходит в обратном порядке
print(df_parts.sort_values(by=['ARR','airport'], ascending = [True, False]))
#при сортировке выше мы сначала сортируем от меньшихзначений кбольшим,азатем от последнихбукв к первым,если есть одинаковые значения первой колонки
print(df[df['DEP'] == df.DEP.max()])#df.sort_values(by=['DEP'], ascending = False.iloc[[0]])
print(df[df['ARR'] == df.ARR.min()])#df.sort_values(by=['ARR'], ascending = True.iloc[[0]])
#мы нашли максимальное и минимальное значение вылетов и прилётов
str_max = df['DEP'].idxmax()
print(str_max)#показывает индекс строки,в которой хранится максимальное значение столбца
str_min = df['DEP'].idxmin()
print(str_min)#минимальное значение на строк, в столбце
str_all = df.loc[[df['DEP'].idxmax()]]#выведет не номер строки,а полнуюстроку
print(str_all)
largest = df.nlargest(n = 3, columns ='DEP')#НАИБОЛЬШИЕ
smallest = df.nsmallest(n = 6, columns = ['DEP'])#наименьшие
print(largest, smallest)# n - количество значений, columns - по колонке 