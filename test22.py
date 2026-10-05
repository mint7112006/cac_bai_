xau = list(input().split(','))
hauto = xau[0]
for w in xau[1:]:
    while not w.endswith(hauto):
        hauto = hauto[1:]
        if hauto == "":break
print(hauto)