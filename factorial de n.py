def Fact(n):
    if n==0:
        return 1
    else:
        r=n*Fact(n-1)
    return r
        