import requests
import re
from bs4 import BeautifulSoup

def getResponseTxt(id, header):
	url = 'https://www.steamidfinder.com/lookup/'
	r = requests.get(url + id, headers = header)
	#r = requests.get(url + id)
	try:
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		print("error in visiting the site...")
		return ''

def extractInfo(txt):
	soup = BeautifulSoup(txt, 'html.parser')
	tmp = soup.find_all('div', "modal-body")
	#for i in tmp:
	#	print(i)
	#	print("*******")
	#print('len: ' + str(len(tmp)))
	txt = re.sub(r'\<code\>', '$', str(tmp[0]))
	txt = re.sub(r'\<.*?\>', '', txt)
	info = re.split(r'\n|\s*\$\s*', txt)
	i = 0
	dic = {}
	for i in range(1,5):
		dic[info[2*i-1]] = info[2*i]
	#sprint(dic)
	#print('len : ' + str(len(info)))
	return dic

if __name__ == '__main__':
	#steam_id = input("Input the steam origin id or customed id: ")
	steam_id = '__marshallee__/'
	header = {
		'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'zh-CN,zh;q=0.9,en;q=0.8',
		'referer':'https://www.steamidfinder.com/',
		'upgrade-insecure-requests':'1'}
	txt = getResponseTxt(steam_id, header)
	print(extractInfo(txt))