n=0
with open("070.vcf",'r')as handle:
    for line in handle:
        if line.startswith("#"):
            continue
        else:
            n+=1    
print(n)        
