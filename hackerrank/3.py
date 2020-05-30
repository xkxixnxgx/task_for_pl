if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())


    arr = list(arr)
    list_unique = list(set(arr))
    list_unique.sort()

    if len(list_unique) == 1:
        print(list_unique[-1])
    else:
        print(list_unique[-2])


