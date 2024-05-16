import os


def thats_the_name(dir_path):
    thats_the_files = []
    files = os.listdir(dir_path)

    for file in files:
        if file.startswith('deep'):
            thats_the_files.append(file)

    return thats_the_files


def main():
    path = input("Please enter a valid path: ")

    res = thats_the_name(path)
    print('The matching files are: ', res)


if __name__ == "__main__":
    main()
