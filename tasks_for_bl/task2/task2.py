from sys import argv
from math import sqrt, fabs


# преобразуем текстовые файлы в список списков координат вершин четырехугольника и данных точек
def convert_to_coordinates(data):
    data = data.split('\n')
    del data[-1]
    list_vertex = []
    for point in data:
        point = point.split(' ')
        coordinates = []
        for value in point:
            value = float(value)
            coordinates.append(value)
        list_vertex.append(coordinates)
    return list_vertex


# рассчитываем длину отрезка по координатам двух точек
def length (a, b):
    len_segment = sqrt(
        (fabs(b[0] - a[0]))**2 +
        (fabs(b[1] - a[1]))**2
    )
    return len_segment


# рассчитываем площадь треугольника по координатам трех известных вершин
def area_triangle (a, b, c):
    s = fabs((b[0]-a[0])*(c[1]-a[1]) - (c[0]-a[0])*(b[1]-a[1])) / 2
    return s

# проверяем принадлежит ли данная точка отрезку соединяющему точки a и b (возвращаем 0).
# если это так, то проверяем совпадает ли данная точка с начальной либо конечной точками отрезка (возвращаем 1)
# если данная точка не принадлежит отрезку (возвращаем False)
def check_accessory(a, b, x):
    L = length(a, b)
    l1 = length(a, x)
    l2 = length(b, x)
    if L == (l1 + l2):
        if x == a:
            return '0'
        elif x == b:
            return '0'
        else:
            return '1'
    else:
        return False


quadrangle = argv[1]
points_ = argv[2]

# сохраняем координаты вершин четырехугольника в список a
with open(quadrangle, 'r', encoding='utf-8') as f:
    a = convert_to_coordinates(f.read())

# сохраняем координаты данных точек в список b
with open(points_, 'r', encoding='utf-8') as f:
    b = convert_to_coordinates(f.read())


# рассчитываем площадь четырехугольника (s_quadrangle):
a1 = length(a[0], a[1])
a2 = length(a[1], a[2])
a3 = length(a[2], a[3])
a4 = length(a[3], a[0])
p = (a1+a2+a3+a4)/2
s_quadrangle = sqrt((p-a1)*(p-a2)*(p-a3)*(p-a4))


# проверяем перебором принадлежит ли данная точка каждой из сторон четырехугольника
for point in b:
    z = check_accessory(a[0], a[1], point)
    if z == False:
        z = check_accessory(a[1], a[2], point)
        if z == False:
            z = check_accessory(a[2], a[3], point)
            if z == False:
                z = check_accessory(a[3], a[0], point)
                if z == False:
                    # рассчитываем сумму площадей треугольников (sum_s_triangle), вершинами которого являются
                    # данная точка и две из четырех вершин данного четырехугольника:
                    s1 = area_triangle(a[0], a[1], point)
                    s2 = area_triangle(a[1], a[2], point)
                    s3 = area_triangle(a[2], a[3], point)
                    s4 = area_triangle(a[3], a[0], point)
                    sum_s_triangle = s1 + s2 + s3 + s4
                    if s_quadrangle == sum_s_triangle:
                        print('2')
                    else:
                        print('3')
            else:
                print(z)
        else:
            print(z)
    else:
        print(z)




