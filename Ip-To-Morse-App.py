from flask import Flask, request

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
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


def holyflask():
    app = Flask(__name__)
    iptomorse = open("connections.txt").read()

    @app.route("/")
    @app.route("/home")
    def home():
        r = request.remote_addr
        r2 = encrypt(r.upper())
        f = open('connections.txt', 'w')
        f.write(f"Client IP {r}\n")
        f.write(f"IP to Morse {encrypt(r.upper())}\n")
        f.close()
        return iptomorse, r2

    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=8081)


holyflask()
