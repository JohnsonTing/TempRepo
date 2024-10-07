import requests
import base64
import json
from datetime import datetime

#second API token: ATATT3xFfGF0-2FV16BrXyUfK4nBcN1-B2Wbe9-Hv1CRmUTMPoQJljFRG7LjHKE_68Pga953mULJSB8ThT6omQ7G04eyM4vXJCBGcgKP581f31e_9hzfL93lwMV2tfXTaGE0ATWXWad70gSQdnT9J9ex_Pq5UW2siDEurahNHr7QR2g0UZJa3VM=0BE8D763

id = input("project ID? ")
email = input("Assigned user email? ")
api = input("Jira API credentials? ")

authToken = base64.b64encode(f"{email}:{api}".encode('ascii')).decode('ascii')


url = f"https://johnsonactest.atlassian.net/rest/api/3/search?jql=project='{id}'&status!='Closed'"



payload = {
    # 'issue': "DRS-11"
}
headers = {
  'Key': 'Accept',
  'Value': 'application/json',
  'Authorization': f'Basic {authToken}'
}

response = requests.request("GET", url, headers=headers, data=payload)
result = response.json()

print(result)

# with open('DRS.json', 'w', encoding='utf-8') as f:
#      json.dump(result, f, ensure_ascii=False, indent=4)

newJson = {
}

for issue in result['issues']:
    dueDate = issue["fields"]["duedate"]
    due_date_obj = datetime.strptime(due_date, '%Y-%m-%d')
    today = datetime.today()
    difference = (due_date_obj - today).days
    if difference < 3:
      issue['fields']['priority']['name'] = "High"
      issue['assignee'] = email



      url = "https://johnsonactest.atlassian.net/rest/api/3/issue/"

      payload = json.dumps(issue)
      headers = {
        'Key': 'Accept',
        'Value': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Basic am9obnNvbi50aW5nQGF1dG9tYXRpb24tY29uc3VsdGFudHMuY29tOkFUQVRUM3hGZkdGMEJOdGY1X3BjTGpEclF2ZW5BRGRCMWxEMm5nNXZkLVZ0SloxbmNhRF84XzVWbEtkdVF0VzBGLVVaQTFhUHdJc0wxck5PWk82ZFo4WUpkN3otc0xnMDZLOTY2TzNwWlZFUzYxSFdtZ1dCQjVSLUhTQnRNRUlpVjRkSlNZMWpEYTA1QThXb25ibFhic29QUVhXNHBqblZvMUhsNDJmU1l5SHkteE5yVkU0U2NSbz1DREQ3NkYzNA==',
        'Cookie': 'atlassian.xsrf.token=45f5f67c30641466752004e68d94222e38b405f0_lin'
      }

      response = requests.request("POST", url, headers=headers, data=payload)

      print(response.text)


# for comment in result['comments']:
#         author = comment['author']['displayName']
#         body = comment['body']['content'][0]['content'][0]['text']
#         print(f"Author: {author}")
#         print(f"Comment: {body}")
#         print("-" * 40)

