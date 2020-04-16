# необходимо установить библиотеку pandas в текущем окружении
import pandas as pd
from sys import argv

directory = argv[1]

# создаем пустой объект DataFrame с заданными названиями колонок и столбцов
index_frame = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
columns_frame = '12345'
frame = pd.DataFrame(columns=list(columns_frame), index=index_frame)

# загружаем из файлов данные и укладываем их в ранее созданный объект DataFrame
for x in range(1, 6):
    address = './' + str(directory) + '/Cash' + str(x) + '.txt'
    x = str(x)
    with open(address, 'r', encoding='utf-8') as f:
        line = []
        for value in f:
            i = float(value)
            line.append(i)
        frame_cash = pd.DataFrame(line, columns=list(x), index=index_frame)
        frame[str(x)] = frame_cash

# создаем объект Series с суммами значений по кассам для каждого периода и выводим номер первого полученного периода,
# в котором сумма значений максимальна
amount_period = frame.sum(axis=1)
period_max = amount_period.idxmax()
print(period_max)




