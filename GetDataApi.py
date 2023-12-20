import requests

try:    
    api_url = "https://google.co.ini"
    response = requests.get(api_url)
    data = response.status_code
    print(data)
#for i in data:
   # print(i['id'])
except:
    print('Error in connecting url')   