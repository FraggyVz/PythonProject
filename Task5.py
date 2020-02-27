#Use the requests library
import requests
#Set the target website
url = 'http://172.17.50.43/freebix'
r = requests.get(url)
#This will get the full page
print(r.text)

#This will get the status code
print('Status code:')
print('\t*', r.status_code)

#This will get just the headers
h = requests.head(url)
print('Header:')
print('******')
#To display line by line
for x in h.headers:
    print('\t',x,':',h.headers[x])
print('******')

#This will modify the Header user-agent to display 'Mobile'
headers = {
    'User-Agent':'Mobile'
}
