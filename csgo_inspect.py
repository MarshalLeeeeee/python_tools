import requests
import re
import os
import json

def dealUrl(url):
	deal_url = re.sub(r'\/', '%2F', url)
	deal_url = re.sub(r'\:', '%3A', deal_url)
	deal_url = re.sub(r'\+', '%2B', deal_url)
	return deal_url

def getScreenId(request_url, header):
	response = requests.get(request_url, headers = header)
	try:
		response.raise_for_status()
		info = json.loads(response.text)
		#print(info['result']['screen_id'])
		return info['result']['screen_id']
	except:
		print("Error in getting screen id...")

def getImgURL(screen_id):
	url = 'https://metjm.net/shared/screenshots-v5.php?cmd=request_screenshot_status&id=' + str(screen_id)
	response = requests.get(url)
	try:
		response.raise_for_status()
		info = json.loads(response.text)
		print(info['result']['image_url'])
		return info['result']['image_url']
	except:
		print('Error in returning image url...')

def saveImg(url, path):
	response = requests.get(url)
	name = re.split(r'\/', url)[-1]
	try:
		response.raise_for_status()
		with open(os.path.join(path, name), 'wb') as f:
			f.write(response.content)
	except:

		print("Error in saving the image...")


if __name__ == '__main__':
	inspect_url = input("please input the inspect url: ")
	path = input("please input the directory saving the image: ")
	deal_url = dealUrl(inspect_url)
	url = 'https://metjm.net/shared/screenshots-v5.php?cmd=request_new_link&inspect_link='
	url_tail = '&user_uuid=08ab67ed-c29d-6de2-92d5-be42042b83bb&user_client=1&custom_rotation_id=0&use_logo=0&mode=7&resolution=4&forceOpskins=0'
	header = {
		'accept':'*/*',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'zh-CN,zh;q=0.9,en;q=0.8',
		'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
	}
	request_url = url + deal_url + url_tail
	screen_id = getScreenId(request_url, header)
	image_url = getImgURL(screen_id)
	saveImg(image_url, path)
	print("over...")



