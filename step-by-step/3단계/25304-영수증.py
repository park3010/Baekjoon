TotalPay = int(input())
num = int(input())
pay = 0

for _ in range(num):
    goods,n = map(int, input().split())
    pay += (goods * n)
    
if pay==TotalPay:
    print('Yes')
else: print('No')
