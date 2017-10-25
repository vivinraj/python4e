fname = input("Enter file name: ")
fh = open(fname)
lst = list()
words = list()
c = 0

for line in fh:
	if c==0 :
		words=line.split()
		print(words)
	else:
		print("in else")
		lst=line.split()

		for w in lst:
			match=0
			for j in words:
				print(w)
				print(j)
				if w == j :
					print("J is equal to W")
					match=1
				else: continue
			if match==0:
				print("appending")
				words.append(w)


	c=c + 1
	print(c)
	print(words)


words.sort()

print(words)
