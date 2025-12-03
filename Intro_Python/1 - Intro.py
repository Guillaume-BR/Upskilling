def pair(n):
    if n%2 == 0:
        print(True)
    else:
        print(False)

pair(35)

n = 0
while 2**n != 256:
    n=n+1
print(n)

def mile_to_km(d):
    mile = d * 1.60934
    print(mile)

mile_to_km(62.137273664980675)