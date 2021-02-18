
ffname = input("Enter file name: ")
fh = open(ffname)
count = 0
Avgval= 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count=count+1
    holder= line[20:]
    holder= holder.rstrip()
    holder= float(holder)
    Avgval= Avgval+holder
Realavg= Avgval/count
print("Average spam confidence:", Realavg)
