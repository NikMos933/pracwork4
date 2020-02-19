def check(a):
    try:
        int(a)
    except ValueError:
        return False
    return True


def pagecheck(s):
    l = len(s)
    integ = []
    i = 0
    r1 = 0
    r2 = 0
    i1 = 0
    while i < len(s):
        s_int = ''
        a = s[i]
        while '0' <= a <= '9':
            s_int += a
            i += 1
            if i < l:
                a = s[i]
            else:
                break
        i += 1
        if s_int != '':
            integ.append(int(s_int))
    for i in s:
        if '<' is s[i1]:
           r1 = r1 + 1
        if '>' is s[i1]:
           r2 = r2 + 1
        i1 = i1 + 1
    if len(integ) == 1 and r1 == 1 and r2 == 1:
        s1 = integ[0]
        s1 = str(s1)
        if s.index('<') < s.index(s1) < s.index('>'):
            s = s.replace('<','')
            s = s.replace('>', '')
            try:
                int(s)
            except ValueError:
                return False
            return True
        else:
            return False
    else:
        return False


def main():
    N = input()
    if check(N) is True:
        N = int(N)
    else:
        print('невенрый ввод данных')
        exit(0)
    m = input()
    if check(m) is True:
        m = int(m)
    else:
        print('невенрый ввод данных')
        exit(0)
    k = input()
    if check(k) is True:
        k = int(k)
    else:
        print('невенрый ввод данных')
        exit(0)
    ans = ''
    while check(m) is True and check(N) is True and check(k) is True and (0 < k <= N):
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
        if pagecheck(d) is True:
            l = len(d)
            integ = []
            i = 0
            while i < len(d):
                s_int = ''
                a = d[i]
                while '0' <= a <= '9':
                    s_int += a
                    i += 1
                    if i < l:
                        a = d[i]
                    else:
                        break
                i += 1
                if s_int != '':
                    integ.append(int(s_int))
            k = integ[0]
        else:
            if d == '>>':
                k = N
            if d == '<<':
                k = 1
            if (d is '<') and k != 1:
                k = k-1
            if d is'>' and k != N:
                k = k+1