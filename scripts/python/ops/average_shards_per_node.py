import requests

# Replace with your Elasticsearch URL
es_url = "http://your-elasticsearch-url:9200"

# The API endpoint for `_cat/shards` with JSON format
endpoint = f"{es_url}/_cat/shards?format=json&bytes=b"

nodes = {
    "data_0_0" : {"size_sum" : 1234, "shards": [ "index": index, "shard"}
}

try:
    # Make the HTTP GET request
    response = requests.get(endpoint)
    response.raise_for_status()  # Raise an error for HTTP codes 4xx/5xx
    
    # Parse the JSON response
    shards_info = response.json()

    # [ { "index": "index", "shard" : "0", 
    #     "pripre" : "p/r", "state" : "STARTED". "docs": "2", "store" : "20.9kb", 
    #     "ip" : "10.114.233.200", "node" : "data_0_0" }, {}, {} ...]

    
    for shard in shards:
        # How many shards are on a given node
        if shard["state"] == "STARTED":
            # add shard count to node
            if shard["node"] in nodes.keys():
                nodes[shard["node"]]+=1
            else:
                nodes[shard["node"]]=1

            #sum of size for a given node
            
        
    
    
except requests.exceptions.RequestException as e:
    print(f"Error fetching shards information: {e}")
