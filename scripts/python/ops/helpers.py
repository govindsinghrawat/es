import requests
import json

def make_api_request(url, headers=None, payload=None, method='GET'):
    # Validate URL format
    try:
        response = requests.request(method, url, headers=headers, json=payload)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

        # Return success response
        return {
            "data": response.json(),
            "error": None,
            "status": response.status_code
        }

    except requests.exceptions.RequestException as e:
        # Return error response for request exceptions
        return {
            "data": None,
            "error": str(e),
            "status": getattr(e, 'response', None) and e.response.status_code or None
        }

    except Exception as e:
        # Return generic error response
        return {
            "data": None,
            "error": str(e),
            "status": None
        }


def process_response(response_dict, interpret_function):
    status_code = response_dict.get("status", None)
    error_message = response_dict.get("error", None)

    if status_code == 200:
        # Call the interpret function on the data element
        data_value = response_dict.get("data", None)
        interpret_function(data_value)
    else:
        # Print error information
        print(f"Error: {error_message}, Status Code: {status_code}")

# Example interpret function
# def interpret_data(data):
#     print("Interpreting data:")
#     print(data)

# Example response dictionary
# response_dict = {
#     "data": {"key": "value"},
#     "error": None,
#     "status": 200
# }

# Process the response using the process_response function
# process_response(response_dict, interpret_function=interpret_data)

# Example usage:
if __name__ == "__main__":
  url = "https://jsonplaceholder.typicode.com/todos/1"
  headers = {'Content-Type': 'application/json'}
  payload = None
  method = 'GET'
  
  result = make_api_request(url, headers=headers, payload=payload, method=method)
  print(json.dumps(result, indent=2))
