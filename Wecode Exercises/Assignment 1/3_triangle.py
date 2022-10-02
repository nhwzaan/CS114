import math
from decimal import Decimal, getcontext

a = float(input())
b = float(input())
c = float(input())

def area(a, b, c):
    s = (a + b +c)/2
    result = (math.sqrt(s * (s - a) * (s - b) * (s - c)))

    return result

def isTriangle(a, b, c):
    check = 0
    if a+b>c and a+c>b and b+c>a:
        check = 1
    else:
        check = 0
    return check


def typeOfTriangle(a, b, c):
    typeTriangle = ''
    if a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
        typeTriangle = 'vuong'
    elif a==b and b==c:
        typeTriangle = 'deu'
    elif a==b or a==c or b==c:
        typeTriangle = 'can'
    else:
        typeTriangle = 'thuong'
    return typeTriangle

if isTriangle(a,b,c)==0:
    print("Khong phai tam giac")
else:
    print('Tam giac ' + typeOfTriangle(a,b,c) + ', dien tich = ', end='')
    DT = round(area(a, b, c), 2)
    print(DT) if DT % 1 != 0 else print(int(DT))