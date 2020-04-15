# необходимо установить в текущем виртуальном окружении модуль numpy
from numpy import percentile
from sys import argv


def format (value):
    format_value = "%.2f" % value
    return format_value


data = argv[1]

with open(data, 'r', encoding='utf-8') as f:
    line = []
    for value in f:
        i = float(value)
        line.append(i)
line.sort()
len_line = len(line)
sum_line = sum(line)


# 90 перцентиль
value_perc = percentile(line, 90)
format_perc = format(value_perc)
print(format_perc)


# медиана
if len_line % 2 == 0:
    median1 = line[len_line//2]
    median2 = line[len_line // 2-1]
    median = (median1 + median2)/2
else:
    median = line[len_line//2]
format_med = format(median)
print(format_med)


# максимальное значение
value_max = max(line)
format_max = format(value_max)
print(format_max)


# минимальное значение
value_min = min(line)
format_min = format(value_min)
print(format_min)


# среднее значение
average = sum_line / len_line
format_ave = format(average)
print(format_ave)