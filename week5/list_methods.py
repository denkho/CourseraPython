l = [1, 2, 3, 4, 5, 4]
print(l)

print(l.count(4))
print(l.index(4))
print(l.index(4, 5))

l.append(7)
l.append(8)
print(l)

lm = [12, 13, 14, 15, 5]
l.extend(lm)
print(l)

l.remove(5)
print(l)

l.insert(5, 105)
print(l)

l.reverse()
print(l)

l.pop()
print(l)

l.pop(2)
print(l)
