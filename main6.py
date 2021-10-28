A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
C = int(input("Введите число C: "))


if __name__ == '__main__':
    var_1 = (A < 45) and (B >= 45) and (C >= 45)
    var_2 = (A >= 45) and (B < 45) and (C >= 45)
    var_3 = (A >= 45) and (B >= 45) and (C < 45)

    print("-----")
    print(var_1 or var_2 or var_3)
