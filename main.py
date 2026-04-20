import numpy as np
import pandas as pd
#
# # Series из списка
# s = pd.Series([10, 20, 30])
# print("Series:\n", s)
# print("Values:\n", s.values)
# print("Index\n",  s.index.values.tolist())
#
# # DataFrame из словаря
# data = {
#     'Имя': ['Анна', 'Борис', 'Вика'],
#     'Возраст': [25, 30, 22],
#     'Оценка': [85, 92, 78]
# }
# df = pd.DataFrame(data)
# print("\nDataFrame:\n", df)
#
# # DataFrame из NumPy массива
# arr = np.random.rand(3, 2)
# df2 = pd.DataFrame(arr, columns=['Признак1', 'Признак2'])
# print("\nИз NumPy:\n", df2)
#
#
# s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
# print("Series:\n", s)
# arr = np.random.randint(1, 20, (4, 2))
# df = pd.DataFrame(arr, columns=["цыфра", "цифра"])
# print("\nDataFrame:\n", df)
#
# # Размерность
# print("Форма:", df.shape)
# print("Индексы строк:", df.index)
# print("Колонки:", df.columns)
# print("Типы данных:\n", df.dtypes)
#
# # Быстрый взгляд на данные
# print("\nПервые 2 строки:\n", df.head(2))
# print("\nПоследние 2 строки:\n", df.tail(2))


sales = pd.DataFrame({
    'Дата': ['2024-01-01', '2024-01-02', '2024-01-03'],
    'Товар': ['Ноутбук', 'Мышь', 'Клавиатура'],
    'Цена': [1000, 25, 75],
    'Количество': [3, 10, 5]
})
sales.to_csv('sales.csv', index=False)

# Читаем CSV
df_sales = pd.read_csv('sales.csv')
# print(df_sales)

# Общая информация о DataFrame
# print(df_sales.info())
#
# Статистика для числовых столбцов
# print(df_sales.describe())
#
# # Подсчёт уникальных значений в категориальном столбце
# print(df_sales['Товар'].value_counts())
#
#
# # Выбор одного столбца -> Series
# print(df_sales['Цена'])
#
# # Выбор нескольких столбцов
# print(df_sales[['Дата', 'Товар']])
#
# # loc: по меткам индекса (в нашем случае индекс 0,1,2)
# print(df_sales.loc[0])          # первая строка как Series
# print(df_sales.loc[0:1, 'Товар':'Цена'])  # строки 0-1, столбцы Товар и Цена
#
# # iloc: по позициям
# print(type(df_sales.iloc[0]))         # первая строка
# print(df_sales.iloc[0:2, 1:3])  # первые 2 строки, столбцы 1 и 2
#

# Условие
# condition = df_sales['Цена'] > 50
# print(condition)
#
# # Применяем фильтр
# expensive = df_sales[condition]
# print(expensive)
#
# # Сложное условие: цена > 50 И количество >= 3
# filtered = df_sales[(df_sales['Цена'] > 50) & (df_sales['Количество'] >= 11)]
# print(filtered)


# Добавляем столбец "Выручка" = Цена * Количество
# df_sales['Выручка'] = df_sales['Цена'] * df_sales['Количество']
# print(df_sales)
#
# # Изменяем тип столбца "Дата" на datetime
# df_sales['Дата'] = pd.to_datetime(df_sales['Дата'])
# print(df_sales['Дата'].dtypes)
#
# def func(x):
#     return x * 3
#
# df_sales["Выручка"] = df_sales["Выручка"].apply(func)
# print(df_sales)

import matplotlib.pyplot as plt


