import requests
banner = '''
      | |             | |                                    
   ___| |__   ___  ___| | ________ _ __  _ __ _____  ___   _ 
  / __| '_ \ / _ \/ __| |/ /______| '_ \| '__/ _ \ \/ / | | |
 | (__| | | |  __/ (__|   <       | |_) | | | (_) >  <| |_| |
  \___|_| |_|\___|\___|_|\_\      | .__/|_|  \___/_/\_\\__, |
                                  | |                   __/ |
                                  |_|                  |___/ 
                                  coded by: @foxeditor
                                  channel: @montelisa
'''
print(banner)

with open('result.txt', 'a') as result_file:
    with open('prox.txt') as f:
        for line in f: 
            proxy_url = line.rstrip('\r\n') 
            print(proxy_url)
            proxies = {
                  "http": "http://"+proxy_url,
                  "https": "http://"+proxy_url,
            } 
            try:
                 r = requests.get("https://vk.com", proxies=proxies) 
                 if r.status_code==200: 
                      print(str(proxy_url)+'-is good')
                      result_file.write(line)
            except requests.exceptions.ConnectionError as errc:
                 continue
print ("Proxies Have Been Checkedsss") 