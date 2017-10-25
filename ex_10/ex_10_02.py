name = input("Enter file:")

handle = open(name)
line=list()
count=dict()


for line in handle :
    line=line.split()

    if len(line)>1 :



            if line[0] != 'From' :
                continue
            else:

                word=line[5]

                pos=word.find(':')
                word=word[0:2]

                count[word]=count.get(word,0) + 1

lst=list()
for key,value in count.items() :
    tup= (key, value)
    lst.append(tup)

lst=sorted(lst)


for key,value in lst :
    print(key, value)
