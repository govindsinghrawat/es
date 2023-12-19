import requests
import sys

if sys.argv[1]:
  url=f"http://{sys.argv[1]}/*/_settings"
else:
  sys.exit(0)
  
payload={}
headers={}


resp=requests.request("GET", url, headers=headers, data=payload)

if resp.status_code == 200:
  for k,v in resp.json().items():
    try:
      if v["settings"]["index"]["blocks"]["read_only_allow_delete"]:
        print(k)
      except:
        continue
        
    
