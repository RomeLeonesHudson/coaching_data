import pandas as pd

table = pd.read_csv('flights_task.csv')
df = pd.DataFrame(table)

#max_dep = df[df['DEP'] == df.DEP.max()]
#min_dep = df[df['DEP'] == df.DEP.min()]

#max_dep = df.sort_values(by = ['DEP'], ascending = False)
#min_dep = df.sort_values(by = ['DEP'], ascending = True)

largest = df.nlargest(n = 10, columns = 'DEP')
smallest = df.nsmallest(n = 10, columns = 'DEP')

#print(largest, smallest)

#print(max_dep['DEP'].max())
#print(min_dep['DEP'].min())

sum_largest = largest['DEP'].sum()
sum_smallest = smallest['DEP'].sum()
all_result = (sum_largest - sum_smallest) / 10
#print(sum_largest, sum_smallest)
print(all_result)
