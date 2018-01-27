import os
import re
import shutil

s = os.getcwd()
l = os.listdir(s)
target_dir = 'C:\\Users\\MacheNike\\Documents\\GitHub\\SJTU_OnlineJudge'
#print(l)
for dir_name in l:
	os.chdir(s)
	if(os.path.isdir(dir_name) and re.match(r"[0-9]*", dir_name)): # the folder name consists only digit
		os.chdir(target_dir)
		os.mkdir(dir_name)
		os.chdir(s+'\\'+dir_name)
		sx = os.getcwd()
		lx = os.listdir(sx)
		for dir_x in lx:
			if(re.match(r"[0-9]*\(*[0-9]*\)*\.cpp", dir_x)):
				#os.chdir(target_dir)
				#os.mkdir(dir_name)
				#os.chdir(target_dir + '\\' + dir_name)
				open(os.path.join(target_dir + '\\' + dir_name ,dir_x), 'w').write(open(dir_x, 'r').read())


