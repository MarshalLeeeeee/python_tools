import requests
import re
import json
from bs4 import BeautifulSoup

def getResponseTxt(id):
	url = 'https://www.steamidfinder.com/lookup/'
	r = requests.get(url + id, headers = header)
	header = {
		'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'zh-CN,zh;q=0.9,en;q=0.8',
		'referer':'https://www.steamidfinder.com/',
		'upgrade-insecure-requests':'1'}
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
	for i in tmp:
		print(i)
		print("*******")
	print('len: ' + str(len(tmp)))
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

def getId(steam_id):
	url = 'https://steamid.xyz/http://steamcommunity.com/id/'
	r = requests.get(url + steam_id)
	info_dic = {}
	try:
		r.raise_for_status()
		tmp = re.split(r'\n', r.text)
		for i in range(90):
			if (i >= 62 and i <= 67):
				#print(tmp[i])
				spt = re.sub(r'\<i\>|\<\/i\> |\<br\>|\r', '', tmp[i])
				spt = re.split(r'\:', spt)
				info_dic[spt[0]] = spt[1]
			if (i >= 74 and i <= 87 and i % 2 == 0):
				spt = re.sub(r'\<input |type=\"text\" |onclick=\"this\.select\(\)\;\" |value=\"|\"\>|\r', '', tmp[i+1])
				#print(spt)
				info_dic[re.sub(r'\r','',tmp[i])] = spt
		return info_dic
	except:
		print("Error...")
		return info_dic

def f1(steam_id):
	txt = getResponseTxt(steam_id)
	print(extractInfo(txt))


if __name__ == '__main__':
	steam_id = input("Input the steam origin id or customed id: ")
	#steam_id = '___marshallee___'
	#f1(steam_id)
	print(json.dumps(getId(steam_id), indent = 4))