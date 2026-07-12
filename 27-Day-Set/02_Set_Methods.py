s = {34,23,2,5,34,23,5,6,7,8}

print(s)

s.add (9)
print(s)

s.remove(5)
print(s)

# s.remove(454568)  #this will give error because 454568 is not present in the set
s.discard(454568)
print(s)


s.pop()
print(s)