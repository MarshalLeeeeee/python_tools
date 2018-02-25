import requests
import json
import re

def returnDic():
	url = 'https://cs.money/load_bots_inventory?hash=1519522976353'
	header = {
		'accept':'*/*',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'zh-CN,zh;q=0.9,en;q=0.8',
		'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
		}
	r = requests.get(url, headers = header)
	r.encoding = 'utf-8'
	js = json.loads(r.text)
	item = {}
	for i in js:
		item[i['m']] = i
	with open('csmoney2.txt', 'w', encoding='utf-8') as f:
		#f.write(json.dumps(json.load(r.text), indent = 4))
		f.write(json.dumps(item, indent = 4))


if __name__ == '__main__':
	returnDic()