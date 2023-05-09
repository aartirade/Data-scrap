import requests
from bs4 import BeautifulSoup
import re


username = "aartirade"

response = requests.get(f"https://auth.geeksforgeeks.org/user/{username}/practice/", headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"
})

if response.status_code != 200:
    print("Failed to fetch user data from GeeksforGeeks")
    exit()

soup = BeautifulSoup(response.content, "html.parser")

problem_elements = soup.find_all("li", {"class": "tab"})
y = str(problem_elements)

sentences = y.split()
formatted_str = y.replace(" ", "")
formatted_str1 = formatted_str.replace("(", "")

medium_match = re.findall(r'MEDIUM\d+', formatted_str1)
hard_match = re.findall(r'HARD\d+', formatted_str1)
easy_match = re.findall(r'EASY\d+', formatted_str1)

medium = re.findall(r'\d+', str(medium_match))
hard = re.findall(r'\d+', str(hard_match))
easy = re.findall(r'\d+', str(easy_match))
print(f"Number of medium problems solved by {username}:", *medium)
print(f"Number of hard problems solved by {username}:", *hard)
print(f"Number of easy problems solved by {username}:", *easy)
