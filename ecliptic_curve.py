import math

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
def is_elliptic_curve(A:int,B:int,p:int):
    summary=delta_of_elliptic_curve(A,B,p)
    print("[4 * (" + str(A) + "^3) + 27 * (" + str(B) + "^2)] mod " + str(p) + " = " + str(summary))
    if(summary==0):
        return False
    else:
        return True


#czy punkt nalezy do krzywej eliptycznej
def is_this_point_on_elliptic_curve(x:int,y:int,A:int,B:int,p:int,adnotations=True):
    if(adnotations):
        print("P(" + str(x) + "," + str(y) + ")\n")
    y=y%p
    if(adnotations):
        print("P mod " + str(p) + " = P(" + str(x) + "," + str(y) + ")\n")
    fx=elliptic_curve(x,A,B,p)
    if(adnotations):
        print("y^2 = [(" + str(x) + "^3) + " + str(A) + " * " + str(x) + " + " + str(B) + "] mod " + str(p) + " = " + str(fx) + "\n")
    if((y**2)%p==fx):
        return True
    else:
        return False

#dodawanie punktow na krzywej eliptycznej
def add_points_on_elliptic_curve(x1:int,y1:int,x2:int,y2:int,A:int,B:int,p:int,adnotations=True):
    
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
