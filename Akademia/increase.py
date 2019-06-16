def increase(from_number):
    increases = []
    i = from_number
    while (i < (from_number + 3)):
        k = i
        def tmp(x):
            return (x + k)

        increases.append(tmp)
        i += 1
    print(increases)
    return increases

z1 = increase(10)

# print (z1[0])
print (z1[1](4))
print (z1[2](4))
