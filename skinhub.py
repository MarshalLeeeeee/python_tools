import requests
import json
import re

def returnDic():
	n = 1
	item = {}
	while(n <= 16):
		url = 'https://api.skinhub.com/api/case_items?min=0.05&page=' + str(n) + '&search='
		header = {
			'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'accept-encoding':'gzip, deflate, br',
			'accept-language':'zh-CN,zh;q=0.9,en;q=0.8',
			'cache-control':'max-age=0',
			'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
		}
		r = requests.get(url, headers = header)
		if not (r.text):
			break
		r.encoding = 'utf-8'
		js = json.loads(r.text)
		dic = {}
		for i in js['case_items']:
			item[i['name']] = i
		#with open('skinhub.txt', 'a', encoding='utf-8') as f:
		#	#f.write(json.dumps(json.load(r.text), indent = 4))
		#	f.write(r.text)
		n += 1
	with open('skinhub2.txt', 'w', encoding = 'utf-8') as f:
		f.write(json.dumps(item, indent = 4))


if __name__ == '__main__':
	returnDic()