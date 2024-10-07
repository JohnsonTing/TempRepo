import requests

url = "https://johnsonactest.atlassian.net/rest/api/3/search?jql=project=DRS"


headers = {
  'Key': 'Accept',
  'Value': 'application/json',
  'Authorization': 'Basic am9obnNvbi50aW5nQGF1dG9tYXRpb24tY29uc3VsdGFudHMuY29tOkFUQVRUM3hGZkdGMEJOdGY1X3BjTGpEclF2ZW5BRGRCMWxEMm5nNXZkLVZ0SloxbmNhRF84XzVWbEtkdVF0VzBGLVVaQTFhUHdJc0wxck5PWk82ZFo4WUpkN3otc0xnMDZLOTY2TzNwWlZFUzYxSFdtZ1dCQjVSLUhTQnRNRUlpVjRkSlNZMWpEYTA1QThXb25ibFhic29QUVhXNHBqblZvMUhsNDJmU1l5SHkteE5yVkU0U2NSbz1DREQ3NkYzNA=='
}

response = requests.request("GET", url, headers=headers)

result = response.json()

print(result)