import requests

url = 'http://127.0.0.1:5000/api/jobs'
response = requests.get(url=url)
print(response.json())


url = 'http://127.0.0.1:5000/api/jobs/1'
response = requests.get(url=url)
print(response.json())

url = 'http://127.0.0.1:5000/api/jobs/105'
response = requests.get(url=url)
print(response.json())

url = 'http://127.0.0.1:5000/api/jobs/gggg'
response = requests.get(url=url)
print(response.json())