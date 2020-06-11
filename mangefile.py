import os

def wir():
    print('Write in the file')
    x = open(input('Enter name file :' ) , 'w')
    x.write(input('Enter text for writing : '))
    print('Done...')
    Interface()
    ######
def r():
    print('Read The file')
    x = open(input('Enter file name : '), 'r')
    print(x.read())
    Interface()
    ######
def c():
    print('Create file')
    open(input('Enter name file : ') , 'a')
    print('Done...')
    Interface()
    ######
def re():
    print('Remove file')
    os.remove(input('Enter name file :' ))
    print('Done...')
    Interface()
    ######
def ch():
    print('Change name file')
    os.rename(input('Enter old name file : ') , input('New name file : '))
    print('Done...')
    Interface()
    ######
def sc():
    print('The file does exist')
    os.path.exists(input('Enter name file : '))
    print('Done...')
    Interface()
    ######
def cf():
    print('Creat folder')
    os.mkdir(input('Enter name folder : '))
    print('Done...')
    Interface()
    ######
def df():
    print('Remove folder')
    os.rmdir(input('Entar folder file : '))
    print('Done...')
    Interface()
    ######
def Interface():
    print('''''')
    print('Manger file simply :)')
    print('''
    Create file = 1
    Change name file = 2
    Remove file = 3
    Creat folder = 4
    Remove folder = 5
    The file does exist = 6
    Read file = 7
    Write in the file = 8''')
    print('')
    z = int(input('Choose : '))
    if z == 1:
        c()
    elif z == 2:
        ch()
    elif z == 3:
        re()
    elif z == 4:
        cf()
    elif z == 5:
        df()
    elif z == 6:
        sc()
    elif z == 7:
        r()
    elif z == 8:
        wir()
    else :
        print('You Did Choose')

#

print('''programming by devil
    Snap : pz_a9
    IG : qq.hk''')
input('Click Inter to continue...')
Interface()
