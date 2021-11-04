def list_sort(lst):
    print(lst)
    new_lst = [int(x) for x in lst]
    new_lst.sort(reverse=True)
    print(new_lst)


if __name__ == '__main__':
    list_ = list(input('Введите числа через пробел: ').split())
    list_sort(list_)
    