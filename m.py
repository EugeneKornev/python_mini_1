n = int(input())


def to_bin(m: int) -> int:
    k = 0
    while m > 0:
        k += (m & 1)
        m >>= 1
    return k


def main(a: int) -> int:
    if a >= 0:
        return to_bin(a)
    else:
        b = 0
        while - 2 ** b > a:
            b += 1
        return 1 + to_bin(2 ** b + a)


assert main(0) == 0
assert main(10) == 2
assert main(-123) == 3

if __name__ == '__main__':
    print(main(n))
