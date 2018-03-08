import re
import requests
import json

'''
def returnCsmoneyDic():
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
	return item
	#with open('csmoney.json', 'w', encoding='utf-8') as f:
		#f.write(json.dumps(json.load(r.text), indent = 4))
	#	f.write(json.dumps(item, indent = 4))

def returnSkinhubDic():
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
	return item
	#with open('skinhub.json', 'w', encoding = 'utf-8') as f:
	#	f.write(json.dumps(item, indent = 4))

def comparePrice(CsmoneyData, SkinhubData):
	# traverse the item in skinhub, and find the list where the skinhubItem is low and CsmoneyItem is high
	SkinhubItemList = SkinhubData.keys()
	priceCompare = {}
	for i in SkinhubItemList:
		priceCompare[i] = [CsmoneyData[i]['p'], float(SkinhubData[i]['price']), CsmoneyData[i]['p'] - float(SkinhubData[i]['price'])]
	answerList = sorted(priceCompare.items(), key = lambda item:item[1][2], reverse = True)
	return answerList
'''

### You can either use with the already existing data from skinhub and csmoney
### You can embed the script from skinhub.py and csmoney.py in to have the instant data from the 2 websites and do the data analysis

if __name__ == '__main__':
	skinhubDic = {}
	csmoneyDic = {}
	with open('skinhub.json', 'r') as f:
		skinhubDic = json.loads(f.read())
	with open('csmoney.json', 'r') as f:
		csmoneyDic = json.loads(f.read())
	skinhubItemList = skinhubDic.keys()
	priceCompare = {}
	#print(csmoneyDic['AK-47 | Redline (Well-Worn)']['p'])
	#print(skinhubDic['AK-47 | Redline (Well-Worn)']['price'])
	#print(csmoneyDic['USP-S | Guardian (Minimal Wear)']['ar'][0]['add_price'])
	for i in skinhubItemList:
		try:
			try:
				priceGap = 0
				for p in csmoneyDic[i]['ar']:
					p_max = p['add_price']
				if (p_max > priceGap):
					priceGap = p_max
			except:
				priceGap = 0
			actualPrice = csmoneyDic[i]['p'] - priceGap
			priceCompare[i] = [actualPrice, float(skinhubDic[i]['price']), actualPrice / float(skinhubDic[i]['price'])]
			#priceCompare[i] = [csmoneyDic[i]['p'] - priceGap, float(skinhubDic[i]['price']), (csmoneyDic[i]['p'] - priceGap) / float(skinhubDic[i]['price'])]
		except:
			continue
	answerList = sorted(priceCompare.items(), key = lambda item:item[1][2], reverse = True)
	with open('compare.json', 'w', encoding = 'utf-8') as f:
		for i in answerList:
			f.write(json.dumps(i, indent = 4))

