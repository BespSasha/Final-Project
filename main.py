import tkinter as tk

root = tk.Tk()
root.title('Шифрування та розшифрування')
photo = tk.PhotoImage(file='SF.png')
root.iconphoto(False, photo)
root.geometry('500x300+510+200')
root['bg'] = '#A58D37'

choice_var = tk.IntVar()

label1 = tk.Label(root, text="Введіть своє речення у поле нижче:", font="Courier 10", bg='#A58D37', fg='#00FAD3')
label1.pack()

entry = tk.Entry(bg='#A58D37', fg='#00FAD3', font='Courier 10')
entry.pack()

label2 = tk.Label(root, text="Введіть ключ:", bg='#A58D37', fg='#00FAD3', font='Courier 10')
label2.pack()

entry2 = tk.Entry(bg='#A58D37', fg='#00FAD3', font='Courier 10')
entry2.pack()

radio_button1 = tk.Radiobutton(root, bg='#A58D37', fg='#00FAD3', text="Шифр Цезаря", variable=choice_var, value=1,
                               font="Courier 10")
radio_button1.pack()
radio_button2 = tk.Radiobutton(root, bg='#A58D37', fg='#00FAD3', text="Шифр Віженера", variable=choice_var, value=2,
                               font="Courier 10")
radio_button2.pack()

label3 = tk.Label(root, text="Зашифроване речення(розшифроване):", bg='#A58D37', fg='#00FAD3', font="Courier 10")
label3.pack()
entry3 = tk.Entry(bg='#A58D37', fg='#00FAD3', font='Courier 10')
entry3.pack()
label4 = tk.Label(root, bg='#A58D37', fg='#00FAD3', font="Courier 10")
label4.pack()

letter_to_digit = {
    'А': '0',
    'Б': '1',
    'В': '2',
    'Г': '3',
    'Ґ': '4',
    'Д': '5',
    'Е': '6',
    'Є': '7',
    'Ж': '8',
    'З': '9',
    'И': '10',
    'І': '11',
    'Ї': '12',
    'Й': '13',
    'К': '14',
    'Л': '15',
    'М': '16',
    'Н': '17',
    'О': '18',
    'П': '19',
    'Р': '20',
    'С': '21',
    'Т': '22',
    'У': '23',
    'Ф': '24',
    'Х': '25',
    'Ц': '26',
    'Ч': '27',
    'Ш': '28',
    'Щ': '29',
    'Ь': '30',
    'Ю': '31',
    'Я': '32',
    'а': '33',
    'б': '34',
    'в': '35',
    'г': '36',
    'ґ': '37',
    'д': '38',
    'е': '39',
    'є': '40',
    'ж': '41',
    'з': '42',
    'и': '43',
    'і': '44',
    'ї': '45',
    'й': '46',
    'к': '47',
    'л': '48',
    'м': '49',
    'н': '50',
    'о': '51',
    'п': '52',
    'р': '53',
    'с': '54',
    'т': '55',
    'у': '56',
    'ф': '57',
    'х': '58',
    'ц': '59',
    'ч': '60',
    'ш': '61',
    'щ': '62',
    'ь': '63',
    'ю': '64',
    'я': '65',
}

digit_to_letter = {
    '0': 'А',
    '1': 'Б',
    '2': 'В',
    '3': 'Г',
    '4': 'Ґ',
    '5': 'Д',
    '6': 'Е',
    '7': 'Є',
    '8': 'Ж',
    '9': 'З',
    '10': 'И',
    '11': 'І',
    '12': 'Ї',
    '13': 'Й',
    '14': 'К',
    '15': 'Л',
    '16': 'М',
    '17': 'Н',
    '18': 'О',
    '19': 'П',
    '20': 'Р',
    '21': 'С',
    '22': 'Т',
    '23': 'У',
    '24': 'Ф',
    '25': 'Х',
    '26': 'Ц',
    '27': 'Ч',
    '28': 'Ш',
    '29': 'Щ',
    '30': 'Ь',
    '31': 'Ю',
    '32': 'Я',
    '33': 'а',
    '34': 'б',
    '35': 'в',
    '36': 'г',
    '37': 'ґ',
    '38': 'д',
    '39': 'е',
    '40': 'є',
    '41': 'ж',
    '42': 'з',
    '43': 'и',
    '44': 'і',
    '45': 'ї',
    '46': 'й',
    '47': 'к',
    '48': 'л',
    '49': 'м',
    '50': 'н',
    '51': 'о',
    '52': 'п',
    '53': 'р',
    '54': 'с',
    '55': 'т',
    '56': 'у',
    '57': 'ф',
    '58': 'х',
    '59': 'ц',
    '60': 'ч',
    '61': 'ш',
    '62': 'щ',
    '63': 'ь',
    '64': 'ю',
    '65': 'я',
}


def letters_to_digits(rechennya, keyword):
    result = ""
    keyword_length = len(keyword)

    for i in range(len(rechennya)):
        char = rechennya[i]
        if char in letter_to_digit:
            char_value = int(letter_to_digit[char])
            keyword_char = keyword[i % keyword_length]
            keyword_value = int(letter_to_digit[keyword_char])
            encrypted_value = (char_value + keyword_value) % 66
            result += str(encrypted_value) + ' '
        else:
            result += char

    return result


def digits_to_letters(rechennya, keyword):
    result = ""
    i = 0
    keyword_length = len(keyword)

    while i < len(rechennya):
        if rechennya[i].isdigit():
            num = rechennya[i]
            while i + 1 < len(rechennya) and rechennya[i + 1].isdigit():
                num += rechennya[i + 1]
                i += 1
            num = int(num)
            keyword_char = keyword[i % keyword_length]
            keyword_value = int(letter_to_digit[keyword_char])
            decrypted_value = (num - keyword_value) % 66
            result += digit_to_letter[str(decrypted_value)]
        else:
            result += rechennya[i]
        i += 1

    return result


def encryption():
    keyword = entry2.get()
    rechennya = entry.get()
    output_string = letters_to_digits(rechennya, keyword)
    entry3.delete(0, tk.END)
    entry3.insert(0, output_string)


def decryption():
    rechennya = entry.get()
    keyword = entry2.get()
    output_string = digits_to_letters(rechennya, keyword)
    entry3.delete(0, tk.END)
    entry3.insert(0, output_string)


button1 = tk.Button(root, bg='#A58D37', fg='#00FAD3', text="Зашифрувати", command=encryption, width=20,
                    font="Courier 10")
button1.pack()
button2 = tk.Button(root, bg='#A58D37', fg='#00FAD3', text="Розшифрувати", command=decryption, width=20,
                    font="Courier 10")
button2.pack()

root.mainloop()
