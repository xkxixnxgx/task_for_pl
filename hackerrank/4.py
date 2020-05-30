if __name__ == '__main__':
    list_rank = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_rank = [name, score]
        list_rank.append(name_rank)
    len_rank = len(list_rank)
    quantity = range(len_rank - 1)
    value_list = []
    for x in quantity:
        value_list.append(list_rank[x][1])
    value_list.sort()
    min2 = value_list[-2]
    final_list = []
    for x in quantity:
        if list_rank[x][1] == min2:
            final_list.append(list_rank[x][0])
    for x in final_list:
        print(x)


