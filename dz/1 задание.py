def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    print(lst)


if __name__ == '__main__':

    str_ = input('Введите список: ')
    list_ = list(str_.split())
    change(list_)
