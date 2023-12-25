def print_full_name(first, last):
    first_name = str(first)
    last_name = str(last)

    text = "Hello {} {}! You just delved into python.".format(first_name, last_name)

    print(text)

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)