file1 = open ('1.txt')
temp=set()
while 1:
	line =file1.readline()
	if not line:
		break;
	print line
	temp.add(line)
file1.close()
file2 = open ('2.txt')
while 1:
	line =file2.readline()
	if not line:
		break;
	print line
	temp.add(line)
file2.close()
f = file('3.txt','w') 
for word in temp:
	
	f.write(word)
f.close()