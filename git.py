import requests
import datetime
import json
username = "aartirade"

current_year = datetime.datetime.now().year

url = f"https://api.github.com/users/{username}/events"
url2 = f"https://api.github.com/users/{username}"
response = requests.get(url)
response2 = requests.get(url2)

user_data = json.loads(response2.text)

if response.status_code == 200:
    events = response.json()
    num_commits = 0
    for event in events:
        if event["type"] == "PushEvent":
            event_year = datetime.datetime.strptime(
                event["created_at"], "%Y-%m-%dT%H:%M:%SZ").year
            if event_year == current_year:
                num_commits += len(event["payload"]["commits"])

    print(f"{username} has made {num_commits} commits in {current_year}.")
else:
    print("Failed to fetch data from GitHub API.")

print(f"{username} has", user_data["public_repos"], "Public Repos")
