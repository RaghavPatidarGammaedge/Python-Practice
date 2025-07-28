import requests
from requests.auth import HTTPBasicAuth

response = requests.get('http://api.github.com/users/aditya2104')
print(response.text)
print(response.status_code)
print(response.content)
print(response.json())
print("-------------------")
print("-------------------")
print("-------------------")


payload = {'xys': 'test', 'sads': 'test123'}
response = requests.post("https://httpbin.org/post", data=payload)
print(response.text)
print(response.status_code)
print("-------------------")
print("-------------------")
print("-------------------")


payload = {'xys': 't1', 'sads': 'test'}
response = requests.put("https://httpbin.org/put", data=payload)
print(response.text)
print(response.status_code)
print("-------------------")
print("-------------------")
print("-------------------")

response = requests.get(
    'https://api.github.com/users',
    auth=HTTPBasicAuth('raghav.patidar@gammaedge.io', 'raghavGammaedge')
)
print(requests.exceptions.RequestException)

print(response.status_code)
print(response.text)
print(response.headers)


