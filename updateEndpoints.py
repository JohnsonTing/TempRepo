import requests
import json

id = input("Issue ID? ")
newSummary = str(input("New Summary?"))
print(isinstance(newSummary, str))

url = f"https://johnsonactest.atlassian.net/rest/api/3/issue/{id}"

payload = json.dumps({
  "fields":{
    "summary": newSummary
       #"update":{
          # "summary": [ {"set": newSummary}] 
       #}
  }
})

headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Basic am9obnNvbi50aW5nQGF1dG9tYXRpb24tY29uc3VsdGFudHMuY29tOkFUQVRUM3hGZkdGMEJOdGY1X3BjTGpEclF2ZW5BRGRCMWxEMm5nNXZkLVZ0SloxbmNhRF84XzVWbEtkdVF0VzBGLVVaQTFhUHdJc0wxck5PWk82ZFo4WUpkN3otc0xnMDZLOTY2TzNwWlZFUzYxSFdtZ1dCQjVSLUhTQnRNRUlpVjRkSlNZMWpEYTA1QThXb25ibFhic29QUVhXNHBqblZvMUhsNDJmU1l5SHkteE5yVkU0U2NSbz1DREQ3NkYzNA=='
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
