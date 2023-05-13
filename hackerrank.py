import requests
from bs4 import BeautifulSoup

username = "aartirade"
profile_url = f'https://www.hackerrank.com/{username}'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(profile_url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

badges = []

target_class = 'hacker-badge'
elements = soup.find_all(class_=target_class)

data_list = [element.text.strip() for element in elements]

for data in data_list:
    badges.append(data)

print(f"{username} has earned", len(badges), "Badges")
print("list of badges are:", badges)
