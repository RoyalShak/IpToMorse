import socket

host_name = socket.gethostname()
IPAddress = socket.gethostbyname(host_name)
print("Your Computer IP Address is:" + IPAddress)

MORSE_CODE_DICT = {'1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += ' '

    return cipher


def main():
    message = IPAddress
    result = encrypt(message.upper())
    print(result)


if __name__ == '__main__':
    main()
