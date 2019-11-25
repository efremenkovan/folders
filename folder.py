#!/usr/bin/env python3
from termcolor import colored
import os
import sys 
import re
DEPTH_LEVEL = sys.maxsize

def checkExistance(string,array):
	for item in array:
		if re.match(string,item) != None:
			return False
	return True

def main(enter,loop, preset,toIgnore):
	if loop <= DEPTH_LEVEL+1:
		folder = enter
		setter = '├── ' if loop > 1 else '├── '
		closeSetter = '└── ' if loop > 1 else '└── '
		extender = ''
		for (dirpath,dirnames,filenames) in os.walk(folder):
			if len(filenames) > 0:
				for fileCounter,file in enumerate(filenames,start=1):
					if fileCounter < len(filenames):
						print(preset+setter+file)
					elif len(dirnames) > 0:
						print(preset+setter+file)
					else:
						print(preset+closeSetter+file)
			for counter,dirname in enumerate(dirnames,start=1):
				if checkExistance(dirname,toIgnore):
					if(len(dirnames)>1 and counter < len(dirnames)):
						extender = '| '
						print(preset+setter[:-1],colored(dirname,'yellow'))
					else:
						extender = '  '
						print(preset+closeSetter[:-1],colored(dirname,'yellow'))
					main(dirpath +'/'+ dirname,loop+1,preset+extender+'  ',toIgnore)
			return
	else:
		return



if __name__ == '__main__':
	IGNORED_FOLDER = []
	for index,arg in enumerate(sys.argv):
		if arg == '--ignore':
			IGNORED_FOLDER.append(str(sys.argv[index+1]))
		elif arg=="--depth":
			DEPTH_LEVEL = int(sys.argv[index+1],base=10)
	print(colored('\nFolder: '+os.getcwd().split('/')[-1].upper(),'green'),'\n|')
	main(os.getcwd(),1,'',IGNORED_FOLDER)
	print('\n')