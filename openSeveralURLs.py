'''Использовал для открытия сразу 20 разных url-ссылок,
когда размещал объявления в разных группах VK и авито.
Читает все из одного текстового файла в той же папке.
Исходный может быть вида, обработает линии только с line.startswith('http'):
выложил 21.06.20.
https://vk.com/bryansk_pogoda             в предложенных

'''

import webbrowser, time
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
filename = askopenfilename()

with open(filename,'r') as stream:
    lines = stream.readlines()

url_list = []
for line in lines:
    if line.startswith('http'):
        arr = line.split()
        if len(arr) > 0:
            use = arr[0]
        else:
            use = arr[0][:-1]
        url_list.append(use)

for url in url_list:
    #print(url)
    webbrowser.open_new_tab(url)
    time.sleep(3)

print('Done...')
time.sleep(2)
