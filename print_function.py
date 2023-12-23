if __name__ == '__main__':
    n = int(input())

    lists = list(range(1, n + 1))
    strList = ''.join(str(list) for list in lists)
    print(strList)
