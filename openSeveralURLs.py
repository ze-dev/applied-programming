'''Использовал для открытия сразу 20 разных url-ссылок,
когда размещал объявления в разных группах VK и авито.
Читает все из одного текстового файла в той же папке.'''

import webbrowser, time

with open('речь и размещение.txt','r') as stream:
    lines = stream.readlines()

url_list = []
for line in lines:
    if line.startswith('http'):
        url_list.append(line.split(' ')[0][:-1])

for url in url_list:
    webbrowser.open_new_tab(url)
    time.sleep(3)

input('Done.Press Enter..')
