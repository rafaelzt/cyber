
from urllib.parse import urlparse

url = "https://www.42madrid.com/admision-2/"

lst = ["https://www.42madrid.com/actualidad/","https://google.com","http://42sp.org.br/"]


for kkkk in lst:
	# if urlparse(url) in url_lst:
	if (urlparse(url).netloc in kkkk):
		print(kkkk)

