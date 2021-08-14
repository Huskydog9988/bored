# Super crude but gets the job done
alphabet = {
    "a": "ALFA",
    "b": "BRAVO",
    "c": "CHARLIE",
    "d": "DELTA",
    "e": "ECHO",
    "f": "FOXTROT",
    "g": "GOLF",
    "h": "HOTEL",
    "i": "INDIA",
    "j": "JULIETT",
    "k": "KILO",
    "l": "LIMA",
    "m": "MIKE",
    "n": "NOVEMBER",
    "o": "OSCAR",
    "p": "PAPA",
    "q": "QUEBEC",
    "r": "ROMEO",
    "s": "SIERRA",
    "t": "TANGO",
    "u": "UNIFORM",
    "v": "VICTOR",
    "w": "WHISKEY",
    "x": "X-RAY",
    "y": "YANKEE",
    "z": "ZULU",
}


def main():
    message = input("Your message: ")
    translated = ""
    for char in message:
        char = char.lower()
        if char in alphabet.keys():
           translated += alphabet[char]
           translated += " " 
        else:
            translated += char
    
    print(translated)

if __name__ == "__main__":
    main()
