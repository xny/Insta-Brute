import requests

pass = "password"
username = "username"
uuid = requests.get('https://httpbin.org/uuid').json()['uuid']


PROXY = {
      "http": f"http://{proxy}",
      "https": f"http://{proxy}"
}

HEAD = {
    'Host': 'i.instagram.com', 
    'Accept': '*/*', 
    'User-Agent': User_Agent(), 
    'Cookie': 'missing', 
    'Accept-Encoding': 'gzip, deflate', 
    'Accept-Language': 'en-US', 
    'X-IG-Capabilities': '3brTvw==', 
    'X-IG-Connection-Type': 'WIFI',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
}
 
DATA = {
    'uuid': uuid.json()['uuid'], 
    'password': pass, 
    'username': username, 
    'device_id': uuid, 
    'from_reg': 'false', 
    '_csrftoken': 'missing', 
    'login_attempt_countn': '0'
}

brute = requests.post('https://i.instagram.com/api/v1/accounts/login/',headers=HEAD, data=DATA,proxies=PROXY, allow_redirects=True)
