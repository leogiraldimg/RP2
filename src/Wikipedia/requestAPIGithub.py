import requests
import json
import datetime

def dateRange (start_date, end_date):
    if start_date <= end_date:
        for n in range((end_date - start_date).days + 1):
            yield start_date + datetime.timedelta(n)
    else:
        for n in range((start_date - end_date).days + 1 ):
            yield start_date - datetime.timedelta( n )

target_user = 'wikimedia'
target_repos = 'apps-android-wikipedia'
auth_username = 'leogiraldimg'
auth_token = '59150587c246f5e3766aaf341fbe887f26ba76fb'
date_start = datetime.date(year=2013, month=10, day=30)
date_end = datetime.date(year=2019, month=8, day=25)
json_response = {}

for date in dateRange (date_start, date_end):
    since = str(date) + "T00:00:00Z"
    until = str(date) + "T23:59:59Z"

    response = requests.get('https://api.github.com/repos/' + target_user + '/' + target_repos + '/commits', auth=(auth_username, auth_token), params={'since': since, 'until': until})

    json_string_response = json.loads(response.text)
    json_response = json.dumps(json_string_response, indent=2, sort_keys=True)
    
    with open('data.json', 'a+') as f:
        f.write(json_response)