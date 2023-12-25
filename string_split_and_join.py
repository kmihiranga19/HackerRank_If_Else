def split_and_join(line):
    text_lst = line.split()
    join = "-".join(text_lst)

    return join

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


