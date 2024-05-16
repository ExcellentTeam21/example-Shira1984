def join(*lists, sep='-'):
    final_list = []
    for l in lists:
        final_list.extend(l)
        final_list.append(sep)

    if not final_list:
        return 'None'

    return final_list[:-1]


def main():
    print(join())


if __name__ == '__main__':
    main()
