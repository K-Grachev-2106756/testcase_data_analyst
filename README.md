# testcase_data_analyst
Тестовое задание на должность Junior Data Analyst

>   Часть 1. Анализ и обработка данных.
>>С помощью метода DataFrame.info() определил, что данные имеют разные "неправильные" значения, из-за которых, к примеру, числа в столбце 'y' хранятся, как строка. 
>>
>>Привел их к виду nan и удалил все такие записи таблицы с помощью DataFrame.dropna(). 
>>
>>Далее столбцы привел к нужным типам (int, float).
>> 
>>Выбрал цвета на Tableu и добавил столбец 'color', каждому кластеру приводя соответствующий цвет, что не противоречит условию.
>>
>>В таблице оставил только столбцы area, cluster, cluster_name, keyword, x, y, count, color.
>>
>>Убрал дублирующиеся в одной области ключевые слова с помощью DataFrame.drop_duplicates(subset = ['area', 'keyword']).
>>
>>Отсортировал по четырём столбцам так, чтобы в area, cluster и cluster_name значения возрастали, а в count - убывали.
>>
>>Сохранил данные в .csv формате в кодировке UTF-16 (при сохранении в другой кодировке, столбец cluster_name не отображается нормально).

>   Часть 2. Визуализация данных.
>>В цикле выполняю работу с каждой областью по-отдельности и для нее отрисовываю диаграмму рассеивания.
>>
>>В тестовом задании было предложено заменять пробелы на '\n', если длина строки больше 15, что я и реализовал в функции change_str(s: str).
>>
>>Сначала на график наносятся точки (было учтено пожелание об обводке объектов). 
>>>В процессе выполнения задания выяснилось, что есть объекты, у которых координаты отличаются меньше чем на 0.01. Возникает ситуация, что один из объектов закрывает другой. Это было решено с помощью параметра ax.scatter(alpha = 0.5), отвечающего за прозрачность объектов на диаграме.
>>
>>Затем формируется легенда.
>>
>>Одним из условий задания было не допустить наложения подписей разных объектов друг на друга. Я решил это следующим образом:
>>>Для текущего объекта я нахожу ближайший объект из всей области. Если координаты по осям различаются меньше, чем на 0.7, подписи могут накладываться друг на друга. Поэтому я смещаю текст с помощью параметра ax.annotate(xytext = (kx, ky)). Смещение также зависит от расстояния между объектами. Таким образом, если расстояние очень маленькое, надписи будут двигаться больше. 
>>
>>В процессе также заметил, что некоторые объекты могут выходить за пределы графика, поэтому было принято решение сместить оси.
>>
>>Для каждого графика добавлена footer-подпись.

Код представлен в двух форматах: .py и .ipynb. В записной книжке вы можете увидеть шаги работы над заданиями более детально.
 
Все основные мысли прокомментированы, все указания к работе выполнены, а именно: 

1) Данные приведены к нужному виду и представлены в google spreadsheets;
2) Для каждой области была построена диаграма рассеивания с легендой и footer-подписью;  
3) Подписи объектов не пересекаются.

[Google spreadsheet](https://docs.google.com/spreadsheets/d/1cEyjHSZiWU_0LZoN3bFFlfEJKyVmueOOOJWkZ9aiA1Q/edit?usp=sharing "Первое задание")

[Visualisation](https://drive.google.com/drive/folders/1IpsqIzXs-mmrfa3K47a_uzP5Cz2fadct?usp=sharing "Второе задание")
