m = int(input())


def to_bin(n: int) -> [int]:
    s = []
    while n > 0:
        s.append(n & 1)
        n >>= 1
    return list(reversed(s))


def main(p):
    if p >= 0:
        return to_bin(p).count(1)
    else:
        l = to_bin(-p)
        f = [1] + [int(not i) for i in l]
        if f[-1] == 0:
            f[-1] = 1
        else:
            for i in range(len(f) - 1, 0, -1):
                if f[i] == 1:
                    f[i] = 0
                else:
                    f[i] = 1
                    break
        return f.count(1)


assert main(10) == 2
assert main(-123) == 3

if __name__ == '__main__':
    print(main(m))