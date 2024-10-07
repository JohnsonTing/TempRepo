import requests

id = input("Issue ID? ")

url = f"https://johnsonactest.atlassian.net/rest/api/3/issue/{id}/comment"



payload = {
    # 'issue': "DRS-11"
}
headers = {
  'Key': 'Accept',
  'Value': 'application/json',
  'Authorization': 'Basic am9obnNvbi50aW5nQGF1dG9tYXRpb24tY29uc3VsdGFudHMuY29tOkFUQVRUM3hGZkdGMEJOdGY1X3BjTGpEclF2ZW5BRGRCMWxEMm5nNXZkLVZ0SloxbmNhRF84XzVWbEtkdVF0VzBGLVVaQTFhUHdJc0wxck5PWk82ZFo4WUpkN3otc0xnMDZLOTY2TzNwWlZFUzYxSFdtZ1dCQjVSLUhTQnRNRUlpVjRkSlNZMWpEYTA1QThXb25ibFhic29QUVhXNHBqblZvMUhsNDJmU1l5SHkteE5yVkU0U2NSbz1DREQ3NkYzNA=='
}

response = requests.request("GET", url, headers=headers, data=payload)
result = response.json()

for comment in result['comments']:
        author = comment['author']['displayName']
        body = comment['body']['content'][0]['content'][0]['text']
        print(f"Author: {author}")
        print(f"Comment: {body}")
        print("-" * 40)

