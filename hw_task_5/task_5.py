import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#task1
data = np.random.randint(1, 11, size=(10, 10))
df = pd.DataFrame(data)

#print(df)

#task2

data1 = np.random.randint(1, 11, size=(10, 10))
df2 = pd.DataFrame(data1, index = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
#print(df2)
df3 = df2[(df2 > 5).all(axis=1)]

#task3

data2 = np.random.randint(1, 11, size=(10, 10))
df4 = pd.DataFrame(data2, index = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
print(df4.shape)
print(df4.columns)
print(df4.values.mean())
#df4.to_csv('random_matrix.csv', index_label='Index')

#task 4
df5 = pd.read_csv('C:/Users/Kukushkin/PycharmProjects/game/hw_task_5/emojis.csv')

#print(df5.head())
print(df5['Category'][df5.Rank == 1])

#task5

df6 = pd.read_csv('C:/Users/Kukushkin/PycharmProjects/game/hw_task_5/emojis.csv')

print(df6.groupby('Year')['Year'].count())
plt.plot(df6.groupby('Year')['Year'].count())
plt.show()
