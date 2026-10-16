f = open("CONTACT.in")
ds = set()
for x in f:
    xau = x.lower()
    ds.add(xau)

res = list(ds)
res.sort()
for x in res:
    print(x)
f.close()
    