def more_than_five(lst):
    lst_int = [int(i) for i in lst]
    return [x for x in lst_int if x > 5 or x < -5]


if __name__ == '__main__':
    a = input('Введите несколько целых чисел через пробел: ').split()
    print(more_than_five(a))