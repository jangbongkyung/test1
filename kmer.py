import sys

def mer(b1,b2,n):
    if n==1:
        return b2
    ltmp=[]
    for i in b1:
        for j in b2:
            ltmp.append(i+j)
    return mer(b1,ltmp,n-1)

b1 =['A','T','G','C']
b2 ={'A','T','G','C'}
n=int(sys.argv[1])
print(mer(b1,b2,n))
