'''
V 1.0

n = 2
primos = [2]
while True:
    l2 = [n % x for x in primos]
    if l2.count(0) == 0:
        primos.append(n)
        print(primos[-1])
        n += 1
    else:
        n += 1
'''

# V 2.0
with open('primos.txt', 'r') as f:
    n = int(f.readlines()[-1])
print(n)
input()
while True:
    with open('primos.txt', 'r') as f:
        l2 = (f.readlines())
    l2 = [int(x) for x in l2]
    l2 = [n % x for x in l2]
    if l2.count(0) == 0:
        with open('primos.txt', 'a') as f:
            f.writelines(str(n) + '\n')
        n +=1
    else:
        n +=1
