'''
1. Zaimplementuj funkcję suma()
Dane: (xy)H,(uw)H ∈ F28
Wynik: (x′y′)H ∈ F28, gdzie (x′y′)H = (xy)H + (uw)H
'''

def suma(liczba1: hex, liczba2: hex) -> hex:
    liczba1b = bin(int(liczba1, 16))[2:].zfill(8)
    liczba2b = bin(int(liczba2, 16))[2:].zfill(8)
    wynik = []
    for a, b in zip(liczba1b, liczba2b):
        wynik.append(int(a) ^ int(b))
    return hex(int(''.join([str(i) for i in wynik]), 2))[2:]


'''
2. Zaimplementuj funkcję xtime()
Dane: (xy)H ∈ F28
Wynik: (x′y′)H ∈ F28, gdzie (x′y′)H = (xy)H · (02)H
'''

def xtime(liczba: hex) -> hex:
    liczbab = bin(int(liczba, 16))[2:].zfill(8)
    if liczbab[0] == '1':
        liczbab = liczbab[1:]
        wynik = hex(int(liczbab, 2) << 1 ^ int('1B', 16))[2:]
    else:
        wynik = hex(int(liczbab, 2) << 1)[2:]
    return wynik


'''
3. Zaimplementuj funkcję iloczyn()
Dane: (xy)H, (uw)H ∈ F28
Wynik: (x′y′)H ∈ F28, gdzie (x′y′)H = (xy)H · (uw)H
'''

def iloczyn(liczba1: hex, liczba2: hex) -> hex:
    wynik = '00'
    liczba1b = bin(int(liczba1, 16))[2:].zfill(8)
    length = len(liczba1b) - 1

    for i in liczba1b:
        if i == '1':
            temp = liczba2
            counter = length
            while counter != 0:
                temp = xtime(temp)
                counter -= 1
            wynik = suma(temp, wynik)
        length -= 1
    return wynik


'''
4. Zaimplementuj funkcję odwrotnosc()
Dane:(xy)H ∈ F28
Wynik:(uw)H ∈ F28, gdzie (xy)H · (uw)H = (01)H

UWAGA: Implementację powyższych funkcji wykonaj na bitach!
'''

def odwrotnosc(liczba: hex) -> hex:
    for i in range(255):
        if iloczyn(liczba, hex(i)[2:]) == '1':
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
    print("test suma: ")
    print(suma('57', '83'))
    # expected: d4

    print("test xtime: ")
    print(xtime('57'))
    # expected result: 'ae'
    print(xtime('ae'))
    #print(x_time('47'))
    print(xtime('47'))
    #print(x_time('8e'))
    print(xtime('8e'))
    # expected result: '07'

    print("test iloczyn: ")
    print(iloczyn('57', '13'))
    # 57 * 13 = FE

    print("test odwrotnosc: ")
    xx='53'
    print(odwrotnosc(xx))
    print(iloczyn(xx,odwrotnosc(xx)))
    # expected: c1

