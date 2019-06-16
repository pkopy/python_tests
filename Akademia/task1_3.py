def chart():
    print('Add first number')
    a = input()
    print('Add second number')
    b = input()

    try:
        result = list((x, y) for x in range(int(a) + 1) for y in range(int(b) + 1))
    except:
         result = 'Ooooops'
    print(result)
# chart()