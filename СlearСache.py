import pyperclip,time
t = input('Сформируем адрес доступа к кешу.\nТерминал?\n')
c = input('Пользователь Windows?\n')
an='\\\\{}\\c$\\Users\\{}\\AppData\\'.format(t,c)
pyperclip.copy(an)
print('Адрес скопирован в буфер: \n'+an)
time.sleep(2)
