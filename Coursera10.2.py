fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
carry=list()
lst=dict()
times=list()
for line in fh:
    line=line.rstrip()
    if line.startswith("From "):
        line=line.split()
        time=line[5]
        time=time.split(':')
        time=time[0]
        carry.append(time)
    else:
            continue
for counts in carry:
    lst[counts]=lst.get(counts,0)+1
for time,amount in lst.items():
    tup = (time, amount)
    times.append(tup)
times = sorted(times)
for val,key in times:
    print(val, key)
