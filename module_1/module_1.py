import random
import time
import multiprocessing

n=100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000961
b=76638723687263876287368268368726378623873687326872634868374687236487623874687648634863847623846834687643
k=76382637812836812638612836812638612376182263812623861283618723681263861238612386


#1  generuje losowy element zbioru Zn
def generate_random_oneliner(k: int):
    return sum([random.randint(0, 1) * 2 ** i for i in range(k)])


def generate_random(k: int):
    result = 0
    i=0
    while i<k:
        if random.randint(0, 1) == 1:
            result += 2**i
        i+=1
    return result

#2  obliczania odwrotności w grupie Φ(n); Rozszerzony Algorytm Euklidesa
def xgcd(a: int, b: int) -> tuple:
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0


def modinv(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        raise Exception('modular inverse doesnt exisist')
    else:
        if y < 0:
            return y + a
        return y

#3  efektywnego potęgowania w zbiorze Z∗n; algorytm iterowanego podnoszenia do kwadratu
def power_binary_list(x, k, n):
    temp_list = list(reversed([int(i) for i in list('{0:0b}'.format(k))]))
    y = 1
    i = len(temp_list) - 1
    while i >= 0:
        y = ( y ** 2 ) % n
        if temp_list[i] == 1:
            y = (y * x) % n
        i = i -1
    return y

#4  sprawdza czy element zbioru Z∗p jest resztą kwadratową w Z∗p; twierdzenie Eulera
def modular_quadric_residue(a, p):
    if p < 2:
        return False
    else:
        if a == 0:
            return False
        else:
            if power_binary_list(a, int((p-1)//2), p) == 1:
                return True
            else:
                return False

#5  oblicza pierwiastek kwadratowy w ciele F∗p, gdzie
#   p ≡ 3 (mod 4) jest liczbą pierwszą; twierdzenie Eulera
def modular_sqrt(a, p):
    if p % 4 == 3:
        b = 0
        if modular_quadric_residue(a, p):
            b = power_binary_list(a, int((p + 1) / 4), p)
            return b, p - b
        else:
            print("Number " + str(a) + " is is not modular quadric residue.")
            return False
    else:
        print(str(p) + " % 4 != 3")
        return False

#6 sprawdza liczba naturalna n jest liczbą pierwszą. Wykorzystaj test Fermata
def is_prime_fermat(n, k = 100):
    if n == 1 or n == 4:
        return False
    if n == 2 or n ==3:
        return True
    else:
        for i in range(k):
            a = random.randint(2, n - 2)

            if power_binary_list(a, n - 1, n) != 1:
                return False
    return True

#lab generowanie dużej liczby pierwszej
def generate_large_prime(b=2048,k=100):
    while True:
        x = generate_random_oneliner(b)
        if is_prime_fermat(x, k):
            return x

#lab znalezienie p i q
def find_p_and_q_elgamal(b=2048, fermat=2):
    time_start = time.time()
    tmp=0
    while True:
        time2_start = time.time()
        q=generate_large_prime(b, fermat)
        p=2*q+1
        if is_prime_fermat(p, fermat):
            time_end = time.time()
            print("This took {0}".format(time_end - time_start))
            return p, q
        else:
            tmp+=1
            time2_end = time.time()
            print(str(tmp) + " prime number doesn't match. It took {0}".format(time2_end - time2_start))

