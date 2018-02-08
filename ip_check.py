import requests
import re

def getIP():
	choice = input("If you want to check the address of IP, enter 1\nElse if you want to check the ip and the address of one url, enter 0\nchoice:")
	target = input("please input the IP or URL you want to check: ")
	url_ip = "http://ip.chinaz.com/?IP="
	url_url = "http://ip.chinaz.com/"
	answer = []
	if (choice == 1):
		r = requests.get(url_ip + target)
	else:
		r = requests.get(url_url + target)
	try:
		print(r.url)
		r.raise_for_status()# raise_for_status() is the function for Response object
							# if the status number is not 200, the function throws HTTPError
		r.encoding = r.apparent_encoding
		r_split = re.split('\n', r.text)
		for x in r_split:
			if (re.match(r"[ \t]*<span class=\"Whwtdhalf w[0-9]{2}-[0-9]{1}\">.*</span>", x)):
				answer.append(re.sub(r"[ \t]*</*?span.*?>", '', x))
		n = 1
		#print(answer)
		for x in answer:
			print(x)
			#print('%-10s'%x, end=' ')
			if (n % 4 == 0):
				print('')
			n += 1

	except:
		print("Error happened...")


if __name__ == "__main__":
	getIP()
