def demo_routine(num):
    print('I am a demo function')
    if num % 2 == 0:
        return True
    else:
        return False

num = int(input('Enter a number\n'))
if demo_routine(num):
    print(num, 'is an even number')
else:
    print(num, 'is an odd number')

