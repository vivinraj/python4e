import re

name =input("Enter the file:")
fh=open(name)
sum=0

for line in fh:
    numbers=re.findall('[0-9]+', line)


    length=len(numbers)



    if length > 0:
        i=0
        while i < length:
            number = int(numbers[i])
            sum = sum + number
            i = i + 1


print(sum)
