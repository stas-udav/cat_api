import requests

endpoint = "http://api.thecatapi.com/v1"
header = { 'x-api-key' : 'live_ljbdLkSdAuBcUrIViCJhPxU2vhCkjqRKV8tiTGhlHOFg59hm2FUDNqPnQNj1Rtml' }

# Call endpoint authorized(using API Key )
def test_call_endpoint_key():
    endpoint_response = requests.get(endpoint, header)
    status_code = endpoint_response.status_code
    print("response - ", status_code)
    assert status_code == 200

# Call endpoint
def test_call_endpoint():
    endpoint_response = requests.get(endpoint)
    status_code = endpoint_response.status_code
    print("response - ", status_code)
    assert status_code == 200

# Testing search    
def test_search():
    search_response = requests.get(endpoint + "/images/search?limit=15")
    status_code = search_response.status_code
    print("response - ", status_code)
    assert status_code == 200
    search_data = search_response.json()
    print(search_data)

# Test analysis
def test_analysis():
    analysis_response = requests.get(endpoint + "/images/image_id/analysis")
    status_code = analysis_response.status_code
    analysis_response_data = analysis_response.json()
    print(analysis_response_data)
    print(status_code)
    assert status_code == 200

# Upload image test
def upload_image():
    upload_image_response = requests.post(endpoint + "/images/upload", header)
    status_code = upload_image_response.status_code
    upload_image_response_data = upload_image_response.json()
    body = 
    print(status_code)
    print(upload_image_response_data)
