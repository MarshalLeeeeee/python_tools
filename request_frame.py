import requests

def getHTML():
	url = input("Input the url you want to visit: ")
	r = requests.get(url)# requests.get() returns Response object
	try:
		r.raise_for_status()# raise_for_status() is the function for Response object
							# if the status number is not 200, the function throws HTTPError
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return "Error..."


if __name__ == "__main__":
	print(getHTML())
