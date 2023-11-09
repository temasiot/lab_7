from random import randint


def main():
    q = create(10)
    print(q)
    print('створений масив')
    out(q, 10)
    print('min = ', min_in_glow(q, 10, 101))
    pass


def create(q):
    return [[randint(0, 100) for i in range(q)] for j in range(q)]


def out(arr, q):
    for i in range(q):
        for j in range(q):
            print('{:>4}'.format(arr[i][j]), end="")
        print()
    pass


def min_in_glow(arr, q, w):
    for i in range(q):
        for j in range(q):
            if i == j:
                w = min(w, arr[i][j])
    return w


if __name__ == '__main__':
    main()
