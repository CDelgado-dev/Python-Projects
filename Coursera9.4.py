fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
emails=dict()
for line in fh:
    line=line.rstrip()
    if line.startswith("From: "):
        line=line.split()
        for word in line:
            emails[word]=emails.get(word,0)+1
    else:
        continue
emails["From:"] = 0
bigcount=None
bigword=None
for words,count in emails.items():
     if bigcount is None or count > bigcount:
      bigword = words
      bigcount=count

print(bigword, bigcount)
