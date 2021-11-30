import requests

print(type(requests.get('http://www.naver.com')))
# <class 'requests.models.Response'>
print(type(requests.post('http://www.google.com')))
# <class 'requests.models.Response'>

