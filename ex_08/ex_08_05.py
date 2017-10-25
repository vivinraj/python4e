fname = input("Enter file name: ")


fh = open(fname)
count = 0
words=list()

for line in fh:
    words=line.split()

    if len(words)>1 :


		if words[0] != 'From' :
			continue
		else:
			word=words[1]
			print(word)
			count=count+1

print("There were", count, "lines in the file with From as the first word")
