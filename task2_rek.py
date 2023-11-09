from random import randint


def main():
    o, q = create(10, [], [])
    print('створений масив')
    out(q, 10, 0, 0)
    print('min =', min_in_glow(q, 10, 101, 0, 0))
    pass


def create(q, arr, fin):
    arr.append(randint(0, 100))
    if len(arr) < q:
        arr, fin = create(q, arr, fin)
    if len(fin) < q:
        fin.append(arr)
        arr, fin = create(q, [], fin)
    return arr, fin


def out(arr, q, i, j):
    print('{:>4}'.format(arr[i][j]), end="")
    if j < q-1:
        out(arr, q, i, j+1)
    else:
        print()
        if i < q-1:
            out(arr, q, i + 1, 0)
    pass


def min_in_glow(arr, q, w, i, j):
    if i == j:
        w = min(w, arr[i][j])
    if j < q - 1:
        w = min_in_glow(arr, q, w, i, j+1)
    elif i < q - 1:
        w = min_in_glow(arr, q, w, i+1, 0)
    return w


if __name__ == '__main__':
    main()
