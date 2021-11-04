def search_substr(subst, st):

    # if subst.lower() in st.lower():
    #     return 'Есть контакт!'
    # else:
    #     return 'Мимо!'

    # Второе решение:

    st_low = st.lower()
    subst_low = subst.lower()
    if st_low.find(subst_low) != -1:
        return 'Есть контакт!'
    else:
        return 'Мимо!'


if __name__ == '__main__':
    a = input('Введите строку, в которой необходимо выполнить поиск: ')
    b = input('Введите подстроку, которую хотите найти: ')
    print(search_substr(b, a))
