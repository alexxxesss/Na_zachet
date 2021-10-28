A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
C = int(input("Введите число C: "))
D = int(input("Введите число C: "))

def func_4(A, B, C, D):
    if A % 2 == 0:
        if B % 2 == 0:
            return True
        elif C % 2 == 0:
            return True
        elif D % 2 == 0:
            return  True
        else:
            return False
    elif B % 2 == 0:
        if C % 2 == 0:
            return  True
        elif D % 2 == 0:
            return True
        else:
            return  False
    elif C % 2 == 0 and D % 2 == 0:
        return True
    else:
        return False


if __name__ == '__main__':


    print("-----")
    print(func_4(A, B, C, D))

