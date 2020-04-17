# необходимо установить библиотеку pandas в текущем окружении
import pandas as pd
from sys import argv
from datetime import datetime
from dateutil.relativedelta import relativedelta


file = argv[1]


# форматируем datetime в строку нужного вида
def format (point):
    f_point = point.strftime('%H:%M')
    return f_point


# отнимаем 1 минуту от времени ухода клиента для нормализации результатов, т.к. фактически он пониул отделение
def m_min(end_time):
    dt_end = datetime.strptime(end_time, '%H:%M')
    down_min = dt_end - relativedelta(minutes=1)
    str_time = down_min.strftime('%H:%M')
    return str_time


# создаем пустой объект DataFrame с заданными названиями колонок и столбцов
index_time = pd.date_range('08:00', '20:00', freq='1min')
columns_frame = '1'
frame = pd.DataFrame(columns=list(columns_frame), index=index_time)

# загружаем из файлов данные и укладываем их в ранее созданный объект DataFrame
with open(file, 'r', encoding='utf-8') as f:
    i = 0
    for value in f:
        i = i + 1
        line = value.strip('\n')
        list_time = line.split(' ')
        time_start = list_time[0]
        time_end = m_min(list_time[1])
        index_time = pd.date_range(time_start, time_end, freq='1min')
        client_frame = pd.DataFrame(1, columns=[str(i)], index=index_time)
        frame[str(i)] = client_frame


# суммируем поминутно количество посетителей и сохраняем список минут, в которые число посетителей максимально
amount_period = frame.sum(axis=1)
max_clients = amount_period.max()
max_all_time = amount_period[amount_period == max_clients]
list_max_time = max_all_time.index


# определяем граничные значения периодов, в которые число посетителей максимально
time1 = datetime(2000, 1, 1, 0, 0, 0)
time2 = datetime(2000, 1, 1, 0, 1, 0)
min_1 = time2 - time1
list_result = []
list_result.append(list_max_time[0])
x = 0
try:
    for i in list_max_time:
        x = x + 1
        i_next = list_max_time[x]
        delta = i_next - i
        if delta != min_1:
            list_result.append(i)
            list_result.append(i_next)
except IndexError:
    pass
list_result.append(list_max_time[-1])


# производим обратную корректировку конечной точки каждого периода, добавляя 1 минуту, для повышения юзабилити
# формируем список откорректированных и отформатированных граничных значений и выводим в консоль
result_corrected = []
even = list_result[::2]
for point in list_result:
    if point in even:
        f_point = format(point)
        result_corrected.append(f_point)
        print(f_point + ' ', end="")
    else:
        corrected_point = point + min_1
        f_point = format(corrected_point)
        result_corrected.append(f_point)
        print(f_point)







