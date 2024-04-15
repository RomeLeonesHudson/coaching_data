import pandas as pd

table = pd.read_csv('flights_task.csv')
df = pd.DataFrame(table)

country_group = df.groupby('STATE')#разбиваем данные на части / сгруппируем по странам

print(len(country_group))

divide_by_country = country_group.get_group('Germany')#вывелись все данные по указанной стране
#sum_state = divide_by_country.DEP.sum()
print(divide_by_country)
#print(sum_state)

for state, arr in country_group:
	print(state, arr.ARR.sum())
#группы поддаются итеративным функциям

state_time = df.groupby(['STATE', 'MONTH'])#выбрали данные по странам и месяцам
print(state_time.get_group(('Greece', 'APR')))

state_Series = df.groupby('STATE').size()#Превращаем объект из множества данных в серии
state_from_Series = df.groupby('STATE',as_index = False).size().sort_values('size')#превращаем обратно и добавляем сразу сортировку по колонке размер в таблице
print(state_Series, state_from_Series)

state_gr = df.groupby(['STATE'], as_index = False)['APT_CODE'].agg('nunique')#чтобы сократить код, и не использовать функции по отдельности - можно использовать agg
state_gr_arr = df.groupby(['STATE'], as_index=False)['ARR'].agg(['min', 'max', 'sum'])#функция может получить список для агрегации
state_gr_dep = df.groupby(['STATE'], as_index=False).agg({'DEP' : 'sum', 'ARR' : 'min'})#также можно использовать как словарьб где ключ - столбец, а значение - указанное в функции действие
print(state_gr, state_gr_arr, sep = '\n')
print(state_gr_dep)

#Также можно использовать написанные фунции самостоятельно
def avg_mean(x):

	return x > x.mean()

print(avg_mean(state_Series))#Получаем правду и ложь, если значение больше - правда, иначе - ложь. Нужно отметить, что работает с Сериями

def largest(x):
	return (x > x.mean()).sum()

special_count_states = df.groupby(['STATE'], as_index=False)['DEP'].agg(largest)
special_count_states_by_dict = df.groupby(['STATE'], as_index=False).agg({'DEP' : largest})
#выше даны 2 одинаковых действия, можно и так, и так
print(special_count_states, special_count_states_by_dict, sep = '\n')