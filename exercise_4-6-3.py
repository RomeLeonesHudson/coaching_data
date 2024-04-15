import pandas as pd 

table=pd.read_csv(r'flights_task.csv')
df= pd.DataFrame(table)

#country = df['STATE'].value_counts()
country_airports = df.STATE.value_counts()
country = country_airports.idxmax()

print(country)