#
# x = np.linspace(0, 10, 50)
# y1 = np.sin(x)
# y2 = np.cos(x)
#
# # 1. ЛИНЕЙНЫЙ ГРАФИК (уже знаком)
# plt.figure(figsize=(8, 4))
# plt.plot(x, y1, label='sin(x)', color='blue', linestyle='-', linewidth=2)
# plt.plot(x, y2, label='cos(x)', color='red', linestyle='-', linewidth=2)
# plt.title('Линейный график: синус и косинус')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.grid(True)
# plt.show()
#
# # 2. ТОЧЕЧНАЯ ДИАГРАММА (SCATTER PLOT) — показывает разброс точек, связь между двумя величинами
# # Например, рост и вес людей
# plt.figure(figsize=(8, 4))
# x_scatter = np.random.randint(0,100, 50)   # 50 случайных чисел от 0 до 100
# y_scatter = x_scatter * 0.5 + np.random.randn(50) * 10   # линейная зависимость + шум
# plt.scatter(x_scatter, y_scatter, color='green', alpha=0.7, s=50)  # s - размер точек, alpha - прозрачность
# plt.title('Точечная диаграмма: зависимость y от x')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.grid(True)
# plt.show()
#
# # 3. СТОЛБЧАТАЯ ДИАГРАММА (BAR CHART) — сравнение категорий (например, продажи по месяцам)
# categories = ['Янв', 'Фев', 'Мар', 'Апр', 'Май']
# values = [23, 45, 56, 78, 33]
# plt.figure(figsize=(6, 4))
# plt.bar(categories, values, color='skyblue', edgecolor='black')
# plt.title('Столбчатая диаграмма: продажи по месяцам')
# plt.xlabel('Месяц')
# plt.ylabel('Продажи (тыс. руб.)')
# plt.show()
#
# # 4. ГОРИЗОНТАЛЬНАЯ СТОЛБЧАТАЯ (BARH) — удобно, когда много категорий или длинные названия
# plt.figure(figsize=(6, 4))
# plt.barh(categories, values, color='lightcoral')
# plt.title('Горизонтальная столбчатая диаграмма')
# plt.xlabel('Продажи')
# plt.ylabel('Месяц')
# plt.show()
#
# # 5. ГИСТОГРАММА (HISTOGRAM) — показывает распределение одной переменной (как часто встречаются значения)
# # Например, распределение возрастов в группе
# data = np.random.normal(loc=170, scale=10, size=200)  # 200 случайных ростов (среднее 170, разброс 10)
# plt.figure(figsize=(8, 4))
# plt.hist(data, bins=20, color='purple', edgecolor='black', alpha=0.7)
# plt.title('Гистограмма: распределение роста')
# plt.xlabel('Рост (см)')
# plt.ylabel('Количество человек')
# plt.grid(axis='y', alpha=0.5)
# plt.show()
#
# # 6. КРУГОВАЯ ДИАГРАММА (PIE CHART) — доли целого
# # Например, доли рынка
# labels = ['Продукт A', 'Продукт B', 'Продукт C', 'Продукт D']
# sizes = [35, 25, 20, 20]
# colors = ['gold', 'lightblue', 'lightgreen', 'pink']
# explode = (0.05, 0, 0, 0)  # выдвинуть первый сектор
# plt.figure(figsize=(6, 6))
# plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
# plt.title('Круговая диаграмма: доли рынка')
# plt.axis('equal')  # чтобы круг был круглым
# plt.show()
#
# # 7. ЯЩИК С УСАМИ (BOXPLOT) — показывает медиану, квартили, выбросы. Очень полезен для сравнения распределений
# # Например, сравним оценки учеников в двух классах
# class1 = np.random.normal(4, 0.8, 50)   # средняя оценка ~4
# class2 = np.random.normal(3.5, 0.9, 50) # средняя ~3.5
# plt.figure(figsize=(6, 5))
# plt.boxplot([class1, class2], labels=['Класс А', 'Класс Б'], patch_artist=True)
# plt.title('Ящик с усами: сравнение оценок')
# plt.ylabel('Оценка')
# plt.grid(axis='y', alpha=0.5)
# plt.show()
# x = np.linspace(0, 2*np.pi, 100)
# y = np.sin(x)
# y_cos = np.cos(x)
# fig, axes = plt.subplots(1, 2, figsize=(10, 4))  # 1 строка, 2 столбца
# axes[0].plot(x, y, 'g')
# axes[0].set_title('Синус')
# axes[1].plot(x, y_cos, 'm')
# axes[1].set_title('Косинус')
# plt.tight_layout()
# plt.show()

# Расширенный DataFrame (например, неделя продаж)
# dates = pd.date_range('2024-01-01', periods=7, freq='D')
# products = ['Ноутбук', 'Мышь', 'Клавиатура', 'Монитор', 'Ноутбук', 'Мышь', 'Клавиатура']
# prices = [1000, 25, 75, 300, 1000, 25, 75]
# quantities = [2, 15, 8, 1, 3, 20, 10]
# df_full = pd.DataFrame({'Дата': dates, 'Товар': products, 'Цена': prices, 'Количество': quantities})
# df_full['Выручка'] = df_full['Цена'] * df_full['Количество']
#
# # 1) Линейный график выручки по дням
# plt.figure(figsize=(10,4))
# plt.plot(df_full['Дата'], df_full['Выручка'], marker='o', linestyle='-')
# plt.title('Выручка по дням')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()
#
# # 2) Гистограмма цен
# plt.hist(df_full['Цена'], bins=5, edgecolor='black')
# plt.title('Распределение цен товаров')
# plt.xlabel('Цена')
# plt.ylabel('Частота')
# plt.show()
#
# # 3) Scatter: цена vs количество
# plt.scatter(df_full['Цена'], df_full['Количество'], c='red', s=80)
# plt.title('Зависимость количества от цены')
# plt.xlabel('Цена')
# plt.ylabel('Количество')
# plt.grid(True)
# plt.show()