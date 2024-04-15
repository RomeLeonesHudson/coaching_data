import pandas as pd 

table_1 = pd.read_csv('europe_flights.csv')
table_2 = pd.read_csv('airports.csv')

#print(table_1.head(15))
state_flights_1 = table_1.groupby(['STATE', 'APT_CODE']) [['DEP', 'ARR']].sum()
state_flights = table_1.groupby(['STATE', 'APT_CODE'], as_index=False) [['DEP', 'ARR']].sum()

#print(state_flights)
#print(state_flights_1)

#print(state_flights['APT_CODE'].nunique())#вывели уникальные аэропорты

#print(table_2.iloc[: 18, : ])


table_2[['name', 'code']] = table_2['ident'].str.split('(', expand = True)
table_2['name'] = table_2['name'].str.strip(' ')
table_2['code'] = table_2['code'].str.strip(')')
print(table_2.iloc[: 18, : 18])
table_merge = pd.merge(table_2, state_flights, left_on = 'ident', right_on = 'APT_CODE', how = 'left')
print(table_merge)