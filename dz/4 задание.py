def all_eq(lst):
    max_symbol = 0
    for i in range(len(lst)):
        if len(lst[i]) > max_symbol:
            max_symbol = len(lst[i])
    print(max_symbol)

    new_lst = []
    for i in lst:
        if len(i) == max_symbol:
            new_lst.append(i)
        else:
            new_lst.append(i.ljust(max_symbol, '_'))

    print(new_lst)



if __name__ == '__main__':
    list_str = list(input("Введите строки: ").split())
    all_eq(list_str)
