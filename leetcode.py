import requests
import json
from bs4 import BeautifulSoup
import re

username = "aartirade"

response = requests.get(f"https://leetcode-stats-api.herokuapp.com/{username}")

if response.status_code != 200:
    print("Failed to fetch user data from LeetCode")
    exit()

soup = BeautifulSoup(response.content, "html.parser")
x = str(soup)
sentences = x.split()
formatted_str = str(sentences).replace('"', "")
formatted_str1 = formatted_str.replace(":", "")

Total_Solved = re.findall(r'totalSolved\d+', formatted_str1)
Total_Solved = re.findall(r'\d+', str(Total_Solved))

easy_match = re.findall(r'easySolved\d+', formatted_str1)
medium_match = re.findall(r'mediumSolved\d+', formatted_str1)
hard_match = re.findall(r'hardSolved\d+', formatted_str1)
points_match = re.findall(r'contributionPoints\d+', formatted_str1)

easy_leetcode = re.findall(r'\d+', str(easy_match))
medium_leetcode = re.findall(r'\d+', str(medium_match))
hard_leetcode = re.findall(r'\d+', str(hard_match))
points_leetcode = re.findall(r'\d+', str(points_match))

print(f"Number of easy problems solved by {username}:", *easy_leetcode)
print(f"Number of medium problems solved by {username}:", *medium_leetcode)
print(f"Number of hard problems solved by {username}:", *hard_leetcode)
print(f"Number of Total problems solved by {username}:", *Total_Solved)
print(f"{username} has", *points_leetcode, "Contribution Points")
