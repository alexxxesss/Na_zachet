def to_dict(lst):
    dict_lst = {}
    for i in lst:
        dict_lst[i] = i
    print(dict_lst)


if __name__ == '__main__':
    list_str = list(input("Введите строки: ").split())
    to_dict(list_str)
