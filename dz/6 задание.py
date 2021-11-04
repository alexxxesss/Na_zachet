
def count_it(sequence):
    list_seq = list(sequence)
    my_dict = {}
    for i in list_seq:
        if my_dict.get(int(i)):
            my_dict[int(i)] = my_dict[int(i)] + 1
        else:
            my_dict[int(i)] = 1
    return my_dict

def some_func(elem):
    return elem[1]


if __name__ == '__main__':
    a = input('Введите строку цифр от 0 до 9: ')
    print(dict(sorted(count_it(a).items(), key=some_func, reverse=True)[:3]))
