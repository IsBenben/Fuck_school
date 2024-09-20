# *-* encoding: utf-8 *-*

import os

with open('model.py', 'r', encoding='utf-8') as f:
    model = f.read()

fucks = []
descriptions = []

for fuck in os.listdir('fucks'):
    if not fuck.endswith('.py'):
        continue
    with open(os.path.join('fucks', fuck), 'r', encoding='utf-8') as f:
        fucks.append(f.read())
    
    description_name = os.path.join('fucks', fuck[:-3] + '.txt')
    if not os.path.exists(description_name):
        descriptions.append('')
    else:
        with open(description_name, 'r', encoding='utf-8') as f:
            descriptions.append(f.read())

with open('main.py', 'w', encoding='utf-8') as f:
    f.write(model.replace('fucks = []', 'fucks = {}'.format(fucks))
                 .replace('descriptions = []', 'descriptions = {}'.format(descriptions)))
