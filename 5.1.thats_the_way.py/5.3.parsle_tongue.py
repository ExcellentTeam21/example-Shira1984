import string


def binary_tongue(file_name):
    with open('logo.jpg', 'rb') as f:
        binary_file = f.read()

    secret_messages = []
    current_message = []

    in_message = False
    for byte in binary_file:
        if byte in range(97, 123):
            if not in_message:
                in_message = True
            current_message.append(chr(byte))
        elif byte == 33:
            if in_message and len(current_message) >= 5:
                yield ''.join(current_message)
            current_message = []
            in_message = False
        else:
            current_message = []
            in_message = False


def main():
    for secret in binary_tongue('logo.jpg'):
        print(secret)


if __name__ == '__main__':
    main()