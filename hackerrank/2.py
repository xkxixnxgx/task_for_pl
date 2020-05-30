if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())


    def sum_coord(a, b, c, n):
        sum_int = a + b + c
        if sum_int != n:
            pr_list = [a, b, c]
            result_list.append(pr_list)
        return


    a = range(0, x + 1)
    b = range(0, y + 1)
    c = range(0, z + 1)

    result_list = []

    for ax in a:
        for bx in b:
            for cx in c:
                sum_coord(ax, bx, cx, n)

    print(result_list)
