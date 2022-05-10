import requests

for i in range(20):
    res = requests.get('https://zipcloud.ibsnet.co.jp/api/search?zipcode=100000i')
    print(res.status_code)
    print(res.text)
    res_json = res.json()
    results = res_json['results'][0]
    address = results['address1'] + results['address2'] + results['address3']
    print(address)