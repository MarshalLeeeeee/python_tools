import os
import re

s = os.getcwd()
l = os.listdir(s)
print(l)
for dir_name in l:
	os.chdir(s)
	if(os.path.isdir(dir_name) and re.match(r"[0-9]*", dir_name)):
		os.chdir(s+'\\'+dir_name)
		sx = os.getcwd()
		lx = os.listdir(sx)
		for dir_x in lx:
			if(re.match(r".*\.cpp", dir_x) and not re.match(r"[0-9]*\(*[0-9]*\)*\.cpp", dir_x)):
				cnt = 1
				try:
					os.rename(dir_x, dir_name+'.cpp')
				except FileExistsError:
					os.rename(dir_x, dir_name+'('+str(cnt)+').cpp')
					cnt += 1
				print(str(os)+'\\'+dir_x)
				#fp = open(sx+'\\'+dir_x)
				#print(dir_x + ':')
				#for line in fp.readlines():
				#	print(line)
