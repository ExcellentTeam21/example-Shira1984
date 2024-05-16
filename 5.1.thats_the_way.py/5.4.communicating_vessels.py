def interleave(*args):
    max_length = max(len(arg) for arg in args)

    for i in range(max_length):
        for arg in args:
            if i < len(arg):
                yield arg[i]


def main():
    result = list(interleave('abc', [1, 2, 3], ('!', '@', '#')))
    print(result)


if __name__ == '__main__':
    main()

