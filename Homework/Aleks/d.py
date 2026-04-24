import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

n=50

table={"name":np.random.choice(["Gigabyte","DELL","HP","ASUS","Acer","Lenovo"],size=50),
       "price":np.random.uniform(100,1000, size=n).round(1),
       "age":np.random.randint(1,11,size=n)
       }
df=pd.DataFrame(table)

def price_of_age(row): # Зависимость цены от возраста модели
    a=row['price']
    if row['age'] <= 3:
        a *= 1
    elif row['age'] <= 5:
        a *= 0.9
    elif row['age'] <= 7:
        a *= 0.8
    else:
        a *= 0.7
    return a

df['discount'] = df.apply(price_of_age, axis=1).round(1)
print(df.head())
df.to_csv("price.csv",index=False)

b=pd.read_csv("price.csv")
print(b.describe(), end='\n\n')
print(b.dtypes, end='\n\n')

# Гистограмма отношения цены и количества
plt.hist(b["discount"],color='skyblue', edgecolor='black')
plt.title("Цены")
plt.xlabel("Цены")
plt.ylabel("Количество покупок")
plt.axvline(b["discount"].mean(), color="y", linestyle="--", label=f"Среднее значение: {b["discount"].mean()}")
plt.grid(True,alpha=0.3)
plt.show()

# Круговая диаграмма продаж по названиям
plt.figure(figsize=(6,5))
b["name"].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['skyblue', 'forestgreen','darkmagenta','darkcyan',
                                                                     'slategray','rosybrown'])
plt.title('Распределение продаж по названиям')
plt.show()

# Столбчатый график количества продаж по возрасту компьютера
plt.figure(figsize=(6,5))
b["age"].value_counts().plot(kind="bar",color='sienna', alpha=0.4, edgecolor='black')
plt.title("Продажи по возрасту компьютера")
plt.xlabel("Возраст, лет")
plt.ylabel("Количство")
plt.grid(True, axis='y')
plt.xticks(rotation=90)
plt.show()

# Столбчатый график количества продаж по назвагию компьютера
plt.figure(figsize=(6,5))
b["name"].value_counts().plot(kind="bar", color='green', alpha=0.4,edgecolor='black')
plt.title("Продажи по названиям")
plt.xlabel("Названия")
plt.ylabel("Цены")
plt.grid(True, axis='y')
plt.xticks(rotation=90)
plt.show()