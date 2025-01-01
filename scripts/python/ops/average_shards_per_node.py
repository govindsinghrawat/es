import requests

# Replace with your Elasticsearch URL
es_url = "http://your-elasticsearch-url:9200"

# The API endpoint for `_cat/shards` with JSON format
endpoint = f"{es_url}/_cat/shards?format=json"

try:
    # Make the HTTP GET request
    response = requests.get(endpoint)
    response.raise_for_status()  # Raise an error for HTTP codes 4xx/5xx
    
    # Parse the JSON response
    shards_info = response.json()

    # [ { "index": "index", "shard" : "0", 
    #     "pripre" : "p/r", "state" : "STARTED". "docs": "2", "store" : "20.9kb", 
    #     "ip" : "10.114.233.200", "node" : "data_0_0" }, {}, {} ...]
    
    
except requests.exceptions.RequestException as e:
    print(f"Error fetching shards information: {e}")
