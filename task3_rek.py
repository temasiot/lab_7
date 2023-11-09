def main():
    n = int(input('n = '))
    q = create(n, [], 0)
    r = []
    out(q, n, 0, 0)
    decide(q, n, r, 0, 0, [])
    if len(r) > 0:
        print('k = ', end="")
        out_list(r, len(r), 0)
        print()
    else:
        print('відсутні однакові рядки')
    is_have_negative(q, n, 0, 0, 0)
    pass


def create(q, e, i):
    e.append(list(map(int, input(f'рядок {i+1} = ').split())))
    if i < q - 1:
        e = create(q, e, i+1)
    return e


def out(arr, q, i, j):
    print('{:>4}'.format(arr[i][j]), end="")
    if j < q-1:
        out(arr, q, i, j+1)
    else:
        print()
        if i < q-1:
            out(arr, q, i + 1, 0)
    pass


def out_list(arr, q, i):
    print('{:>4}'.format(arr[i]), end="")
    if i < q-1:
        out_list(arr,q, i+1)
    pass


def decide(arr, q, w, i, j, e):
    e.append(arr[j][i])
    if arr[i] == e:
        w.append(i)
    if j < q - 1:
        decide(arr, q, w, i, j + 1, e)
    elif i < q - 1:
        decide(arr, q, w, i + 1, 0, [])
    pass


def is_have_negative(arr, q, w, i, j) -> int:
    if arr[i][j] < 0:
        print('сума =', '{:>4}'.format(sum_line(arr, q, i, 0, 0)))
    else:
        w += 1
    if w == q * q:
        print('відсутні відємні значення')
    elif j < q - 1:
        is_have_negative(arr, q, w, i, j+1)
    elif i < q - 1:
        is_have_negative(arr, q, w, i+1, 0)
    return 0


def sum_line(arr, q, w, e, i) -> int:
    e += arr[w][i]
    if i < q-1:
        e = sum_line(arr, q, w, e, i+1)
    return e


if __name__ == '__main__':
    main()
