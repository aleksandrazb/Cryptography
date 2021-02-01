# =========================================================
# ALGEBRAIC FUNCTIONS
INT_BITS = 32


def left_rotate(n: int, d: int) -> int:
    # In n<<d, last d bits are 0.
    # To put first 3 bits of n at
    # last, do bitwise or of n<<d
    # with n >>(INT_BITS - d)
    return (n << d) | (n >> (INT_BITS - d))


# Function to right
# rotate n by d bits
def right_rotate(n: int, d: int) -> int:
    # In n>>d, first d bits are 0.
    # To put last 3 bits of at
    # first, do bitwise or of n>>d
    # with n <<(INT_BITS - d)
    return (n >> d) | (n << (INT_BITS - d)) & 0xFFFFFFFF


def left_shift(a: hex, shift: hex) -> hex:
    return a << shift


def bytes_xor(a, b) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))


# Extended Euclidean algorithm
def egcd(a: int, b: int) -> tuple:
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = egcd(b % a, a)
        return gcd, y - (b//a) * x, x


# =========================================================
# SUPPORT FUNCTIONS - CONVERTERS
def bytes_to_hex(bytes_) -> hex:
    return bytes_.hex()


def bytes_to_int(bytes_: bytes) -> int:
    return int.from_bytes(bytes_, byteorder='big', signed=True)


def hex_to_bytes(hex_) -> bytes:
    return bytes.fromhex(hex_)


def hex_to_int(str_: str) -> int:
    return int(str_, 16)


def int_to_bytes(int_) -> bytes:
    return int_.to_bytes(2, byteorder='big')


def int_to_hex(int_: int) -> hex:
    return '{:x}'.format(int_)
    # return hex(int_)


# =========================================================
# MAIN METHODS
'''
1. Zaimplementuj funkcję suma()
Dane: (xy)H,(uw)H ∈ F28
Wynik: (x′y′)H ∈ F28, gdzie (x′y′)H = (xy)H + (uw)H
'''


def add(xy: hex, uw: hex) -> hex:
    # CORRECT
    return bytes_xor(hex_to_bytes(xy), hex_to_bytes(uw)).hex()


'''
2. Zaimplementuj funkcję xtime()
Dane: (xy)H ∈ F28
Wynik: (x′y′)H ∈ F28, gdzie (x′y′)H = (xy)H · (02)H
'''


def x_time(xy: hex) -> hex:
    # PARTIALLY CORRECT - WRONG RESULTS ON LEFT_SHIFT
    return int_to_hex(left_rotate(hex_to_int(xy), 1))
    # return bytes_xor(a, hex_to_bytes('1B')).hex()

def xtime(hexstr):
    num = int(hexstr,16)
    bs1 = bin(num)[2:]
    if len(bs1)!=8:
        bs1 = '0'*(8-len(bs1))+bs1
    num = (num<<1)%2**8
    if bs1[0]=='1':
        num = num^int("1B",16)
    return hex(num)[2:]


'''
3. Zaimplementuj funkcję iloczyn()
Dane: (xy)H, (uw)H ∈ F28
Wynik: (x′y′)H ∈ F28, gdzie (x′y′)H = (xy)H · (uw)H
'''


def multiply(xy: hex, uw: hex) -> hex:
    # PENDING
    # IMPLEMENT EUCLIDE ALGORITHM FROM PREVIOUS LECTURE
    return int_to_hex(left_rotate(hex_to_int(xy), hex_to_int(uw)))


'''
4. Zaimplementuj funkcję odwrotnosc()
Dane:(xy)H ∈ F28
Wynik:(uw)H ∈ F28, gdzie (xy)H · (uw)H = (01)H

UWAGA: Implementację powyższych funkcji wykonaj na bitach!
'''


def inverse(xy: hex) -> hex:
    # PENDING
    # OPERATION DECLARED IN EXCERCISE TEXT
    return multiply('1', xy)
    pass


# =========================================================
# CONTROLLER
if __name__ == '__main__':
    # addition test
    print("addition test: ")
    print(add('57', '83'))
    # expected: d4

    # multiplication test
    print("multiplication test: ")
    # 57 * 13 = FE

    # BUT
    # 57 * 13 = 57 * (1 + 2 + 10) = 57 + AE + 7 = FE
    # and this works:
    print(add(add('57', 'ae'), '07'))
    # TODO get sum of second number - make 1+2+10 from 13 etc.

    # print(multiply('57', '13'))
    # expected: fe

    # xtime test:
    print("xtime test: ")
    #print(x_time('57'))
    print(xtime('57'))
    # expected result: 'ae'
    #print(x_time('ae'))
    print(xtime('ae'))
    # expected result: '47'
    #print(x_time('47'))
    print(xtime('47'))
    # expected result: '8e'
    #print(x_time('8e'))
    print(xtime('8e'))
    # expected result: '07'

    # inversion test
    print("inversion test: ")
    # print(inverse('57'))
    # expected: c1

    # extended euclidean test
    print("extended euclidean test: ")
    a1 = 30
    b1 = 50
    g1, x1, y1 = egcd(a1, b1)
    print("gcd(%s, %s) = %s, x= %s, y = %s" % (a1, b1, g1, x1, y1))
    # gcd(30, 50) = 10
    # Here, x = 2
    # y = -1 as 30 * 2 + 50 * -1 = 10
