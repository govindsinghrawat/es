import helpers
import sys


def interpret_ro_data(data):
  print("Interpreting data:")
  for k,v in data.items():
    try:
      if v["settings"]["index"]["blocks"]["read_only_allow_delete"]:
        print(k)
      except:
        continue
    


if sys.argv[1]:
  url=f"http://{sys.argv[1]}/*/_settings"
else:
  sys.exit(0)
  
payload={}
headers={}


resp=requests.request("GET", url, headers=headers, data=payload)

process_response(resp, interpret_function=interpret_ro_data)
