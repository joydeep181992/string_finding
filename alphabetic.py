# given string s.
#on any input it will work which has a seq in alphabet
s = 'abcdrhgirgabcvjdenjjklfeffghdweq'

#keyfunc function takes an arg which is passed in enumerate fun as tuple 
def keyfunc(t):
    i, c = t
    return ord(c) - i
a = []

for k, v in groupby(enumerate(s), key=keyfunc):
    seq = [t[1] for t in v]
    if len(seq) > 1:
        a.append(''.join(seq))
        
print(a)
