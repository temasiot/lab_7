from random import randint


def main():
    print('створений масив')
    o, q = create(7, 6, [], [])
    out(q, 7, 6, 0, 0)
    print('масив після змін')
    q, w, e = sum_za_cruterijamu(q, 7, 6, 0, 0, 0, 0)
    out(q, 7, 6, 0, 0)
    print('сума =', '{:>4}'.format(w))
    print('кількість просумованих елементів =', '{:>4}'.format(e), end='\n\n')
    print('створений масив')
    o, q = create(7, 6, [], [])
    out(q, 7, 6, 0, 0)
    print('масив після змін')
    sort(q, 7, 0, 0, 0)
    out(q, 7, 6, 0, 0)
    pass


def create(q, w, arr, fin):
    arr.append(randint(-42, 51))
    if len(arr) < w:
        arr, fin = create(q, w, arr, fin)
    if len(fin) < q:
        fin.append(arr)
        arr, fin = create(q, w, [], fin)
    return arr, fin


def out(arr, q, w, i, j):
    print('{:>4}'.format(arr[i][j]), end="")
    if j < w-1:
        out(arr, q, w, i, j+1)
    else:
        print()
        if i < q-1:
            out(arr, q, w, i + 1, 0)
    pass


def sum_za_cruterijamu(arr, q, w, e, r, i, j):
    if not(arr[i][j] > 0 and arr[i][j] % 5 == 0):
        e += arr[i][j]
        arr[i][j] = 0
        r += 1
    if j < w - 1:
        arr, e, r = sum_za_cruterijamu(arr, q, w, e, r, i, j+1)
    elif i < q - 1:
        arr, e, r = sum_za_cruterijamu(arr, q, w, e, r, i+1, 0)
    return arr, e, r


def sort(arr, q, r, i, j):
    if r % 2 == 0:
        y = list()
        if arr[j][r] > arr[j + 1][r]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if j < q - i - 1 - 1:
            sort(arr, q, r, i, j + 1)
        elif i < q - 1 - 1:
            y.append(arr[j + 1][r])
            sort(arr, q, r, i + 1, 0)
        y.append(arr[j][r])
        if r == 2:
            return arr
        elif len(y) != len(set(y)):
            return sort(arr, q, r+1, 0, 0)
        else:
            return arr
    else:
        y = list()
        if arr[j][r] < arr[j + 1][r]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if j < q - i - 1 - 1:
            sort(arr, q, r, i, j + 1)
        elif i < q - 1 - 1:
            y.append(arr[j + 1][r])
            sort(arr, q, r, i + 1, 0)
        y.append(arr[j][r])
        if r == 2:
            return arr
        elif len(y) != len(set(y)):
            return sort(arr, q, r + 1, 0, 0)
        else:
            return arr


if __name__ == '__main__':
    main()
