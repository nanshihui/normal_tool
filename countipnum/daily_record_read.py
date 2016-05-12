#!/usr/bin/python
#coding:utf-8


import time

def readfile(path,callback=None,needWrite=False,writeFilename='default.log',finallycallback=None,keywords=None):
	f = open (path)
	params=None
	filePoint=None

	if needWrite:
		filePoint=file(writeFilename,'w')
	while 1:
		line =f.readline()
		if not line :
			break;
		if callback is None:
			pass
		else:
			
			params=callback(line,filePoint,params,keywords)

	if finallycallback is not None:

		finallycallback(filePoint,params,keywords)
	if needWrite:
		filePoint.close()

	f.close()
def deal_file(line,writeplace=None,params=None,keywords=None):
	linearray = line.split()
	# if  '10/May/2016:23' in linearray[3]  :
	# if  '14.117.49.148' in linearray[0] and linearray[8]=='200' and '.' not in linearray[6]:
	# if  '04/May/2016:16' in linearray[3] and linearray[8]=='200' and 'evaluate'  in linearray[6]:
	# if  '04/May/2016:16' in linearray[3] :
	if keywords is None:
		return params

	if  keywords[0] in linearray[3] and linearray[8]==keywords[1] and keywords[2]  in linearray[6]:
		if writeplace is not None:

			writeplace.write(line)
	return params
def keyword_file(line,writeplace=None,params=None,keywords=None):
	linearray = line.split()

	if  keywords[4] in linearray[0] and linearray[8]==keywords[1] and '.' not in linearray[6] and  keywords[1][2:] in linearray[3]:
		if writeplace is not None:

			writeplace.write(line)
	return params
def countIPnumber(line,writeplace=None,dic=None,keywords=None):
	linearray = line.split()
	if dic is None:
		dic={}
	if len(linearray)>0:


		if dic.get(linearray[0],'') =='':
			dic[linearray[0]]=1
		else:
			dic[linearray[0]]=dic[linearray[0]]+1
	return dic
def write_dic(filePoint,params,keywords=None):

	for i in params.keys():
		filePoint.write(str(params[i])+'  '+str(i)+'\n')

		keywords.append(str(i))
		localtime=str(time.strftime("%Y-%m-%d-%X", time.localtime()))

		readfile(path=keywords[3],callback=keyword_file,needWrite=True,writeFilename=str(i)+'.'+localtime+'.log',keywords=keywords)
	
if __name__ == "__main__":
	keywords='evaluate'
	keyarray=['11/May/2016:00:0','200','evaluate','access.log']
	localtime=str(time.strftime("%Y-%m-%d-%X", time.localtime()))
	readfile(path=keyarray[3],callback=deal_file,needWrite=True,writeFilename=keywords+'.'+localtime+'.log',keywords=keyarray)



	readfile(path=keywords+'.'+localtime+'.log',callback=countIPnumber,needWrite=True,writeFilename='IPcount'+localtime+'.log',finallycallback=write_dic,keywords=keyarray)


