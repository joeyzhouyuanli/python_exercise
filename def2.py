import math    

def quadratic(A,B,C = 0):
    a = float(A)
    b = float(B)
    c = float(C)
    if a == 0:
        print('a<>0')
    else:
        s = b*b-4*a*c
        M = float(s)
        if M < 0:
            print('no root')
        else:
            k = math.sqrt(M)
            nx = (- b + k)/(2*a)
            ny = (- b - k)/(2*a)
            return nx, ny

a = input('a:')
b = input('b:')
c = input('c:')
s = quadratic(a,b,c)
print(s)