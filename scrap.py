import requests
import json

# URL of the user profile on GitHub
url = "https://api.github.com/users/aartirade"

# Send a GET request to the API endpoint
response = requests.get(url)

# Convert the response to JSON format
user_data = json.loads(response.text)
data = json.loads(response.content)
print(data)
# Print the user's name and email
print("Name:", user_data["name"])
print("Email:", user_data["email"])
print("Repos:", user_data["public_repos"])
