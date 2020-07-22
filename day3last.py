import pandas as pd
from matplotlib import pyplot as plt
d={"SNP":0,"Ins":0,"Del":0}

with open("070.vcf",'r') as handle:
    for line in handle:
        if line.startswith("#"):
            continue
        
        splitted=line.strip().split("\t")
        chrom = splitted[0]
        pos = splitted[1]
        id_ = splitted[2]
        ref = splitted[3]
        alts = splitted[4].split(",")
        for alt in alts:
            if len(ref)==len(alt):
                d["SNP"] +=1
            elif len(ref)<len(alt):
                d["Ins"] +=1
            elif len(ref)>len(alt):
                d["Del"] +=1
            else:
                raise "something wrong"

print(d)
df=pd.DataFrame([d])
print(df)
df.plot.bar()
plt.savefig("v.png")
