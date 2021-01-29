
'''
1. Zaimplementuj funkcję suma()
Dane: (xy)H,(uw)H ∈ F28
Wynik: (x′y′)H ∈ F28, gdzie (x′y′)H = (xy)H + (uw)H

2. Zaimplementuj funkcję xtime()
Dane: (xy)H ∈ F28
Wynik: (x′y′)H ∈ F28, gdzie (x′y′)H = (xy)H · (02)H

3. Zaimplementuj funkcję iloczyn()
Dane: (xy)H, (uw)H ∈ F28
Wynik: (x′y′)H ∈ F28, gdzie (x′y′)H = (xy)H · (uw)H

4. Zaimplementuj funkcję odwrotnosc()
Dane:(xy)H ∈ F28
Wynik:(uw)H ∈ F28, gdzie (xy)H · (uw)H = (01)H

UWAGA: Implementację powyższych funkcji wykonaj na bitach!
'''


INT_BITS = 32


def left_rotate(n: int, d: int) -> int:
    # In n<<d, last d bits are 0.
    # To put first 3 bits of n at
    # last, do bitwise or of n<<d
    # with n >>(INT_BITS - d)
    return (n << d) | (n >> (INT_BITS - d))


# Function to right
# rotate n by d bits
def right_rotate(n, d) -> int:
    # In n>>d, first d bits are 0.
    # To put last 3 bits of at
    # first, do bitwise or of n>>d
    # with n <<(INT_BITS - d)
    return (n >> d) | (n << (INT_BITS - d)) & 0xFFFFFFFF


def left_shift(a: hex, shift: hex) -> hex:
    return a << shift


def hex_to_bytes(hex_) -> bytes:
    return bytes.fromhex(hex_)


def bytes_to_hex(bytes_) -> hex:
    return bytes_.hex()


def int_to_bytes(int_) -> bytes:
    return int_.to_bytes(2, byteorder='big')


def bytes_to_int(bytes_: bytes) -> int:
    return int.from_bytes(bytes_, byteorder='big', signed=True)


def bytes_xor(a, b) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))


def hex_to_int(str_: str) -> int:
    return int(str_, 16)


def int_to_hex(int_: int) -> hex:
    return '{:x}'.format(int_)
    # return hex(int_)


# =========================================================
def add(xy: hex, uw: hex) -> hex:
    # CORRECT
    return bytes_xor(hex_to_bytes(xy), hex_to_bytes(uw)).hex()


def x_time(xy: hex) -> hex:
    # PARTIALLY CORRECT - WRONG RESULTS ON LEFT_SHIFT
    return int_to_hex(left_rotate(hex_to_int(xy), 1))
    # return bytes_xor(a, hex_to_bytes('1B')).hex()


def multiply(xy: hex, uw: hex) -> hex:
    # PENDING
    # IMPLEMENT EUCLIDE ALGORITHM FROM PREVIOUS LECTURE
    return int_to_hex(left_rotate(hex_to_int(xy), hex_to_int(uw)))


def inverse(xy: hex) -> hex:
    # PENDING
    # OPERATION DECLARED IN EXCERCISE TEXT
    return multiply('1', xy)
    pass


# =========================================================
if __name__ == '__main__':
    # addition test
    print("addition test: ")
    print(add('57', '83'))
    # expected: d4

    # multiplication test
    print("multiplication test: ")
    # print(multiply('57', '83'))
    # expected: c1

    # xtime test:
    print("xtime test: ")
    print(x_time('57'))
    # expected result: 'ae'
    print(x_time('ae'))
    # expected result: '47'
    print(x_time('47'))
    # expected result: '8e'
    print(x_time('8e'))
    # expected result: '07'

    # inversion test
    print("inversion test: ")
    # print(inverse('57'))
    # expected: c1
