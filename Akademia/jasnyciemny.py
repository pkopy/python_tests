
def jasnyciemny(kolor =['ciemny']):
    
    
    if kolor[0] == 'jasny':
        kolor[0] = 'ciemny'
    else:
        kolor[0] = 'jasny'
        
    
    print(kolor[0])

def increase(amount=0):
    def tmp(arg):
        print(amount)
        return arg + amount
    return tmp

a = increase()
b = increase(99)
print(a(8))
print(b(253))
# jasnyciemny()
# jasnyciemny()
# jasnyciemny()
# jasnyciemny()

