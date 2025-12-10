Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#1
my_dict = {1.12: 'aa', 67.9: 45, 3.11: 'ccc', 7.9: 'dd', 9.2: 'ee',
7.1: 'ff', 0.12: 'qq', 1.91: 'aa', 10.12: [1, 2, 3], 99.0: {9, 0, 1}}

print(min(my_dict) + max(my_dict))

#2
users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

names = []

for u in users:
    phone = u['phone'].replace('+', '').replace('-', '')
    if phone[-1] == '8':   
        names.append(u['name'])

print(*sorted(names))

#3
users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]


names = []

for user in users:
    if 'email' not in user:
        names.append(user['name'])
    else:
        if user['email'] == '':
            names.append(user['name'])

names.sort()
print(' '.join(names))

#4
digits = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

num = input()

result = []

for char in num:
    word = digits[char]
    result.append(word)

print(' '.join(result))
#5

courses = {
    "CS101": ["3004", "Хайнс", "8:00"],
    "CS102": ["4501", "Альварадо", "9:00"],
    "CS103": ["6755", "Рич", "10:00"],
    "NT110": ["1244", "Берк", "11:00"],
    "CM241": ["1411", "Ли", "13:00"]
}

course = input().strip()

room, teacher, time = courses[course]
print(f"{course}: {room}, {teacher}, {time}")
#6
mapping = {
    '1': '.,?!:;-"()\'',
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ',
    '0': ' '
}

text = input()

result = []

for ch in text.upper():
    for key, letters in mapping.items():
        if ch in letters:
            presses = key * (letters.index(ch) + 1)
            result.append(presses)

print(*result)
#7
morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}

text = input()

result = []

for ch in text.upper():
    if ch == ' ':
        result.append('')
    elif ch in morse:
        result.append(morse[ch])

print(' '.join(result))
#8
result = {}

for i in range(11, 16):
    result[i] = i ** 2
#9
result = dict1.copy()

for k, v in dict2.items():
    if k in result:
        result[k] += v
    else:
        result[k] = v
#10
for ch in text:
    if ch in result:
        result[ch] += 1
    else:
        result[ch] = 1
#11
words = s.split()

count = {}
for w in words:
    if w in count:
        count[w] += 1
    else:
        count[w] = 1

max_count = max(count.values())

candidates = []
for w in count:
    if count[w] == max_count:
        candidates.append(w)

print(min(candidates))
... 
... #12
... for dog, name, surname, age in pets:
...     key = (name, surname, age)
...     result.setdefault(key, []).append(dog)
... 
... #13
... text = input().lower()
... 
... for ch in '.,!?:;-':
...     text = text.replace(ch, ' ')
... 
... words = text.split()
... 
... count = {}
... for w in words:
...     if w in count:
...         count[w] += 1
...     else:
...         count[w] = 1
... 
... min_count = min(count.values())
... candidates = []
... for w in count:
...     if count[w] == min_count:
...         candidates.append(w)
... print(min(candidates))
... #14
... ids = input().split()
... 
... used = {}
... res = []
... 
... for x in ids:
...     if x not in used:
...         used[x] = 0
...         res.append(x)
...     else:
...         used[x] += 1
...         res.append(f'{x}_{used[x]}')
... 
