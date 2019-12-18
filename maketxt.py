def maketxt(filename):
    '''Создает текстовый файл в директории запуска скрипта.
    В консоли вызывать maketxt.py НужноеИмяФайла (БЕЗ пробелов)'''
    import time, os
    with open('%s.txt' % filename, 'w') as ff:
        dirPath=os.getcwd()
        fullPath = '%s\%s' % (dirPath, filename)
        print('\nДиректория назначения вызова > %s ' % dirPath)
        print('\nФайл  %s.txt  создан...' % filename)
        time.sleep(2)

if __name__ == '__main__':
    import sys
    if len (sys.argv) > 1:
        parameter = sys.argv[1]
    else:
        parameter = input('Введите имя файла >  ')
    maketxt(parameter)
