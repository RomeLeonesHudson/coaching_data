import pandas as pd 

table=pd.read_csv(r'flights_task.csv')
df = pd.DataFrame(table)

countries = df['STATE'].sort_values()
country = countries.value_counts()

counter = 0
for i in country:
	if i > 10:
		counter += i
print(counter)

#print(country)
#print(countries)