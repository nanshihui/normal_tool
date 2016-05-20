file1 = open ('1.txt')
temp=set()
while 1:
	line =file1.readline()
	if not line:
		break;
	array= line.split()
	temp.add(array[5])
file1.close()

f = file('3.txt','w') 
for word in temp:
	
	f.write(word+'\n')
f.close()