if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(all([
        all(int(x) >= 0 for x in arr),
        any(str(x) == str(x)[::-1] for x in arr)
        ]))

