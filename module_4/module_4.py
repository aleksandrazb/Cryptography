bits=8
'''
1. Zaimplementuj funkcję suma()
Dane: (xy)H,(uw)H ∈ F28
Wynik: (x′y′)H ∈ F28, gdzie (x′y′)H = (xy)H + (uw)H
'''

def suma(l1: hex, l2: hex) -> hex:
    l1bin = bin(int(l1, 16))[2:].zfill(bits)
    l2bin = bin(int(l2, 16))[2:].zfill(bits)
    w = []
    for a, b in zip(l1bin, l2bin):
        w.append(int(a) ^ int(b))
    return hex(int(''.join([str(i) for i in w]), 2))[2:]


'''
2. Zaimplementuj funkcję xtime()
Dane: (xy)H ∈ F28
Wynik: (x′y′)H ∈ F28, gdzie (x′y′)H = (xy)H · (02)H
'''

def xtime(l: hex) -> hex:
    lb = bin(int(l, 16))[2:].zfill(bits)
    if lb[0] == '1':
        lb = lb[1:]
        w = hex(int(lb, 2) << 1 ^ int('1B', 16))[2:]
    else:
        w = hex(int(lb, 2) << 1)[2:]
    return w


'''
3. Zaimplementuj funkcję iloczyn()
Dane: (xy)H, (uw)H ∈ F28
Wynik: (x′y′)H ∈ F28, gdzie (x′y′)H = (xy)H · (uw)H
'''

def iloczyn(l1: hex, l2: hex) -> hex:
    l1bin = bin(int(l1, 16))[2:].zfill(bits)
    l = len(l1bin) - 1
    w = '00'
    for i in l1bin:
        if i == '1':
            p = l
            tmp = l2
            while p != 0:
                tmp = xtime(tmp)
                p -= 1
            w = suma(tmp, w)
        l -= 1
    return w


'''
4. Zaimplementuj funkcję odwrotnosc()
Dane:(xy)H ∈ F28
Wynik:(uw)H ∈ F28, gdzie (xy)H · (uw)H = (01)H

UWAGA: Implementację powyższych funkcji wykonaj na bitach!
'''

def odwrotnosc(l: hex) -> hex:
    for i in range(255):
        if iloczyn(l, hex(i)[2:]) == '1':
            return hex(i)[2:]

#def odwrotnosc(a: hex) -> hex:
#    b=a
#    for i in range(13,0,-1):
#        if i and 1:
#            tmp=b
#        else:
#            tmp=a
#        b=iloczyn(b,tmp)
#    return b



if __name__ == '__main__':
    #print("test suma: ")
    #print(suma('57', '83'))
    # expected: d4

    #print("test xtime: ")
    #print(xtime('57'))
    # expected result: 'ae'
    #print(xtime('ae'))
    #print(x_time('47'))
    #print(xtime('47'))
    #print(x_time('8e'))
    #print(xtime('8e'))
    # expected result: '07'

    #print("test iloczyn: ")
    #print(iloczyn('57', '83'))
    # 57 * 13 = FE

    #print("test odwrotnosc: ")
    xx='00'
    print(odwrotnosc(xx))
    #print(iloczyn(xx,odwrotnosc(xx)))

    print(iloczyn('42', '62'))
    print(iloczyn('02', '03'))
    print(suma('a2','a2'))