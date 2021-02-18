
ffname = input("Enter file name: ")
fh = open(ffname)
for lines in fh:
    lines=lines.upper()
    lines=lines.rstrip()
    print(lines)
