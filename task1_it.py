from random import randint


def main():
    print('створений масив')
    q = create(7, 6)
    out(q, 7, 6)
    print('масив після змін')
    q, w, e = sum_za_cruterijamu(q, 7, 6, 0, 0)
    out(q, 7, 6)
    print('сума =', '{:>4}'.format(w))
    print('кількість просумованих елементів =', '{:>4}'.format(e), end='\n\n')
    print('створений масив')
    q = create(7, 6)
    out(q, 7, 6)
    print('масив після змін')
    sort(q, 7, 0)
    out(q, 7, 6)
    pass


def create(q, w):
    return [[randint(-42, 51) for i in range(w)] for j in range(q)]


def out(arr, q, w):
    for i in range(q):
        for j in range(w):
            print('{:>4}'.format(arr[i][j]), end="")
        print()
    pass


def sum_za_cruterijamu(arr, q, w, e, r):
    for i in range(q):
        for j in range(w):
            if not(arr[i][j] > 0 and arr[i][j] % 5 == 0):
                e += arr[i][j]
                arr[i][j] = 0
                r += 1
    return arr, e, r


def sort(arr, q, r):
    if r % 2 == 0:
        y = list()
        for i in range(q - 1):
            for j in range(q - i - 1):
                if arr[j][r] > arr[j + 1][r]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            y.append(arr[j+1][r])
        y.append(arr[j][r])
        if r == 2:
            return arr
        elif len(y) != len(set(y)):
            return sort(arr, q, r+1)
        else:
            return arr
    else:
        y = list()
        for i in range(q - 1):
            for j in range(q - i - 1):
                if arr[j][r] < arr[j + 1][r]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            y.append(arr[j + 1][r])
        y.append(arr[j][r])
        if r == 2:
            return arr
        elif len(y) != len(set(y)):
            return sort(arr, q, r + 1)
        else:
            return arr


if __name__ == '__main__':
    main()
