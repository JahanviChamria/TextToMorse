
MORSE_CODE_DICT = { 'A' :'.-', 'B' :'-...',
                    'C' :'-.-.', 'D' :'-..', 'E' :'.',
                    'F' :'..-.', 'G' :'--.', 'H' :'....',
                    'I' :'..', 'J' :'.---', 'K' :'-.-',
                    'L' :'.-..', 'M' :'--', 'N' :'-.',
                    'O' :'---', 'P' :'.--.', 'Q' :'--.-',
                    'R' :'.-.', 'S' :'...', 'T' :'-',
                    'U' :'..-', 'V' :'...-', 'W' :'.--',
                    'X' :'-..-', 'Y' :'-.--', 'Z' :'--..',
                    '1' :'.----', '2' :'..---', '3' :'...--',
                    '4' :'....-', '5' :'.....', '6' :'-....',
                    '7' :'--...', '8' :'---..', '9' :'----.',
                    '0' :'-----', ', ' :'--..--', '.' :'.-.-.-',
                    '?' :'..--..', '/' :'-..-.', '-' :'-....-',
                    '(' :'-.--.', ')' :'-.--.-', ' ':' '}


st=input("Enter the sentence to be converted: ")
s=st.upper()
morse=""
for letter in s:
    morsec=MORSE_CODE_DICT[letter]
    morse=morse+morsec

print(f"Morse Code Equivalent: {morse}")