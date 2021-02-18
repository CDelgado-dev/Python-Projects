fname = input("Enter file name: ")
fh = open(fname)
lst = list()
fresh = list()
i = 0
for line in fh:
        x=line.split()
        lst=lst+x
while i < len(lst):
 if lst[i] not in fresh:
    fresh.append(lst[i])
    i=i+1
 else:
     i=i+1
     continue
fresh.sort()
print(fresh)
