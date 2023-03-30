import pandas as pd

def string_to_morse(text):
    morse_code = ""
    df = pd.read_csv('morse_code.csv')
    morse_table = df.to_dict('list')
    
    pos = 0 
    for a in answer:
        if a.upper() in morse_table['Letters']:
            pos = morse_table['Letters'].index(a.upper())
            morse_code += morse_table['Morse'][pos] + ' '
        elif a == '.':
            pos = morse_table['Letters'].index('Period')
            morse_code += morse_table['Morse'][pos] + ' '
        elif a == ',':
            pos = morse_table['Letters'].index('Comma')
            morse_code += morse_table['Morse'][pos] + ' '
        elif a == ' ':
            morse_code += '   '
    print(morse_code)

ask = True

print('Welcome to the simple text to morse code converter.\n')

while ask:
    answer = input('Type text to convert and press enter (leave blank to end program): ')
    
    if len(answer) > 0:
        string_to_morse(text=answer)
    else: ask = False