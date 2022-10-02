def fibonanci(n):
    if n==1 or n==2:
        return 1
    return fibonanci(n-1) + fibonanci(n-2)

x = int(input())

if x<1:
    print("So ", x, " khong nam trong khoang [1,30].")
elif x>30:
    print("So ", x, " khong nam trong khoang [1,30].")
else:
    print(fibonanci(x))
