s1 = input().lower()
s2 = input().lower()
xau1 = set(s1.split())
xau2 = set(s2.split())
union = xau1 | xau2
giao = xau1 & xau2
union1 = sorted(list(union))
giao1 = sorted(list(giao))

union_res = " ".join(union1)
giao_res = " ".join(giao1)

print(union_res)
print(giao_res)
