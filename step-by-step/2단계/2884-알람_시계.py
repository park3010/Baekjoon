h,m = map(int, input().split())

if m>=45:
    m-=45
    print(h)
    print(m)
else:
    if h==0:
        h = 23
    else: h-=1
    m = (m+60)-45
    if m==60:
        h+=1
        m=0
    print(h)
    print(m)
