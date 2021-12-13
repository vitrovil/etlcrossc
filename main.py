import requests
import json

page = 1
PAG = []
DAT = []

while page < 10001:
    url = 'http://challenge.dienekes.com.br/api/numbers?page=%s'%page
    data = requests.get(url)
    page = page + 1
    print('PAGE', page-1, 'WAS SUCCEFFULLY EXTRACTED')
    DAT.append(data.json())
    if page == 10001:    
        print('EXTRACTED DATA:', DAT)
        print('TOTAL PAGES EXTRACTED:', page-1)
