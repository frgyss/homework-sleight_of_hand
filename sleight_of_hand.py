#!\usr\bin\env python 3
# -*- coding: utf-8 -*-


def sleight_of_hand(k, a, b, c, d):
    print(k)
    print(a)
    print(b)
    print(c)
    print(d)
    t = 10
    vin = 0
    sp = a + b + c + d
#    sp = sp.replace('.', '')
    for i in range(t):                      # цикл по времени t
        km = sp.count(str(i))
        if 0 < km <= (k*2):
            vin += 1

    return(vin)

print(sleight_of_hand(3, "8888", "8888", "1155", "5555"))
