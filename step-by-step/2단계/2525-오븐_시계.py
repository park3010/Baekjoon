h, m = map(int, input().split())
n = int(input())

m += n
while m >= 60:
    m -= 60
    h += 1
    if h == 24: h = 0
        
print(h)
print(m)
