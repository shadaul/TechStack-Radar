import requests
import json

url = 'https://www.arbeitnow.com/api/job-board-api'

response = requests.get(url)

if response.status_code == 200:
    print("we did it")
    raw_data = response.json()
    jobs_list = raw_data['data']
    print(f'Found {len(jobs_list)} jobs')
    print(jobs_list[0]['title'])
    with open('raw_data.json','w', encoding='utf-8') as file:
        json.dump(jobs_list, file,ensure_ascii=False, indent=4)
