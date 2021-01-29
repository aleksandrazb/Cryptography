
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


def left_rotate(n, d) -> int:
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


def hex_to_int(str_: str) -> hex:
    return int(str_, 16)


# =========================================================
def add(xy: str, uw: str) -> hex:
    return bytes_xor(hex_to_bytes(xy), hex_to_bytes(uw)).hex()


def x_time(xy: hex) -> hex:
    a = int_to_bytes(left_shift(hex(xy), 1))
    return bytes_xor(a, hex_to_bytes('1B')).hex()


def multiply(xy: str, uw: str) -> hex:
    print(hex_to_int(xy), hex_to_int(uw))
    a = left_rotate(hex_to_int(xy), hex_to_int(uw))
    print(a)
    a = int_to_bytes(a)
    return bytes_to_hex(a)


def inverse(xy, uw):
    pass


# =========================================================
if __name__ == '__main__':
    # addition test
    print(add('57', '83'))
    # expected: d4

    # xtime test:
    print(x_time('57'))
    # expected result: 'ae'
