# Decorator Function Working
def decor(wish):
    def inner(name):
        if name == 'Sai':
            print('Hi',name,'Good Morning! Have Great Day..')
        else:
            wish(name)
    return inner
@decor
def wish(name):
    print('Hello',name,'Good Morning')
wish('Suraj')
wish('Sai')
wish('Madhavi')