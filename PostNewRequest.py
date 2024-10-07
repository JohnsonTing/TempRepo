import requests
import json

url = "https://johnsonactest.atlassian.net/rest/api/3/issue/"

payload = json.dumps({
  "fields": {
    "project": {
      "key": "DRS"
    },
    "summary": "Issue Summary",
    "issuetype": {
      "name": "Bug"
    }
  }
})
headers = {
  'Key': 'Accept',
  'Value': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Basic am9obnNvbi50aW5nQGF1dG9tYXRpb24tY29uc3VsdGFudHMuY29tOkFUQVRUM3hGZkdGMEJOdGY1X3BjTGpEclF2ZW5BRGRCMWxEMm5nNXZkLVZ0SloxbmNhRF84XzVWbEtkdVF0VzBGLVVaQTFhUHdJc0wxck5PWk82ZFo4WUpkN3otc0xnMDZLOTY2TzNwWlZFUzYxSFdtZ1dCQjVSLUhTQnRNRUlpVjRkSlNZMWpEYTA1QThXb25ibFhic29QUVhXNHBqblZvMUhsNDJmU1l5SHkteE5yVkU0U2NSbz1DREQ3NkYzNA==',
  'Cookie': 'atlassian.xsrf.token=45f5f67c30641466752004e68d94222e38b405f0_lin'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
