import re
text=open('regex_sum_938648.txt')
numlist=list()
sum=0
for line in text:
    line=line.rstrip()
    num = re.findall('([0-9.]+)',line)
    i=0
    while i < len(num):
        try:
            floater=float(num[i])
            #print(floater)
            sum=sum+floater
            i=i+1
        except:
            i=i+1
            continue
#print(sum)
