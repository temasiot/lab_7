def main():
    n = int(input('n = '))
    q = create(n, [])
    r = []
    out(q, n)
    decide(q, n, r)
    if len(r) > 0:
        out_list(r, len(r))
    else:
        print('відсутні однакові рядки')
    is_have_negative(q, n, 0)
    pass


def create(q, e):
    for i in range(q):
        e.append(list(map(int, input(f'рядок {i+1} = ').split())))
    return e


def out(arr, q):
    for i in range(q):
        for j in range(q):
            print('{:>4}'.format(arr[i][j]), end="")
        print()
    pass


def out_list(arr, q):
    for i in range(q):
        print('k =', '{:>4}'.format(arr[i]), end="")
    print()
    pass


def decide(arr, q, w):
    for i in range(q):
        e = list()
        for j in range(q):
            e.append(arr[j][i])
        if arr[i] == e:
            w.append(i)
    pass


def is_have_negative(arr, q, w) -> int:
    for i in range(q):
        for j in range(q):
            if arr[i][j] < 0:
                print('сума =', '{:>4}'.format(sum_line(arr, q, i)))
            else:
                w += 1
    if w == q * q:
        print('відсутні відємні значення')
    return 0


def sum_line(arr, q, w) -> int:
    e = 0
    for i in range(q):
        e += arr[w][i]
    return e


if __name__ == '__main__':
    main()
