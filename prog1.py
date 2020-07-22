
def combination(elements,length): 
    for i in elements: 
        if length==1: 
            return elements[i] 
    
    
if __name__=="__main__": 
    elements=input("나열할 요소들을 입력하시오 : ") 
    length=int(input("요소들 중 몇 개를 뽑을 것인지 입력하시오 : ")) 
    result=list(combination(elements, length)) 
    print("%s 중 %d개를 선택하는 조합의 경우는 다음과 같이 %d 가지 있습니다." % (elements, length, len(result)))
    print() 
    for i in range(len(result)): 
        print("%d. %s" % (i+1, result[i])) 
    print()


