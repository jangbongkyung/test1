import sys
l=[]
def fibo(n:int)->int:
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

n=int(sys.argv[1])

print(fibo(n))

    

# return 에 자기 자신으 함수를 넣야할 경우 재귀     
