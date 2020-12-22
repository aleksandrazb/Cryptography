import math
import random

def modinv(n,p):
    u = extended_euklides(n,p)[0]
    v = extended_euklides(n,p)[1]
    if ((u * n % p) == 1):
        if (u < 0):
            return u + p
        return u
    else:
        if v < 0:
            return v + p
        return v


def extended_euklides(a, b):
    if b == 0:
        return 1, 0
    else:
        q, r = divmod(a,b)
        s, t = extended_euklides(b, r)
        return t, s - q * t



def elliptic_curve(x:int,A:int,B:int,p:int):
    return ((x**3)%p+(A*x)%p+B%p)%p

def delta_of_elliptic_curve(A:int,B:int,p:int):
    return (4*(A**3)+27*(B**2))%p


#czy rownanie jest krzywa eliptyczna
def is_elliptic_curve(A:int,B:int,p:int,adnotations=False):
    summary=delta_of_elliptic_curve(A,B,p)
    if(adnotations):
        print("[4 * (" + str(A) + "^3) + 27 * (" + str(B) + "^2)] mod " + str(p) + " = " + str(summary))
    if(summary==0):
        return False
    else:
        return True



#1 generowanie losowej krzywej eliptycznej
def random_elliptic_curve(p:int,adnotations=False):
    if(p%4 != 3%4):
        if(adnotations):
            print("!!! " + str(p) + " (mod 4) != 3 (mod 4)")
        return -1
    else:
        if(adnotations):
            print("OK " + str(p) + " (mod 4) == 3 (mod 4)\n")
        while(True):
            A=random.randint(0,p-1)
            B=random.randint(0,p-1)
            if(adnotations):
                summary=is_elliptic_curve(A,B,p,adnotations)
                print("A = " + str(A) + "\nB = " + str(B) + "\n" + str(summary) + "\n")
            if(is_elliptic_curve(A,B,p)):
                if(adnotations):
                    print("Random elliptic curve\ny^2 = x^3 + " + str(A) + "*x + "+ str(B) + "\n")
                return A,B,p
                break

#2 znajdz losowy punkt na krzywej eliptycznej
def find_point_on_elliptic_curve(A:int,B:int,p:int,adnotations=False):
    while(True):
        i=random.randint(0,p-1)
        fx=elliptic_curve(i,A,B,p)
        if(adnotations):
            print("y^2 = [(" + str(i) + "^3) + " + str(A) + " * " + str(i) + " + " + str(B) + "] mod " + str(p) + " = " + str(fx) + "\n")
            print("P(" + str(i) + "," + str(math.sqrt(fx)) + ")")
        _is=is_this_point_on_elliptic_curve(i,math.sqrt(fx),A,B,p,adnotations)
        if(_is==True):
            if(adnotations):
                print("This point is on elliptic curve")
            return i,math.sqrt(fx)
        elif(adnotations):
            print("This point isn't on elliptic curve")
        
    

#3 czy punkt nalezy do krzywej eliptycznej
def is_this_point_on_elliptic_curve(x:int,y:int,A:int,B:int,p:int,adnotations=False):
    if(adnotations):
        print("P(" + str(x) + "," + str(y) + ")\n")
    fx=elliptic_curve(x,A,B,p)
    if(adnotations):
        print("y^2 = [(" + str(x) + "^3) + " + str(A) + " * " + str(x) + " + " + str(B) + "] mod " + str(p) + " = " + str(fx) + "\n")
    if(fx-y**2==0):
        return True
    else:
        return False

#4 punkt przeciwny
def opposite_point(x:int,y:int,A:int,B:int,p:int,adnotations=False):
    if(adnotations):
        print("P = (" + str(x) + ", " + str(y) + ")")
        print("-P = (" + str(x) + ", " + str(-y) + ")\n")
        is_this_point_on_elliptic_curve(x,-y,A,B,p,adnotations)
    if(is_this_point_on_elliptic_curve(x,-y,A,B,p)):
        return x,-y
    else:
        return -1

#5 dodawanie punktow na krzywej eliptycznej
def add_points_on_elliptic_curve(x1:int,y1:int,x2:int,y2:int,A:int,B:int,p:int,adnotations=False):
    
    if(is_this_point_on_elliptic_curve(x1,y1,A,B,p,False)):
        if(adnotations):
            print("P = (" + str(x1) + ", " + str(y1) + ") is on elliptic curve")
    else:
        print("!!! P = (" + str(x1) + ", " + str(y1) + ") isn't on elliptic curve")
        
    if(is_this_point_on_elliptic_curve(x2,y2,A,B,p,False)):
        if(adnotations):
            print("Q = (" + str(x2) + ", " + str(y2) + ") is on elliptic curve")
    else:
        print("!!! Q = (" + str(x2) + ", " + str(y2) + ") isn't on elliptic curve")

    if(x1!=x2 and y1!=y2):
        _lambda=((y2-y1)*modinv((x2-x1),p))%p
        if(adnotations):
            print("lambda = [(" + str(y2) + " - " + str(y1) + ") * (" + str(x2) + " - " + str(x1) + ")^(-1)  )] mod " + str(p) + " = " + str(_lambda))
        x=((_lambda**2)-x1-x2)%p
        if(adnotations):
            print("x = [ " + str(_lambda) + "^2 - " + str(x1) + " - " + str(x2) + " ] mod " + str(p) + " = " + str(x))
        y=(_lambda*(x1-x)-y1)%p
        if(adnotations):
            print("y = [ " + str(_lambda) + " * (" + str(x1) + " - " + str(x) + ") - " + str(y1) + " ] mod " + str(p) + " = " + str(y))
            print("R = (" + str(x) + ", " + str(y) + ")")
        return x,y

    if(x1==x2 and y1==y2):
        _lambda=((3*(x1**2)+A)*modinv((2*y1),p))%p
        if(adnotations):
            print("lambda = [(3 * " + str(x1) + "^2 + " + str(A) + ") * (2 * " + str(y1)+ ")^(-1))] mod " + str(p) + " = " + str(_lambda))
        x=((_lambda**2)-2*x1)%p
        if(adnotations):
            print("x = [ " + str(_lambda) + "^2 - 2 * " + str(x1)  + " ] mod " + str(p) + " = " + str(x))
        y=(_lambda*(x1-x)-y1)%p
        if(adnotations):
            print("y = [ " + str(_lambda) + " * (" + str(x1) + " - " + str(x) + ") - " + str(y1) + " ] mod " + str(p) + " = " + str(y))
            print("R = (" + str(x) + ", " + str(y) + ")")
        return x,y

    if(x1==0 and y1==0):
        if(adnotations):
            print("R = (" + str(x2) + ", " + str(y2) + ")")
        return x2,y2
    else:
        if(x2==0 and y2==0):
            if(adnotations):
                print("R = (" + str(x1) + ", " + str(y1) + ")")
            return x1,y1
