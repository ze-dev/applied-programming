def getpath():
    import os
    import pyperclip
    a = os.getcwd() + '\\'
    pyperclip.copy(a)
    pyperclip.paste()
    input('В буфер скопирован путь >  \n%s ' % a)

if __name__ == '__main__':
    getpath()
    
    
