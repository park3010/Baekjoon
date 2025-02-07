a,b,c = map(int, input().split())
dice = sorted([a,b,c], reverse=True)

if a==b==c:
    money = 10000 + (a * 1000)
    print(money)
elif (dice[0]==dice[1]) or (dice[1]==dice[2]):
    money = 1000 + (dice[1] * 100)
    print(money)
else: print(max(dice)*100)
