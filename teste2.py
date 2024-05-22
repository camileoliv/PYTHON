n = [22,44,-33,21,-12,11,23,37,-36,-46,45,-41]
p = []
ne= []

for i in n :
    if (i >= 0):
        p.append(i)
    else:
        ne.append(i)

print(p)
print(ne)