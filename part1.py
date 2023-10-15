import pandas as pd

def custom_to_float(value): # Для преобразования всех возможных вариантов обозначения NaN к одному - float('nan')
    try:
        return float(value)
    except (ValueError, TypeError):
        return float('nan')
    
def check(): # Функция для проверки своей работы
    def custom_to_float(value):
        try:
            return float(value)
        except (ValueError, TypeError):
            return float('nan')

    df_check = pd.read_csv('./task.csv')
    df_check['y'] = df_check['y'].apply(custom_to_float)
    df_check['count'] = df_check['count'].apply(custom_to_float)
    df_check.dropna(inplace = True)
    if len(df_check) - len(df) == len(pd.concat(g for _, g in df_check.groupby(['area', 'keyword']) if len(g) > 1)):
        print("It's all right")
    else:
        print("Something goes wrong")
    
df = pd.read_csv('./task.csv')

df.info() # Посмотрим на состояние данных
print(pd.unique(df.cluster)) # Есть пропущенные значения

df['y'] = df['y'].apply(custom_to_float) # Сейчас столбец имеет тип object, но там хранятся float координаты
df['count'] = df['count'].apply(custom_to_float) # Сейчас столбец имеет тип object, но там хранятся int значения
df.dropna(inplace = True)
df['cluster'] = df['cluster'].astype(int)
df['count'] = df['count'].astype(int)
df.info() # Привели всё к нужным типам данных
print(pd.unique(df.cluster))

colors = {k: v for k, v in zip(pd.unique(df.cluster), ['#17becf', '#bcbd22', '#7f7f7f','#e377c2'])} # Чтобы задать цвет каждому кластеру (по условию, кластеры разных областей могут быть одного цвета)

df['color'] = df['cluster'].map(colors)
df.drop('good (1)', axis = 1, inplace = True) # Удалили ненужные по условию столбцы

df.drop_duplicates(subset = ['area', 'keyword'], keep = False, inplace = True)
print(len(df)) # Избавились от дублирующихся ключевых слов внутри одной области

df = df.sort_values(by = ['area', 'cluster', 'cluster_name', 'count'], ascending = [True, True, True, False]) # Произвели сортировку данных

check() # Проверили свою работу

df.to_csv('to_spreadsheet.csv', index = False, sep = ',', encoding = 'utf-16') # Сохранили файл в кодировке utf-16, необходимой для корректного отображения колонки cluster_name