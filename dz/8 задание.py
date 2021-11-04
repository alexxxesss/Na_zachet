def first_last(letter, st):
    result_list = []
    st_low = st.lower()
    letter_low = letter.lower()

    if letter_low in st_low:
        result_list.append(st_low.find(letter_low))
        result_list.append(st_low.rfind(letter_low))
    else:
        result_list.extend([None, None])

    return tuple(result_list)


if __name__ == '__main__':
    a = input('Введите строку, в которой необходимо выполнить поиск буквы: ')
    b = input('Введите букву, индексы первого и последнего вхождения которой хотите найти: ')
    print(first_last(b, a))
