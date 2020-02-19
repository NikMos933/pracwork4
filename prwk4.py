def probe(a):
    try:
        int(a)
    except ValueError:
        return False
    return True


N = input()
if probe(N) is True:
    N = int(N)
else:
    print('невенрый ввод данных')
    exit(0)
m = input()
if probe(m) is True:
    m = int(m)
else:
    print('невенрый ввод данных')
    exit(0)
k = input()
if probe(k) is True:
    k = int(k)
else:
    print('невенрый ввод данных')
    exit(0)
ans = ''
while probe(m) is True and probe(N) is True and probe(k) is True and (0<k<=N):
    ans = ''
    if k > 1:
        ans = '<< '
    for i in range(k-m, k+m+1):
        if 0 < i <= N:
            if i != k:
                ans = ans+str(i)+' '
            else:
                ans = ans+'('+str(i)+')'+' '
    if k < N:
        ans = ans+' >>'
    print(ans)
    d = input()
    if d == '>>':
        k = N
    if d == '<<':
        k = 1
    if (d is '<') and k != 1:
        k = k-1
    if d is'>' and k != N:
        k = k+1