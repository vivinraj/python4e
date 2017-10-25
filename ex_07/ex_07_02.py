# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total=0
count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    print(line)
    pos=line.find(":")
    print(pos)
    length=len(line)
    print(length)
    val=line[pos+2:length]
    print(val)
    val=val.strip()
    print(val)
    val=float(val)
    total=total + val
    count=count+1
avg= total/count
print("Average spam confidence:", avg)
