# *-* encoding: utf-8 *-*

import os

with open('model.py', 'r', encoding='utf-8') as f:
    model = f.read()

fucks = []
descriptions = []
files = []

for fuck in os.listdir('fucks'):
    if not fuck.endswith('.py'):
        continue
    filename = os.path.join('fucks', fuck)[:-3]

    with open(filename + '.py', 'r', encoding='utf-8') as f:
        fucks.append(f.read())
    files.append(filename)
    if not os.path.exists(filename + '.txt'):
        descriptions.append('')
    else:
        with open(filename + '.txt', 'r', encoding='utf-8') as f:
            descriptions.append(f.read())

with open('main.py', 'w', encoding='utf-8') as f:
    f.write(model.replace('fucks = []', 'fucks = {}'.format(fucks))
                 .replace('descriptions = []', 'descriptions = {}'.format(descriptions))
                 .replace('filenames = []', 'filenames = {}'.format(files)))
