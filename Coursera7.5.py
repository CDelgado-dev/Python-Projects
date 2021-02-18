

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
emails=dict()
for line in fh:
    line=line.rstrip()
    if line.startswith("From: "):
        count = count+1
        line=line.split()
        print(line[1])
    else:
        continue

#words = line.split()
print("There were", count, "lines in the file with From as the first word")
