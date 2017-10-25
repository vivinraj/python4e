


name = input("Enter file:")

fh = open(name)
email=dict()
for line in fh:
	words=line.split()

	if len(words)>1 :


		if words[0] != 'From' :
			continue
		else:
			word=words[1]
			email[word]=email.get(word,0) + 1




bigcount=None
bigword=None
for word,count in email.items() :
	if bigcount is None or count > bigcount :
		bigword=word
		bigcount=count

print(bigword, bigcount)
