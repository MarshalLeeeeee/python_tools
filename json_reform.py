import json
import re

def reform1():
	stack = []
	file_name = input("Input the file name: ")
	f = open(file_name, 'r+')
	txt = f.read()
	print(txt)
	print('++++++++++++++++++++++++')
	txt_split = re.split(r'\,', txt)
	#print(txt_split)
	txt_print = []
	for txt_s in txt_split:
		#txt_print.append(len(stack) * '\t')
		print(len(stack) * '\t', end = '')
		for ch in txt_s:
			if (ch == '{' or ch == '['):
				stack.append(ch)
			elif(ch == '}'):
				if (stack[len(stack)-1] == '{'):
					stack.pop()
				else:
					print("Error in extracting json file...")
					exit(1)
			elif(ch == ']'):
				if (stack[len(stack)-1] == '['):
					stack.pop()
				else:
					print("Error in extracting json file...")
					exit(1)
		#txt_print.append(txt_s)
		#txt_print.append('\n')
		print(txt_s + ',')
	#print(txt_print)


def reform2():
	file_name = input("Input the file name: ")
	with open(file_name, 'r+') as f:
		js = json.loads(f.read())
	#print(js)
	print(json.dumps(js, indent = 4))

if __name__ == '__main__':
	#reform1()
	reform2()