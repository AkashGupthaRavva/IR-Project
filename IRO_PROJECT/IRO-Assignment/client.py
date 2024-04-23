import requests
import json

url = 'http://localhost:5000/search'  # Adjust the URL if necessary
data = {'query': 'Academic projects'}  # Replace 'your_search_query_here' with your actual search query

headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.json())
