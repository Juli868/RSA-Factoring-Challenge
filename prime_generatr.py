#!/usr/bin/python3
def generator(number=0):
    found = []
    for a in range (1, number):
        d = (a** number) - a
        found.append(d)
    for a in range(len(found)):
        temp = found[a] % number
        if temp != 0:
            return (-1)
    return (1)
prime_number= []
a = 1
counter = 0
while (True):
    a += 1
    generate = generator(a)
    if generate == 1:
        prime_number.append(a)
        counter += 1
    else:
        continue
    if (counter > 100):
        break
print(prime_number)
